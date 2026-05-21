#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查当前建筑数据
"""

import os
import django

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel.settings')
django.setup()

from api.models_architecture import AncientBuilding, ArchDynasty, ArchRegion, ArchStructureType

print("=== 数据统计 ===")
print(f"建筑数量: {AncientBuilding.objects.count()}")
print(f"朝代数量: {ArchDynasty.objects.count()}")
print(f"地域数量: {ArchRegion.objects.count()}")
print(f"结构类型数量: {ArchStructureType.objects.count()}")

print("\n=== 建筑列表 ===")
for b in AncientBuilding.objects.all():
    dynasty = b.dynasty.dname if b.dynasty else "未知"
    region = b.region.rname if b.region else "未知"
    struct_type = b.structure_type.tname if b.structure_type else "未知"
    print(f"{b.bid}: {b.bname} - {dynasty} - {region} - {struct_type}")

print("\n=== 朝代列表 ===")
for d in ArchDynasty.objects.all():
    print(f"{d.did}: {d.dname} - {d.period}")

print("\n=== 地域列表 ===")
for r in ArchRegion.objects.all():
    print(f"{r.rid}: {r.rname}")

print("\n=== 结构类型列表 ===")
for t in ArchStructureType.objects.all():
    print(f"{t.tid}: {t.tname}")
