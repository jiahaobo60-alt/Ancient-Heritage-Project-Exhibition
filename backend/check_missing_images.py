import sqlite3
import os

# 连接数据库
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# 查询所有建筑
cursor.execute('''
    SELECT b.bid, b.bname, d.dname, b.image_url
    FROM architecture_building b
    JOIN architecture_dynasty d ON b.dynasty_id = d.did
    ORDER BY b.bid
''')

buildings = cursor.fetchall()

print("=" * 80)
print("Building Image Status Check")
print("=" * 80)
print(f"{'ID':<5} {'Name':<20} {'Dynasty':<15} {'Image Status':<30}")
print("-" * 80)

missing = []
has_images = []

for bid, bname, dynasty, image_url in buildings:
    # 检查图片文件是否存在
    has_image = bool(image_url and image_url.strip())
    if has_image:
        # 构建完整路径
        image_path = os.path.join('..', 'img', image_url.replace('img/', ''))
        if not os.path.exists(image_path):
            has_image = False
            print(f"{bid:<5} {bname:<20} {dynasty:<15} {'[X] File not found':<30}")
            missing.append((bid, bname, dynasty))
        else:
            print(f"{bid:<5} {bname:<20} {dynasty:<15} {'[OK] Has image':<30}")
            has_images.append((bid, bname, dynasty))
    else:
        print(f"{bid:<5} {bname:<20} {dynasty:<15} {'[X] No image URL':<30}")
        missing.append((bid, bname, dynasty))

print("=" * 80)
print(f"\nStatistics:")
print(f"[OK] Has images: {len(has_images)} buildings")
print(f"[X] Missing images: {len(missing)} buildings")

if missing:
    print(f"\nBuildings missing images:")
    for bid, bname, dynasty in missing:
        print(f"  - {bid}. {bname} ({dynasty})")

conn.close()
