#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新建筑图片路径 - 将img文件夹中的图片关联到数据库
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel.settings')
django.setup()

from api.models_architecture import AncientBuilding

BUILDING_IMAGE_MAPPING = {
    '佛光寺东大殿': {
        'folder': '佛光寺东大殿-唐代-山西五台山',
        'images': ['foguang_01.jpg', 'foguang_02.jpg', 'foguang_03.jpg', 'foguang_04.jpg', 'foguang_05.jpg']
    },
    '大明宫': {
        'folder': '大明宫-唐代-陕西西安',
        'images': ['daming_01.jpg', 'daming_02.jpg', 'daming_03.jpg', 'daming_04.jpg', 'daming_05.jpg']
    },
    '大雁塔': {
        'folder': '大雁塔-唐代-陕西西安',
        'images': ['dayan_01.jpg', 'dayan_03.jpg', 'dayan_04.jpg', 'dayan_05.jpg']
    },
    '天坛祈年殿': {
        'folder': '天坛祈年殿-明代-北京',
        'images': ['qinian_01.jpg', 'qinian_02.jpg', 'qinian_03.jpg', 'qinian_04.jpg', 'qinian_05.jpg']
    },
    '太和殿': {
        'folder': '太和殿-明清-北京故宫',
        'images': ['taihe_01.jpg', 'taihe_02.jpg', 'taihe_03.jpg', 'taihe_04.jpg', 'taihe_05.jpg']
    },
    '应县木塔': {
        'folder': '应县木塔-辽代-山西应县',
        'images': ['yingxian_01.jpg', 'yingxian_02.jpg', 'yingxian_03.jpg', 'yingxian_04.jpg', 'yingxian_05.jpg']
    },
    '拙政园': {
        'folder': '拙政园-明代-江苏苏州',
        'images': ['zhuozheng_01.jpg', 'zhuozheng_02.jpg', 'zhuozheng_03.jpg', 'zhuozheng_04.jpg', 'zhuozheng_05.jpg']
    },
    '苏州拙政园': {
        'folder': '拙政园-明代-江苏苏州',
        'images': ['zhuozheng_01.jpg', 'zhuozheng_02.jpg', 'zhuozheng_03.jpg', 'zhuozheng_04.jpg', 'zhuozheng_05.jpg']
    },
    '天坛': {
        'folder': '天坛祈年殿-明代-北京',
        'images': ['qinian_01.jpg', 'qinian_02.jpg', 'qinian_03.jpg', 'qinian_04.jpg', 'qinian_05.jpg']
    },
    '晋祠圣母殿': {
        'folder': '晋祠圣母殿-宋代-山西太原',
        'images': ['jinci_01.jpg', 'jinci_02.jpg', 'jinci_03.jpg', 'jinci_04.jpg', 'jinci_05.jpg']
    },
    '永乐宫': {
        'folder': '永乐宫-元代-山西芮城',
        'images': ['yongle_01.jpg', 'yongle_02.jpg', 'yongle_03.jpg', 'yongle_04.jpg', 'yongle_05.jpg']
    },
    '独乐寺观音阁': {
        'folder': '独乐寺观音阁-辽代-天津蓟县',
        'images': ['dule_01.jpg', 'dule_02.jpg', 'dule_03.jpg', 'dule_04.jpg', 'dule_05.jpg']
    },
}

def update_building_images():
    print("开始更新建筑图片路径...")
    updated_count = 0
    placeholder_image = "/img/placeholder.jpg"
    
    for building in AncientBuilding.objects.all():
        bname = building.bname
        
        if bname in BUILDING_IMAGE_MAPPING:
            mapping = BUILDING_IMAGE_MAPPING[bname]
            folder = mapping['folder']
            first_image = mapping['images'][0]
            
            image_path = f"/img/{folder}/{first_image}"
            
            building.image_url = image_path
            building.save()
            
            print(f"已更新: {bname} -> {image_path}")
            updated_count += 1
        else:
            building.image_url = placeholder_image
            building.save()
            print(f"使用占位图: {bname} -> {placeholder_image}")
            updated_count += 1
    
    print(f"\n更新完成! 共更新 {updated_count} 条记录")

if __name__ == '__main__':
    update_building_images()
