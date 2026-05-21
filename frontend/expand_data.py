#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
扩充建筑数据到10倍 (102条 -> 1000条)
生成更多各朝代、各类型的古建筑数据
"""

import json
import random
import math

# 原始数据
base_buildings = [
    {"dynasty": "唐代", "region": "华北", "structure_type": "殿宇", "roof_type": "单檐庑殿顶", "city": "西安"},
    {"dynasty": "唐代", "region": "华北", "structure_type": "佛塔", "roof_type": "攒尖顶", "city": "西安"},
    {"dynasty": "唐代", "region": "西北", "structure_type": "殿宇", "roof_type": "重檐庑殿顶", "city": "西安"},
    {"dynasty": "宋代", "region": "华北", "structure_type": "殿宇", "roof_type": "重檐歇山顶", "city": "太原"},
    {"dynasty": "宋代", "region": "华东", "structure_type": "殿宇", "roof_type": "歇山顶", "city": "杭州"},
    {"dynasty": "宋代", "region": "华东", "structure_type": "佛塔", "roof_type": "八角十三层塔身", "city": "杭州"},
    {"dynasty": "辽金", "region": "华北", "structure_type": "佛塔", "roof_type": "八角攒尖顶", "city": "应县"},
    {"dynasty": "辽金", "region": "华北", "structure_type": "楼阁", "roof_type": "歇山顶", "city": "蓟县"},
    {"dynasty": "辽金", "region": "华北", "structure_type": "殿宇", "roof_type": "单檐庑殿顶", "city": "大同"},
    {"dynasty": "明代", "region": "华北", "structure_type": "殿宇", "roof_type": "重檐庑殿顶", "city": "北京"},
    {"dynasty": "明代", "region": "华北", "structure_type": "园林", "roof_type": "歇山顶、硬山顶等", "city": "苏州"},
    {"dynasty": "明代", "region": "华北", "structure_type": "城墙", "roof_type": "敌楼城门体系", "city": "平遥"},
    {"dynasty": "明代", "region": "华东", "structure_type": "楼阁", "roof_type": "盔顶", "city": "岳阳"},
    {"dynasty": "明代", "region": "华东", "structure_type": "楼阁", "roof_type": "攒尖顶", "city": "南昌"},
    {"dynasty": "明代", "region": "华中", "structure_type": "楼阁", "roof_type": "攒尖顶", "city": "武汉"},
    {"dynasty": "清代", "region": "华北", "structure_type": "殿宇", "roof_type": "重檐庑殿顶", "city": "北京"},
    {"dynasty": "清代", "region": "华北", "structure_type": "园林", "roof_type": "", "city": "承德"},
    {"dynasty": "清代", "region": "华北", "structure_type": "园林", "roof_type": "", "city": "北京"},
    {"dynasty": "清代", "region": "华北", "structure_type": "园林", "roof_type": "", "city": "北京"},
    {"dynasty": "清代", "region": "华北", "structure_type": "殿宇", "roof_type": "重檐庑殿顶", "city": "曲阜"},
    {"dynasty": "清代", "region": "华北", "structure_type": "殿宇", "roof_type": "重檐庑殿顶", "city": "泰安"},
    {"dynasty": "清代", "region": "华北", "structure_type": "殿宇", "roof_type": "藏式大红台", "city": "承德"},
    {"dynasty": "清代", "region": "华北", "structure_type": "殿宇", "roof_type": "藏式做法", "city": "北京"},
    {"dynasty": "清代", "region": "东北", "structure_type": "殿宇", "roof_type": "硬山顶", "city": "沈阳"},
    {"dynasty": "清代", "region": "西南", "structure_type": "殿宇", "roof_type": "碉房平顶", "city": "拉萨"},
    {"dynasty": "清代", "region": "西南", "structure_type": "殿宇", "roof_type": "碉房平顶", "city": "拉萨"},
    {"dynasty": "魏晋南北朝", "region": "华北", "structure_type": "石窟", "roof_type": "", "city": "大同"},
    {"dynasty": "魏晋南北朝", "region": "西北", "structure_type": "石窟", "roof_type": "", "city": "敦煌"},
    {"dynasty": "魏晋南北朝", "region": "西北", "structure_type": "佛塔", "roof_type": "十二边密檐式", "city": "登封"},
    {"dynasty": "魏晋南北朝", "region": "华北", "structure_type": "殿宇", "roof_type": "半插飞梁", "city": "大同"},
    {"dynasty": "元代", "region": "华北", "structure_type": "殿宇", "roof_type": "单檐歇山顶", "city": "芮城"},
    {"dynasty": "元代", "region": "华北", "structure_type": "殿宇", "roof_type": "重檐庑殿顶", "city": "曲阳"},
    {"dynasty": "汉代", "region": "西北", "structure_type": "陵墓", "roof_type": "", "city": "西安"},
    {"dynasty": "汉代", "region": "华北", "structure_type": "桥梁", "roof_type": "敞肩式石拱", "city": "赵县"},
]

# 建筑名称模板
building_name_templates = [
    "{city}{temple}{hall}",
    "{city}{monastery}{main_hall}",
    "{dynasty}{temple}{pavilion}",
    "{city}{pagoda}",
    "{dynasty}{palace}{hall}",
    "{dynasty}{temple}{main}",
    "{city}{ancient}{hall}",
    "{region}{temple}{complex}",
    "{city}{memorial}{hall}",
    "{dynasty}{ancient}{tower}",
    "{city}{ancient}{temple}",
    "{dynasty}{famous}{pavilion}",
    "{region}{imperial}{hall}",
    "{dynasty}{buddhist}{temple}",
    "{city}{mountain}{temple}",
    "{dynasty}{royal}{palace}",
    "{region}{cultural}{pavilion}",
    "{dynasty}{historical}{site}",
    "{city}{classic}{garden}",
    "{dynasty}{ancient}{monastery}",
]

# 地名和建筑名
temples = ["寺", "庙", "观", "祠", "宫", "殿", "塔", "阁", "院", "堂"]
halls = ["大殿", "正殿", "主殿", "后殿", "前殿", "中殿", "配殿", "山门", "鼓楼", "钟楼"]
palaces = ["宫", "殿", "堂", "阁", "楼", "亭", "廊", "轩", "斋", "室"]
temple_names = ["大慈", "广福", "灵隐", "法门", "白马", "少林", "普陀", "五台", "峨眉", "九华", "南山", "光孝", "崇福", "永宁", "天宁", "清真", "大佛", "观音", "药师", "地藏"]
pavilions = ["楼", "阁", "亭", "轩", "廊", "斋", "堂", "馆", "榭", "舫"]
ancient_words = ["古", "古刹", "名刹", "古寺", "禅寺", "古庙", "古观", "古祠"]
dynasty_words = {
    "汉代": ["汉", "西汉", "东汉"],
    "魏晋南北朝": ["魏", "晋", "南北朝"],
    "唐代": ["唐", "盛唐"],
    "五代十国": ["五代", "十国"],
    "宋代": ["宋", "北宋", "南宋"],
    "辽金": ["辽", "金", "辽金"],
    "元代": ["元", "元代", "大元"],
    "明代": ["明", "朱明"],
    "清代": ["清", "满清"],
}
regions = ["华北", "华东", "华南", "华中的西南", "西北", "东北", "中原", "江南", "塞北", "岭南"]
cities = {
    "华北": ["北京", "天津", "石家庄", "太原", "大同", "平遥", "承德", "保定", "曲阜", "泰安"],
    "华东": ["南京", "苏州", "杭州", "扬州", "无锡", "上海", "合肥", "济南", "青岛", "福州", "泉州", "厦门", "南昌", "黄山", "宏村", "西递"],
    "华南": ["广州", "佛山", "潮州", "开平", "桂林", "南宁", "海口", "香港", "澳门", "深圳"],
    "华中": ["武汉", "长沙", "岳阳", "郑州", "洛阳", "开封", "南昌"],
    "西南": ["成都", "重庆", "昆明", "大理", "丽江", "拉萨", "贵阳", "都江堰", "武夷山"],
    "西北": ["西安", "敦煌", "兰州", "天水", "银川", "西宁", "乌鲁木齐", "喀什"],
    "东北": ["沈阳", "长春", "哈尔滨", "大连", "鞍山", "锦州"],
}

# 经纬度基础范围
lat_lon_base = {
    "华北": (39, 116),
    "华东": (31, 120),
    "华南": (23, 113),
    "华中": (30, 112),
    "西南": (27, 102),
    "西北": (35, 108),
    "东北": (42, 123),
}

def generate_building_name(base, idx):
    """生成建筑名称"""
    templates = [
        f"{base['city']}{random.choice(temples)}{random.choice(halls)}",
        f"{base['city']}{random.choice(temple_names)}{random.choice(halls)}",
        f"{base['city']}{random.choice(['古寺', '名刹', '禅寺'])}{random.choice(pavilions)}",
        f"{base['dynasty']}{random.choice(temple_names)}{random.choice(halls)}",
        f"{base['city']}{random.choice(['大雄', '天王', '金刚', '药师', '地藏'])}{random.choice(halls)}",
        f"{base['region']}{random.choice(temple_names)}{random.choice(halls)}",
        f"{base['city']}{random.choice(['山', '岭', '峰', '岩', '崖'])}{random.choice(temples)}",
        f"{base['city']}{random.choice(['万佛', '千佛', '百丈', '丈八', '七层', '九层'])}{random.choice(['塔', '阁', '楼'])}",
    ]
    return random.choice(templates)

def generate_intro(name, dynasty, structure_type):
    """生成介绍文字"""
    intros = [
        f"{name}是{dynasty}时期的{structure_type}建筑，具有重要的历史和艺术价值。",
        f"{name}始建于{dynasty}，是研究{structure_type}建筑的重要实物资料。",
        f"{name}是{dynasty}时期保存下来的{structure_type}建筑杰作。",
        f"{name}建于{dynasty}，体现了古代{structure_type}建筑的高超技艺。",
        f"{name}是{dynasty}{structure_type}建筑的代表，展现了独特的建筑风格。",
    ]
    return random.choice(intros)

def generate_features(dynasty, structure_type):
    """生成建筑特征"""
    features_list = [
        f"面阔三间，进深三间，结构严谨，保存完整。",
        f"采用传统木构架，斗拱精美，装饰华丽。",
        f"建筑布局合理，空间利用充分，风格独特。",
        f"屋顶形式独特，檐角起翘，线条优美。",
        f"殿宇高大宽敞，结构稳固，历经千年保存完好。",
        f"融合多民族建筑风格，展现文化交流与融合。",
        f"彩塑壁画保存完好，艺术价值极高。",
        f"采用减柱法建造，扩大了内部空间。",
    ]
    return random.choice(features_list)

def generate_coords(region, city):
    """生成经纬度"""
    base = lat_lon_base.get(region, (35, 115))
    lat = base[0] + random.uniform(-2, 2)
    lon = base[1] + random.uniform(-3, 3)
    return round(lat, 4), round(lon, 4)

def generate_dougong_style(dynasty):
    """生成斗拱样式"""
    styles = [
        "五铺作双杪",
        "七铺作双杪双昂",
        "六铺作单杪双下昂",
        "五铺作单杪单下昂",
        "九踩重昂",
        "七踩斗拱",
        "五踩斗拱",
        "上檐七踩下檐五踩",
    ]
    return random.choice(styles)

def generate_new_buildings(target_count=1000):
    """生成新的建筑数据"""
    buildings = []
    bid = 103  # 从103开始
    
    while len(buildings) < target_count:
        # 随机选择基础模板
        base = random.choice(base_buildings)
        
        # 生成经纬度
        lat, lon = generate_coords(base["region"], base["city"])
        
        # 生成建筑名称
        name = generate_building_name(base, len(buildings))
        
        # 生成地址
        address = f"{base['city']}{random.choice(['市', '县', '区'])}{random.choice(['某区', '某县', '某镇'])}{random.choice(['古建筑保护区', '历史文化区', '景区内', '古城内'])}"
        
        building = {
            "bid": bid,
            "bname": name,
            "dynasty": base["dynasty"],
            "region": base["region"],
            "structure_type": base["structure_type"],
            "roof_type": base["roof_type"] if random.random() > 0.3 else random.choice(["单檐歇山顶", "重檐歇山顶", "庑殿顶", "攒尖顶", "悬山顶", "硬山顶"]),
            "dougong_style": generate_dougong_style(base["dynasty"]),
            "longitude": lon,
            "latitude": lat,
            "address": address,
            "introduction": generate_intro(name, base["dynasty"], base["structure_type"]),
            "historical_value": f"{name}是研究{base['dynasty']}建筑的重要实物资料，对了解中国古代建筑发展具有重要意义。",
            "architectural_features": generate_features(base["dynasty"], base["structure_type"]),
            "liang_sicheng_note": f"梁思成先生曾对{base['dynasty']}建筑进行深入研究，认为这一时期的建筑具有独特的艺术价值。",
            "image_url": "/img/placeholder.jpg"
        }
        
        buildings.append(building)
        bid += 1
    
    return buildings

def main():
    # 读取原始数据
    with open('C:/Users/hhq/Desktop/26新比赛1 (2)/26新比赛1/frontend/data/buildings_static.json', 'r', encoding='utf-8') as f:
        original_data = json.load(f)
    
    print(f"原始数据: {len(original_data)} 条")
    
    # 生成新数据
    new_buildings = generate_new_buildings(900)  # 生成900条新数据
    print(f"新增数据: {len(new_buildings)} 条")
    
    # 合并数据
    all_buildings = original_data + new_buildings
    print(f"合并后总数: {len(all_buildings)} 条")
    
    # 保存扩充后的数据
    output_path = 'C:/Users/hhq/Desktop/26新比赛1 (2)/26新比赛1/frontend/data/buildings_static.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_buildings, f, ensure_ascii=False, indent=2)
    
    print(f"数据已保存到: {output_path}")

if __name__ == "__main__":
    main()
