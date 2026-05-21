import sqlite3
import shutil
import os

# 连接数据库
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# 查询需要更新的建筑（有图片URL但文件不存在）
cursor.execute('''
    SELECT b.bid, b.bname, b.image_url, d.dname
    FROM architecture_building b
    JOIN architecture_dynasty d ON b.dynasty_id = d.did
    WHERE image_url IS NOT NULL AND image_url != ''
    ORDER BY b.bid
''')

buildings = cursor.fetchall()

print("="*80)
print("Checking image files in database vs. actual folders")
print("="*80)

updates_made = []
for bid, bname, image_url, dynasty in buildings:
    # 构建图片路径
    if image_url.startswith('img/'):
        # 提取文件夹名
        folder_name = image_url.split('/')[1]
        image_filename = image_url.split('/')[-1]
        
        # 检查文件是否存在
        folder_path = f'../img/{folder_name}'
        image_path = f'{folder_path}/{image_filename}'
        
        if os.path.exists(image_path):
            # 查找文件夹中的所有图片
            if os.path.exists(folder_path):
                images = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
                if images:
                    first_image = images[0]
                    print(f"[{bid}] {bname} - Folder: {folder_name}, Images: {len(images)}")
                else:
                    print(f"[{bid}] {bname} - No images in folder")
            else:
                print(f"[{bid}] {bname} - Folder not found")
        else:
            print(f"[{bid}] {bname} - Image not found: {image_path}")

conn.close()
print("="*80)
