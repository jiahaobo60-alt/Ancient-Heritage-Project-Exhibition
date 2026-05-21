#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""更新古建筑图片URL"""

import sqlite3
import os

# 连接到数据库
db_path = 'db.sqlite3'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 更新现有建筑的图片URL
updates = [
    (1, 'img/佛光寺东大殿-唐代-山西五台山/佛光寺东大殿_01.jpg'),
    (2, 'img/应县木塔-辽代-山西应县/应县木塔_01.jpg'),
    (3, 'img/太和殿-明清-北京故宫/太和殿_01.jpg'),
    (4, 'img/晋祠圣母殿-宋代-山西太原/晋祠圣母殿_01.jpg'),
    (5, 'img/独乐寺观音阁-辽代-天津蓟县/独乐寺观音阁_01.jpg'),
    (6, 'img/拙政园-明代-江苏苏州/拙政园_01.jpg'),
]

updated = 0
for bid, image_url in updates:
    cursor.execute('UPDATE architecture_building SET image_url = ? WHERE bid = ?', (image_url, bid))
    if cursor.rowcount > 0:
        updated += 1
        print(f'Updated building {bid}: {image_url}')
    else:
        print(f'Building {bid} not found')

# 提交更改
conn.commit()
conn.close()

print(f'\nDone! Updated {updated} buildings')
