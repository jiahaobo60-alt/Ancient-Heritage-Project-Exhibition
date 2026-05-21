import requests
from PIL import Image
import io
import os

# 需要下载图片的建筑
buildings_data = [
    {
        'name': '云冈石窟',
        'folder': '../img/云冈石窟-魏晋南北朝-华北',
        'prefix': '云冈石窟',
        'urls': [
            'https://cdn.britannica.com/28/123628-050-468B6D16/caves-Yungang-Datong-Shanxi-China.jpg',
            'https://smarthistory.org/wp-content/uploads/2020/11/yungang-grottoes-2-scaled.jpg',
            'https://smarthistory.org/wp-content/uploads/2020/11/Yungang-Cave-20_WANG-Xiaoshu.jpeg',
            'https://www.chinatoptrip.com/wp-content/uploads/2018/11/yungang-grottoes-datong-shanxi.jpg',
            'https://images.chinahighlights.com/allpicture/12/f11522514cca40879e49a612_cut_750x400_66.jpg',
        ]
    },
    {
        'name': '客家土楼',
        'folder': '../img/客家土楼-明代-华南',
        'prefix': '客家土楼',
        'urls': [
            'https://cdn.britannica.com/65/180265-050-7D0C8B7A/Fujian-tulou-fujian-province-China.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Fujian_Tulou_Earth_Buildings.jpg/1280px-Fujian_Tulou_Earth_Buildings.jpg',
            'https://www.chinadiscovery.com/images/tulou.jpg',
            'https://images.chinahighlights.com/allpicture/2020/08/c547e6e9f7d94e1d981d1e2_cut_750x400_66.jpg',
            'https://www.travelchinaguide.com/images/tulou.jpg',
        ]
    },
    {
        'name': '敦煌莫高窟',
        'folder': '../img/敦煌莫高窟-魏晋南北朝-西北',
        'prefix': '敦煌莫高窟',
        'urls': [
            'https://cdn.britannica.com/42/176842-050-A2D1D393/Mogao-Caves-Dunhuang-Gansu-China.jpg',
            'https://images.chinahighlights.com/allpicture/2013/11/c447f7e1b47b4c22b9aa1f8_cut_750x400_66.jpg',
            'https://www.travelchinaguide.com/images/mogao-caves.jpg',
            'https://www.chinadiscovery.com/images/mogao-caves.jpg',
            'https://www.silkroads.org.cn/images/mogao.jpg',
        ]
    },
    {
        'name': '秦始皇陵',
        'folder': '../img/秦始皇陵-汉代-西北',
        'prefix': '秦始皇陵',
        'urls': [
            'https://cdn.britannica.com/48/180848-050-E346C3BC/Terracotta-Army-Xian-Shaanxi-China.jpg',
            'https://images.chinahighlights.com/allpicture/2012/01/c447f7e1b47b4c22b9aa1f8_cut_750x400_66.jpg',
            'https://www.travelchinaguide.com/images/terracotta-warriors.jpg',
            'https://www.chinadiscovery.com/images/terracotta-warriors.jpg',
            'https://www.xian-tourism.com/images/mausoleum.jpg',
        ]
    },
    {
        'name': '避暑山庄',
        'folder': '../img/避暑山庄-清代-华北',
        'prefix': '避暑山庄',
        'urls': [
            'https://cdn.britannica.com/58/180558-050-D9F0C6C8/Chengde-Imperial-Summer-Resort-Hebei-China.jpg',
            'https://images.chinahighlights.com/allpicture/2016/07/c447f7e1b47b4c22b9aa1f8_cut_750x400_66.jpg',
            'https://www.travelchinaguide.com/images/summer-resort.jpg',
            'https://www.chinadiscovery.com/images/summer-resort.jpg',
            'https://www.hebei-tourism.com/images/resort.jpg',
        ]
    },
    {
        'name': '颐和园',
        'folder': '../img/颐和园-清代-华北',
        'prefix': '颐和园',
        'urls': [
            'https://cdn.britannica.com/52/180852-050-F3E2F5E8/Summer-Palace-Beijing-China.jpg',
            'https://images.chinahighlights.com/allpicture/2014/05/c447f7e1b47b4c22b9aa1f8_cut_750x400_66.jpg',
            'https://www.travelchinaguide.com/images/summer-palace.jpg',
            'https://www.chinadiscovery.com/images/summer-palace.jpg',
            'https://www.beijing-tourism.com/images/palace.jpg',
        ]
    },
    {
        'name': '黄鹤楼',
        'folder': '../img/黄鹤楼-明代-华中',
        'prefix': '黄鹤楼',
        'urls': [
            'https://cdn.britannica.com/59/176759-050-3B8F5A0E/Yellow-Crane-Tower-Wuhan-Hubei-China.jpg',
            'https://images.chinahighlights.com/allpicture/2015/03/c447f7e1b47b4c22b9aa1f8_cut_750x400_66.jpg',
            'https://www.travelchinaguide.com/images/yellow-crane-tower.jpg',
            'https://www.chinadiscovery.com/images/yellow-crane-tower.jpg',
            'https://www.wuhan-tourism.com/images/tower.jpg',
        ]
    },
    {
        'name': '滕王阁',
        'folder': '../img/滕王阁-明代-华东',
        'prefix': '滕王阁',
        'urls': [
            'https://cdn.britannica.com/60/176760-050-4C9F8B9D/Tengwang-Pavilion-Nanchang-Jiangxi-China.jpg',
            'https://images.chinahighlights.com/allpicture/2016/11/c447f7e1b47b4c22b9aa1f8_cut_750x400_66.jpg',
            'https://www.travelchinaguide.com/images/tengwang-pavilion.jpg',
            'https://www.chinadiscovery.com/images/tengwang-pavilion.jpg',
            'https://www.nanchang-tourism.com/images/pavilion.jpg',
        ]
    }
]

# 下载函数
def download_images(building):
    output_dir = building['folder']
    os.makedirs(output_dir, exist_ok=True)

    print(f"\n{'='*60}")
    print(f"Downloading images for: {building['name']}")
    print(f"{'='*60}")

    success_count = 0
    for idx, url in enumerate(building['urls'][:5], 1):
        try:
            print(f"[{idx}/5] Downloading...")
            response = requests.get(url, timeout=15)
            response.raise_for_status()

            # 使用Pillow打开并转换为JPG
            img = Image.open(io.BytesIO(response.content))
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # 保存为JPG
            output_path = os.path.join(output_dir, f"{building['prefix']}_{idx}.jpg")
            img.save(output_path, 'JPEG', quality=92)

            size_kb = os.path.getsize(output_path) / 1024
            print(f"  Saved: {output_path} ({size_kb:.1f} KB)")
            success_count += 1

        except Exception as e:
            print(f"  Error: {str(e)[:60]}")

    print(f"Completed: {success_count}/5 images saved")
    return success_count

# 主程序
print("="*60)
print("Final Batch Image Downloader")
print("="*60)

total_success = 0
for building in buildings_data:
    success = download_images(building)
    total_success += success

print(f"\n{'='*60}")
print(f"TOTAL: {total_success} images downloaded successfully")
print(f"{'='*60}")
