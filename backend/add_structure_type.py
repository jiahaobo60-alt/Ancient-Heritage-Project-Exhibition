#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
添加结构类型
"""

import os
import django

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel.settings')
django.setup()

from api.models_architecture import ArchStructureType

# 添加石窟结构类型
struct_type, created = ArchStructureType.objects.get_or_create(tname='石窟')
if created:
    print('添加石窟结构类型成功')
else:
    print('石窟结构类型已存在')

# 查看所有结构类型
print('所有结构类型:')
for t in ArchStructureType.objects.all():
    print(f'{t.tid}: {t.tname}')
