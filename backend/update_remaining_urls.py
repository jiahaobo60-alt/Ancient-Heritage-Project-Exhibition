import sqlite3
import os

# 连接数据库
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# 建筑ID和文件夹映射
building_folders = {
    15: ('云冈石窟', '云冈石窟-魏晋南北朝-华北'),
    16: ('客家土楼', '客家土楼-明代-华南'),
    17: ('敦煌莫高窟', '敦煌莫高窟-魏晋南北朝-西北'),
    18: ('秦始皇陵', '秦始皇陵-汉代-西北'),
    13: ('避暑山庄', '避暑山庄-清代-华北'),
    12: ('颐和园', '颐和园-清代-华北'),
    19: ('黄鹤楼', '黄鹤楼-明代-华中'),
    20: ('滕王阁', '滕王阁-明代-华东'),
}

print("="*80)
print("Updating remaining building image URLs in database")
print("="*80)

updated = 0
for bid, (bname, folder_name) in building_folders.items():
    folder_path = f'../img/{folder_name}'

    if os.path.exists(folder_path):
        # 获取第一张图片
        images = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
        if images:
            first_image = images[0]
            image_url = f'img/{folder_name}/{first_image}'

            # 更新数据库
            cursor.execute('UPDATE architecture_building SET image_url = ? WHERE bid = ?', (image_url, bid))
            if cursor.rowcount > 0:
                print(f"[{bid}] {bname} -> {image_url}")
                updated += 1
        else:
            print(f"[{bid}] {bname} - No images found in folder")
    else:
        print(f"[{bid}] {bname} - Folder not found")

conn.commit()
conn.close()

print("="*80)
print(f"Updated {updated} buildings with image URLs")
print("="*80)
