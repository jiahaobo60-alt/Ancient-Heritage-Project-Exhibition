import sqlite3
import os

# 连接数据库
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# 查询所有建筑
cursor.execute('''
    SELECT b.bid, b.bname, b.image_url, d.dname
    FROM architecture_building b
    JOIN architecture_dynasty d ON b.dynasty_id = d.did
    ORDER BY b.bid
''')

buildings = cursor.fetchall()

print("="*80)
print("FINAL VERIFICATION - All Buildings Image Status")
print("="*80)

total = 0
with_images = 0
without_images = 0

for bid, bname, image_url, dynasty in buildings:
    total += 1

    # 检查图片
    has_image = False
    if image_url and image_url.startswith('img/'):
        image_path = f'../{image_url}'
        if os.path.exists(image_path):
            has_image = True

    if has_image:
        with_images += 1
        print(f"[{bid:2d}] {bname:15s} ({dynasty}) - OK")
    else:
        without_images += 1
        print(f"[{bid:2d}] {bname:15s} ({dynasty}) - MISSING")

print("="*80)
print(f"Summary:")
print(f"  Total buildings: {total}")
print(f"  With images: {with_images} ({with_images*100//total}%)")
print(f"  Without images: {without_images} ({without_images*100//total}%)")

if without_images == 0:
    print("\nSUCCESS! All buildings have images!")
else:
    print(f"\nWARNING: {without_images} buildings still missing images!")

conn.close()
