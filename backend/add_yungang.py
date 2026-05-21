#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
添加云冈石窟数据
"""

import os
import django

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel.settings')
django.setup()

from api.models_architecture import AncientBuilding, ArchDynasty, ArchRegion, ArchStructureType

def add_yungang():
    """添加云冈石窟"""
    # 检查是否已存在
    if AncientBuilding.objects.filter(bname='云冈石窟').exists():
        print('云冈石窟已存在')
        return
    
    # 获取关联对象
    dynasty, _ = ArchDynasty.objects.get_or_create(
        dname='魏晋南北朝',
        defaults={'period': '220年-589年'}
    )
    region, _ = ArchRegion.objects.get_or_create(rname='华北')
    struct_type, _ = ArchStructureType.objects.get_or_create(tname='石窟')
    
    # 创建建筑
    building = AncientBuilding.objects.create(
        bid=15,
        bname='云冈石窟',
        roof_type='',
        dougong_style='',
        longitude=113.208,
        latitude=40.186,
        address='山西省大同市云冈区',
        introduction='云冈石窟是北魏时期开凿的佛教石窟群，是中国四大石窟之一。',
        historical_value='云冈石窟是中国古代佛教艺术的瑰宝，体现了中西文化的融合。',
        architectural_features='现存主要洞窟45个，造像51000余尊，雕刻精美，气势雄伟。',
        image_url='img/index/lishi.jpg',
        dynasty=dynasty,
        region=region,
        structure_type=struct_type
    )
    
    print('创建建筑: 云冈石窟')

if __name__ == '__main__':
    add_yungang()
