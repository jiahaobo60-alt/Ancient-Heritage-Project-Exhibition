#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
初始化更多中国古建筑数据
"""

import os
import django

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel.settings')
django.setup()

from api.models_architecture import AncientBuilding, ArchDynasty, ArchRegion, ArchStructureType

def get_or_create_dynasty(name, period):
    """获取或创建朝代"""
    dynasty, created = ArchDynasty.objects.get_or_create(
        dname=name,
        defaults={'period': period}
    )
    return dynasty

def get_or_create_region(name):
    """获取或创建地域"""
    region, created = ArchRegion.objects.get_or_create(rname=name)
    return region

def get_or_create_structure_type(name):
    """获取或创建结构类型"""
    struct_type, created = ArchStructureType.objects.get_or_create(tname=name)
    return struct_type

def create_building(data):
    """创建建筑"""
    # 检查是否已存在
    if AncientBuilding.objects.filter(bname=data['name']).exists():
        print(f"建筑 {data['name']} 已存在，跳过...")
        return
    
    # 获取关联对象
    dynasty = get_or_create_dynasty(data['dynasty_name'], data['dynasty_period'])
    region = get_or_create_region(data['region'])
    struct_type = get_or_create_structure_type(data['structure_type'])
    
    # 创建建筑
    building = AncientBuilding.objects.create(
        bid=data['bid'],
        bname=data['name'],
        roof_type=data.get('roof_type', ''),
        dougong_style=data.get('dougong_style', ''),
        longitude=data.get('longitude', 0),
        latitude=data.get('latitude', 0),
        address=data.get('address', ''),
        introduction=data['introduction'],
        historical_value=data.get('historical_value', ''),
        architectural_features=data.get('architectural_features', ''),
        liang_sicheng_note=data.get('liang_sicheng_note', ''),
        image_url=data.get('image_url', 'img/index/lishi.jpg'),
        model_3d_url=data.get('model_3d_url', ''),
        dynasty=dynasty,
        region=region,
        structure_type=struct_type
    )
    
    print(f"创建建筑: {data['name']}")
    return building

# 建筑数据
buildings_data = [
    {
        'bid': 7,
        'name': '大明宫',
        'dynasty_name': '唐代',
        'dynasty_period': '618年-907年',
        'region': '西北',
        'structure_type': '殿宇',
        'roof_type': '重檐庑殿顶',
        'address': '陕西省西安市未央区',
        'longitude': 108.938,
        'latitude': 34.263,
        'introduction': '大明宫是唐代长安城的皇宫，是中国古代最大的宫殿建筑群之一，占地面积约3.2平方公里。',
        'historical_value': '大明宫是唐代政治中心，见证了盛唐的繁荣与辉煌，是中国古代宫殿建筑的杰出代表。',
        'architectural_features': '布局严谨，规模宏大，建筑风格雄伟壮丽，体现了唐代建筑的最高成就。'
    },
    {
        'bid': 8,
        'name': '大雁塔',
        'dynasty_name': '唐代',
        'dynasty_period': '618年-907年',
        'region': '西北',
        'structure_type': '佛塔',
        'roof_type': '攒尖顶',
        'address': '陕西省西安市雁塔区',
        'longitude': 108.947,
        'latitude': 34.218,
        'introduction': '大雁塔建于唐永徽三年（652年），是为保存玄奘法师从天竺带回的佛经而建。',
        'historical_value': '大雁塔是唐代佛教建筑的重要代表，也是中印文化交流的见证。',
        'architectural_features': '方形七层楼阁式砖塔，高64米，造型简洁大方，体现了唐代佛塔的典型风格。'
    },
    {
        'bid': 9,
        'name': '永乐宫',
        'dynasty_name': '元代',
        'dynasty_period': '1271年-1368年',
        'region': '华北',
        'structure_type': '殿宇',
        'roof_type': '单檐歇山顶',
        'address': '山西省芮城县',
        'longitude': 110.783,
        'latitude': 34.747,
        'introduction': '永乐宫原名大纯阳万寿宫，是元代全真教的重要宫观，以精美壁画著称。',
        'historical_value': '永乐宫壁画是中国古代壁画艺术的瑰宝，保存了大量元代绘画精品。',
        'architectural_features': '宫殿布局严谨，建筑风格融合宋辽金元特色，壁画内容丰富，技艺精湛。'
    },
    {
        'bid': 10,
        'name': '天坛',
        'dynasty_name': '明代',
        'dynasty_period': '1368年-1644年',
        'region': '华北',
        'structure_type': '殿宇',
        'roof_type': '三重檐圆形攒尖顶',
        'address': '北京市东城区',
        'longitude': 116.413,
        'latitude': 39.883,
        'introduction': '天坛是明清两代皇帝祭天的场所，是中国现存最大的古代祭祀性建筑群。',
        'historical_value': '天坛体现了中国古代"天人合一"的哲学思想，是中国古代祭祀建筑的杰出代表。',
        'architectural_features': '祈年殿是天坛的主体建筑，三重檐圆形攒尖顶，蓝色琉璃瓦，象征天圆地方。'
    },
    {
        'bid': 11,
        'name': '岳阳楼',
        'dynasty_name': '明代',
        'dynasty_period': '1368年-1644年',
        'region': '华中',
        'structure_type': '楼阁',
        'roof_type': '盔顶',
        'address': '湖南省岳阳市岳阳楼区',
        'longitude': 113.095,
        'latitude': 29.355,
        'introduction': '岳阳楼始建于三国时期，是江南三大名楼之一，因范仲淹《岳阳楼记》而闻名天下。',
        'historical_value': '岳阳楼是中国古代楼阁建筑的代表，体现了中国传统建筑与文学艺术的完美结合。',
        'architectural_features': '三层盔顶式建筑，飞檐翘角，气势雄伟，登楼可俯瞰洞庭湖美景。'
    },
    {
        'bid': 12,
        'name': '颐和园',
        'dynasty_name': '清代',
        'dynasty_period': '1644年-1912年',
        'region': '华北',
        'structure_type': '园林',
        'address': '北京市海淀区',
        'longitude': 116.275,
        'latitude': 39.998,
        'introduction': '颐和园是清代皇家园林，是中国现存规模最大、保存最完整的皇家园林。',
        'historical_value': '颐和园是中国古典园林艺术的杰作，体现了中国传统园林的审美理念。',
        'architectural_features': '以昆明湖和万寿山为主体，融合了江南园林的精巧与北方园林的雄浑。'
    },
    {
        'bid': 13,
        'name': '避暑山庄',
        'dynasty_name': '清代',
        'dynasty_period': '1644年-1912年',
        'region': '华北',
        'structure_type': '园林',
        'address': '河北省承德市双桥区',
        'longitude': 117.938,
        'latitude': 40.979,
        'introduction': '避暑山庄是清代皇帝的夏宫，是中国现存最大的皇家园林。',
        'historical_value': '避暑山庄是清代政治活动的重要场所，见证了康乾盛世的辉煌。',
        'architectural_features': '融合了江南园林和北方草原风格，兼具皇家气派与自然野趣。'
    },
    {
        'bid': 14,
        'name': '长城',
        'dynasty_name': '明代',
        'dynasty_period': '1368年-1644年',
        'region': '华北',
        'structure_type': '城墙',
        'address': '中国北方',
        'longitude': 116.047,
        'latitude': 40.431,
        'introduction': '长城是中国古代伟大的防御工程，是世界文化遗产。',
        'historical_value': '长城是中国古代军事防御体系的杰出代表，是中华民族的象征。',
        'architectural_features': '城墙高大坚固，敌楼、烽火台等设施完备，绵延万里。'
    },
    {
        'bid': 15,
        'name': '云冈石窟',
        'dynasty_name': '魏晋南北朝',
        'dynasty_period': '220年-589年',
        'region': '华北',
        'structure_type': '石窟',
        'address': '山西省大同市云冈区',
        'longitude': 113.208,
        'latitude': 40.186,
        'introduction': '云冈石窟是北魏时期开凿的佛教石窟群，是中国四大石窟之一。',
        'historical_value': '云冈石窟是中国古代佛教艺术的瑰宝，体现了中西文化的融合。',
        'architectural_features': '现存主要洞窟45个，造像51000余尊，雕刻精美，气势雄伟。'
    },
    {
        'bid': 16,
        'name': '客家土楼',
        'dynasty_name': '明代',
        'dynasty_period': '1368年-1644年',
        'region': '华南',
        'structure_type': '民居',
        'address': '福建省龙岩市永定区',
        'longitude': 116.713,
        'latitude': 24.733,
        'introduction': '客家土楼是客家民居的独特形式，是中国传统民居建筑的杰出代表。',
        'historical_value': '土楼体现了客家人的聚族而居传统，是研究客家文化的重要实物资料。',
        'architectural_features': '圆形或方形，以夯土为主要材料，防御功能与居住功能相结合。'
    },
    {
        'bid': 17,
        'name': '敦煌莫高窟',
        'dynasty_name': '魏晋南北朝',
        'dynasty_period': '220年-589年',
        'region': '西北',
        'structure_type': '石窟',
        'address': '甘肃省敦煌市',
        'longitude': 94.608,
        'latitude': 40.139,
        'introduction': '敦煌莫高窟是世界上现存规模最大、内容最丰富的佛教艺术圣地。',
        'historical_value': '莫高窟保存了大量壁画和彩塑，是研究中国古代艺术、宗教、历史的重要资料。',
        'architectural_features': '洞窟形制多样，壁画色彩鲜艳，内容丰富，技艺精湛。'
    },
    {
        'bid': 18,
        'name': '秦始皇陵',
        'dynasty_name': '汉代',
        'dynasty_period': '前206年-220年',
        'region': '西北',
        'structure_type': '陵墓',
        'address': '陕西省西安市临潼区',
        'longitude': 109.278,
        'latitude': 34.385,
        'introduction': '秦始皇陵是中国历史上第一个皇帝嬴政的陵墓，规模宏大，陪葬品丰富。',
        'historical_value': '秦始皇陵及兵马俑坑是世界文化遗产，展示了秦代的强大国力和高超工艺。',
        'architectural_features': '陵园布局严谨，兵马俑排列整齐，体现了秦代的军事制度和艺术水平。'
    },
    {
        'bid': 19,
        'name': '黄鹤楼',
        'dynasty_name': '明代',
        'dynasty_period': '1368年-1644年',
        'region': '华中',
        'structure_type': '楼阁',
        'roof_type': '攒尖顶',
        'address': '湖北省武汉市武昌区',
        'longitude': 114.305,
        'latitude': 30.540,
        'introduction': '黄鹤楼是江南三大名楼之一，因崔颢《黄鹤楼》诗而闻名天下。',
        'historical_value': '黄鹤楼是中国古代楼阁建筑的代表，体现了中国传统建筑与文学艺术的结合。',
        'architectural_features': '五层攒尖顶建筑，飞檐翘角，气势雄伟，登楼可俯瞰长江美景。'
    },
    {
        'bid': 20,
        'name': '滕王阁',
        'dynasty_name': '明代',
        'dynasty_period': '1368年-1644年',
        'region': '华东',
        'structure_type': '楼阁',
        'roof_type': '攒尖顶',
        'address': '江西省南昌市东湖区',
        'longitude': 115.890,
        'latitude': 28.682,
        'introduction': '滕王阁是江南三大名楼之一，因王勃《滕王阁序》而闻名天下。',
        'historical_value': '滕王阁是中国古代楼阁建筑的代表，体现了中国传统建筑与文学艺术的结合。',
        'architectural_features': '九层攒尖顶建筑，飞檐翘角，气势雄伟，登楼可俯瞰赣江美景。'
    }
]

if __name__ == '__main__':
    print("开始添加更多古建筑数据...")
    count = 0
    for data in buildings_data:
        try:
            create_building(data)
            count += 1
        except Exception as e:
            print(f"创建建筑 {data['name']} 失败: {e}")
    print(f"成功添加 {count} 个建筑数据！")
