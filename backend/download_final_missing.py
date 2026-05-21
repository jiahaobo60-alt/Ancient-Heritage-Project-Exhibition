import sqlite3
import os

# 连接数据库
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# 查询所有建筑及其图片URL
cursor.execute('''
    SELECT b.bid, b.bname, b.image_url, d.dname
    FROM architecture_building b
    JOIN architecture_dynasty d ON b.dynasty_id = d.did
    ORDER BY b.bid
''')

buildings = cursor.fetchall()

print("="*80)
print("Checking missing images in folders")
print("="*80)

missing_images = []
has_images = []

for bid, bname, image_url, dynasty in buildings:
    if image_url and image_url.startswith('img/'):
        # 提取文件夹路径
        parts = image_url.split('/')
        if len(parts) >= 2:
            folder_name = parts[1]
            folder_path = f'../img/{folder_name}'

            # 检查文件夹是否存在
            if os.path.exists(folder_path):
                # 检查图片是否存在
                image_path = f'../img/{image_url}'
                if os.path.exists(image_path):
                    # 统计文件夹中的图片数量
                    images = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
                    has_images.append((bid, bname, folder_name, len(images)))
                    print(f"[{bid}] {bname} - {len(images)} images")
                else:
                    missing_images.append((bid, bname, folder_name, dynasty))
                    print(f"[{bid}] {bname} - MISSING image file")
            else:
                missing_images.append((bid, bname, folder_name, dynasty))
                print(f"[{bid}] {bname} - MISSING folder")
    else:
        missing_images.append((bid, bname, 'N/A', dynasty))
        print(f"[{bid}] {bname} - NO image URL")

print("="*80)
print(f"Summary:")
print(f"  Has images: {len(has_images)}")
print(f"  Missing images: {len(missing_images)}")

if missing_images:
    print(f"\nMissing images details:")
    for bid, bname, folder, dynasty in missing_images:
        print(f"  {bid}. {bname} ({dynasty}) - Folder: {folder}")

conn.close()

# 输出需要下载的建筑列表（供后续使用）
if missing_images:
    print("\n\nBuildings needing image download:")
    for bid, bname, folder, dynasty in missing_images:
        print(f"- {bid}. {bname} ({dynasty})")
