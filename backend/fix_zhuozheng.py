import sqlite3
import shutil
import os

# 连接数据库
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# 拙政园文件夹
folder_path = '../img/拙政园-明代-江苏苏州'

# 获取文件夹中的图片
if os.path.exists(folder_path):
    images = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
    if images:
        # 更新数据库为第一张图片
        first_image = images[0]
        image_url = f'img/拙政园-明代-江苏苏州/{first_image}'

        cursor.execute('UPDATE architecture_building SET image_url = ? WHERE bid = 6', (image_url,))
        conn.commit()

        print(f"Updated 拙政园 image_url to: {image_url}")
        print(f"Total images in folder: {len(images)}")
    else:
        print("No images found in folder")
else:
    print("Folder not found")

conn.close()
