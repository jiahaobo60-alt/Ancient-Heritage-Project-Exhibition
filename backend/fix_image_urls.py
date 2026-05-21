import sqlite3
import os

# 连接数据库
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# 建筑文件夹和第一张图片的映射
folder_image_map = {
    '佛光寺东大殿-唐代-山西五台山': 'img/佛光寺东大殿-唐代-山西五台山/佛光寺东大殿_2.jpg',
    '应县木塔-辽代-山西应县': 'img/应县木塔-辽代-山西应县/应县木塔_1.jpg',
    '太和殿-明清-北京故宫': 'img/太和殿-明清-北京故宫/太和殿_1.jpg',
    '晋祠圣母殿-宋代-山西太原': 'img/晋祠圣母殿-宋代-山西太原/晋祠圣母殿_01.jpg',
    '独乐寺观音阁-辽代-天津蓟县': 'img/独乐寺观音阁-辽代-天津蓟县/独乐寺观音阁_01.jpg',
    '拙政园-明代-江苏苏州': 'img/拙政园-明代-江苏苏州/拙政园_01.jpg',
    '云冈石窟-魏晋南北朝-华北': 'img/云冈石窟-魏晋南北朝-华北/云冈石窟_01.jpg',
    '大明宫-唐代-陕西西安': 'img/大明宫-唐代-陕西西安/daming_01.jpg',
    '大雁塔-唐代-陕西西安': 'img/大雁塔-唐代-陕西西安/dayan_01.jpg',
    '永乐宫-元代-山西芮城': 'img/永乐宫-元代-山西芮城/yongle_01.jpg',
    '天坛祈年殿-明代-北京': 'img/天坛祈年殿-明代-北京/qinian_01.jpg',
    '岳阳楼-明代-华中': 'img/岳阳楼-明代-华中/岳阳楼_01.jpg',
    '颐和园-清代-华北': 'img/颐和园-清代-华北/颐和园_01.jpg',
    '避暑山庄-清代-华北': 'img/避暑山庄-清代-华北/避暑山庄_01.jpg',
    '长城-明代-华北': 'img/长城-明代-华北/长城_01.jpg',
    '客家土楼-明代-华南': 'img/客家土楼-明代-华南/客家土楼_01.jpg',
    '敦煌莫高窟-魏晋南北朝-西北': 'img/敦煌莫高窟-魏晋南北朝-西北/敦煌莫高窟_01.jpg',
    '秦始皇陵-汉代-西北': 'img/秦始皇陵-汉代-西北/秦始皇陵_01.jpg',
    '黄鹤楼-明代-华中': 'img/黄鹤楼-明代-华中/黄鹤楼_01.jpg',
    '滕王阁-明代-华东': 'img/滕王阁-明代-华东/滕王阁_01.jpg',
}

print("="*80)
print("Updating image URLs in database")
print("="*80)

# 查询所有建筑
cursor.execute('SELECT bid, bname FROM architecture_building ORDER BY bid')
buildings = cursor.fetchall()

updated = 0
for bid, bname in buildings:
    # 查找对应的文件夹
    matching_folder = None
    for folder, image_url in folder_image_map.items():
        if bname in folder:
            # 检查文件夹中的图片文件
            folder_path = f'../img/{folder}'
            if os.path.exists(folder_path):
                images = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
                if images:
                    # 获取第一张图片
                    first_image = images[0]
                    # 构建正确的URL
                    new_url = f'img/{folder}/{first_image}'

                    # 更新数据库
                    cursor.execute('UPDATE architecture_building SET image_url = ? WHERE bid = ?', (new_url, bid))
                    if cursor.rowcount > 0:
                        print(f"[{bid}] {bname} -> {new_url}")
                        updated += 1
                    break

conn.commit()
conn.close()

print("="*80)
print(f"Updated {updated} buildings with correct image URLs")
print("="*80)
