#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""验证数据库更新结果"""

import sqlite3
import os

DB_PATH = "D:/26新比赛1/backend/db.sqlite3"

try:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("验证数据库更新结果")
    print("=" * 60)
    print()
    
    # 查询更新结果
    cursor.execute("SELECT bid, bname, image_url FROM architecture_building WHERE bid >= 11 AND bid <= 20 ORDER BY bid")
    results = cursor.fetchall()
    
    success_count = 0
    total_count = 0
    
    for row in results:
        bid, bname, image_url = row
        total_count += 1
        
        if image_url and image_url != "":
            status = "[OK]"
            success_count += 1
        else:
            status = "[EMPTY]"
        
        print(f"{status} ID: {bid} | 名称: {bname}")
        if image_url:
            print(f"     图片: {image_url}")
        print()
    
    print("=" * 60)
    print(f"总计: {total_count}个建筑")
    print(f"有图片: {success_count}个")
    print(f"无图片: {total_count - success_count}个")
    print("=" * 60)
    
    conn.close()
    
except Exception as e:
    print(f"[ERROR] {str(e)}")