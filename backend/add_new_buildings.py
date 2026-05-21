#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""添加新的古建筑数据"""

import sqlite3

# 连接到数据库
db_path = 'db.sqlite3'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 新建筑数据
new_buildings = [
    {
        'bid': 7,
        'bname': '大明宫',
        'dynasty_id': 3,  # 唐代
        'region_id': 6,   # 西北
        'structure_type_id': 1,  # 殿宇
        'roof_type': '重檐庑殿顶',
        'dougong_style': '七铺作斗拱',
        'longitude': 108.9465,
        'latitude': 34.2658,
        'address': '陕西省西安市新城区自强东路585号',
        'introduction': '大明宫是唐代的皇宫，始建于唐太宗贞观八年（634年），是唐长安城三大宫之一。',
        'historical_value': '大明宫是中国古代宫殿建筑的巅峰之作，体现了唐代的建筑技术水平和艺术成就。',
        'architectural_features': '大明宫采用前朝后寝的布局，主要建筑有含元殿、宣政殿、紫宸殿等。',
        'liang_sicheng_note': '大明宫是中国古代宫殿建筑的杰作，规模宏大，布局严谨。',
        'image_url': 'img/大明宫-唐代-陕西西安/daming_01.jpg',
    },
    {
        'bid': 8,
        'bname': '大雁塔',
        'dynasty_id': 3,  # 唐代
        'region_id': 6,   # 西北
        'structure_type_id': 2,  # 佛塔
        'roof_type': '四角攒尖顶',
        'dougong_style': '砖石仿木结构',
        'longitude': 108.9604,
        'latitude': 34.2175,
        'address': '陕西省西安市雁塔区雁塔路南段11号大慈恩寺内',
        'introduction': '大雁塔又称大慈恩寺塔，建于唐永徽三年（652年），是玄奘法师为保存从印度带回的佛经而建造的。',
        'historical_value': '大雁塔是唐代佛教建筑的杰出代表，也是中印文化交流的见证。',
        'architectural_features': '大雁塔为七层四方楼阁式砖塔，塔身呈方形锥体，逐层递减。',
        'liang_sicheng_note': '大雁塔是唐代佛塔建筑的典范，造型简洁大方，结构稳固。',
        'image_url': 'img/大雁塔-唐代-陕西西安/dayan_01.jpg',
    },
    {
        'bid': 9,
        'bname': '永乐宫',
        'dynasty_id': 7,  # 元代
        'region_id': 1,   # 华北
        'structure_type_id': 1,  # 殿宇
        'roof_type': '单檐庑殿顶',
        'dougong_style': '五铺作斗拱',
        'longitude': 110.6944,
        'latitude': 34.6986,
        'address': '山西省运城市芮城县永乐镇',
        'introduction': '永乐宫建于元定宗二年（1247年），是为纪念八仙之一吕洞宾而建的道教宫观。',
        'historical_value': '永乐宫是中国现存最完整的元代道教建筑群，宫内壁画总面积达960平方米。',
        'architectural_features': '永乐宫主要建筑有龙虎殿、三清殿、纯阳殿、重阳殿等。',
        'liang_sicheng_note': '永乐宫是元代建筑的杰出代表，建筑布局和壁画艺术都达到了很高的水平。',
        'image_url': 'img/永乐宫-元代-山西芮城/yongle_01.jpg',
    },
    {
        'bid': 10,
        'bname': '天坛祈年殿',
        'dynasty_id': 8,  # 明代
        'region_id': 1,   # 华北
        'structure_type_id': 1,  # 殿宇
        'roof_type': '三重檐攒尖顶',
        'dougong_style': '无斗拱（梁架结构）',
        'longitude': 116.4066,
        'latitude': 39.8822,
        'address': '北京市东城区天坛路甲1号天坛公园内',
        'introduction': '天坛祈年殿建于明永乐十八年（1420年），是明清皇帝祭天的场所。',
        'historical_value': '祈年殿是中国古代祭祀建筑的最高成就，体现了中国古代天人合一的哲学思想。',
        'architectural_features': '祈年殿为圆形三重檐攒尖顶，高38米，直径32米。',
        'liang_sicheng_note': '天坛祈年殿是中国古代祭祀建筑的巅峰之作，建筑形式独特，寓意深刻。',
        'image_url': 'img/天坛祈年殿-明代-北京/qinian_01.jpg',
    },
]

added_count = 0

for building in new_buildings:
    try:
        # 检查建筑是否已存在
        cursor.execute('SELECT bid FROM architecture_building WHERE bid = ?', (building['bid'],))
        if cursor.fetchone():
            print(f"Building {building['bid']} already exists: {building['bname']}")
            continue
        
        # 插入新建筑数据
        cursor.execute('''
            INSERT INTO architecture_building 
            (bid, bname, dynasty_id, region_id, structure_type_id, roof_type, dougong_style,
             longitude, latitude, address, introduction, historical_value, architectural_features,
             liang_sicheng_note, image_url)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            building['bid'], building['bname'], building['dynasty_id'], building['region_id'],
            building['structure_type_id'], building['roof_type'], building['dougong_style'],
            building['longitude'], building['latitude'], building['address'],
            building['introduction'], building['historical_value'], building['architectural_features'],
            building['liang_sicheng_note'], building['image_url']
        ))
        
        added_count += 1
        print(f"Added new building {building['bid']}: {building['bname']}")
        
    except Exception as e:
        print(f"Error adding building {building['bid']}: {str(e)}")

# 提交更改
conn.commit()
conn.close()

print(f'\nDone! Added {added_count} new buildings')
