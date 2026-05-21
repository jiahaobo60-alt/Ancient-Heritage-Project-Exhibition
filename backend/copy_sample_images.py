import sqlite3
import shutil
import os
import random

# 连接数据库
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# 查询需要图片的空文件夹
empty_folders = [
    ('客家土楼', '../img/客家土楼-明代-华南', '客家土楼'),
    ('敦煌莫高窟', '../img/敦煌莫高窟-魏晋南北朝-西北', '敦煌莫高窟'),
    ('秦始皇陵', '../img/秦始皇陵-汉代-西北', '秦始皇陵'),
    ('避暑山庄', '../img/避暑山庄-清代-华北', '避暑山庄'),
    ('颐和园', '../img/颐和园-清代-华北', '颐和园'),
    ('黄鹤楼', '../img/黄鹤楼-明代-华中', '黄鹤楼'),
    ('滕王阁', '../img/滕王阁-明代-华东', '滕王阁'),
]

# 从已有图片的文件夹中随机选择图片作为样本
source_images = []
source_folders = [
    '../img/佛光寺东大殿-唐代-山西五台山',
    '../img/应县木塔-辽代-山西应县',
    '../img/太和殿-明清-北京故宫',
    '../img/晋祠圣母殿-宋代-山西太原',
    '../img/独乐寺观音阁-辽代-天津蓟县',
    '../img/拙政园-明代-江苏苏州',
]

# 收集所有源图片
for folder in source_folders:
    if os.path.exists(folder):
        for file in os.listdir(folder):
            if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
                source_images.append(os.path.join(folder, file))

print("="*80)
print("Copying sample images to empty folders")
print("="*80)
print(f"Found {len(source_images)} source images")
print()

success_count = 0
for bname, folder, prefix in empty_folders:
    # 创建文件夹
    os.makedirs(folder, exist_ok=True)

    # 复制5张图片
    print(f"Copying to: {folder}")
    for idx in range(1, 6):
        try:
            # 随机选择一张源图片
            src_file = random.choice(source_images)
            dst_file = os.path.join(folder, f"{prefix}_{idx}.jpg")

            # 复制文件
            shutil.copy2(src_file, dst_file)

            # 检查文件大小
            size_kb = os.path.getsize(dst_file) / 1024
            print(f"  [{idx}] Copied ({size_kb:.1f} KB)")
            success_count += 1

        except Exception as e:
            print(f"  [{idx}] Error: {str(e)[:40]}")
    print()

print("="*80)
print(f"TOTAL: {success_count} images copied to empty folders")
print("="*80)

conn.close()
