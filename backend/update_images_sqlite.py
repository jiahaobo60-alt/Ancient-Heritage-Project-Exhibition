#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用SQLite3直接更新古建筑图片URL
不需要Django环境
"""

import os
import sqlite3

# 数据库路径
DB_PATH = "D:/26新比赛1/backend/db.sqlite3"

# 需要更新的古建筑图片映射
BUILDING_IMAGES = {
    11: "img/岳阳楼-明代-华中/岳阳楼_01.jpg",
    12: "img/颐和园-清代-华北/颐和园_01.jpg",
    13: "img/避暑山庄-清代-华北/避暑山庄_01.jpg",
    14: "img/长城-明代-华北/长城_01.jpg",
    # 15: 云冈石窟 - 暂时跳过
    16: "img/客家土楼-明代-华南/客家土楼_01.jpg",
    17: "img/敦煌莫高窟-魏晋南北朝-西北/敦煌莫高窟_01.jpg",
    18: "img/秦始皇陵-汉代-西北/秦始皇陵_01.jpg",
    19: "img/黄鹤楼-明代-华中/黄鹤楼_01.jpg",
    20: "img/滕王阁-明代-华东/滕王阁_01.jpg"
}

def update_database():
    """更新数据库"""
    print("=" * 60)
    print("更新古建筑图片URL到数据库")
    print(f"数据库: {DB_PATH}")
    print("=" * 60)
    print()
    
    try:
        # 连接数据库
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        success_count = 0
        
        for bid, image_path in BUILDING_IMAGES.items():
            # 检查图片文件是否存在
            full_path = os.path.join("D:/26新比赛1", image_path)
            if os.path.exists(full_path):
                # 更新数据库
                cursor.execute(
                    "UPDATE architecture_building SET image_url = ? WHERE bid = ?",
                    (image_path, bid)
                )
                
                if cursor.rowcount > 0:
                    print(f"[OK] 更新成功 - ID: {bid}")
                    print(f"     图片路径: {image_path}")
                    success_count += 1
                else:
                    print(f"[WARN] 未找到建筑ID: {bid}")
            else:
                print(f"[WARN] 图片文件不存在: {full_path}")
            
            print()
        
        # 提交更改
        conn.commit()
        
        print("=" * 60)
        print(f"更新完成！成功更新: {success_count}/{len(BUILDING_IMAGES)}")
        print("=" * 60)
        
        # 查询验证
        print()
        print("验证更新结果:")
        cursor.execute("SELECT bid, bname, image_url FROM architecture_building WHERE bid >= 11 AND bid <= 20")
        results = cursor.fetchall()
        
        for row in results:
            bid, bname, image_url = row
            status = "✓" if image_url and image_url != "" else "✗"
            print(f"{status} ID: {bid} | 名称: {bname}")
            if image_url:
                print(f"  图片: {image_url}")
        
        conn.close()
        
    except Exception as e:
        print(f"[ERROR] 数据库操作失败: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    # 检查数据库文件是否存在
    if not os.path.exists(DB_PATH):
        print(f"[ERROR] 数据库文件不存在: {DB_PATH}")
        print("请确保数据库文件路径正确")
    else:
        update_database()
