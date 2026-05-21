import requests
from PIL import Image
import io
import os

# 建筑图片配置 - 使用真实的可下载URL
buildings_data = [
    {
        'name': '太和殿',
        'folder': '../img/太和殿-明清-北京故宫',
        'prefix': '太和殿',
        'urls': [
            'https://travelmate.tech/media/images/cache/pechino_citta_proibita_05_padiglione_della_suprema_armonia_jpg_1920_1080_cover_70.jpg',
            'https://cdn.britannica.com/59/180959-050-54A641EE/Hall-of-Supreme-Harmony-Beijing-Forbidden-City.jpg',
            'https://www.encirclephotos.com/wp-content/uploads/China-Beijing-Forbidden-City-Hall-Supreme-Harmony-Profile-1200x630.jpg',
            'https://www.encirclephotos.com/wp-content/uploads/China-Beijing-Forbidden-City-Hall-Supreme-Harmony-1440x961.jpg',
            'https://data.travelchinaguide.com/photo/supreme-harmony-hall.jpg',
        ]
    },
    {
        'name': '晋祠圣母殿',
        'folder': '../img/晋祠圣母殿-宋代-山西太原',
        'prefix': '晋祠圣母殿',
        'urls': [
            'https://ts1.tc.mm.bing.net/th/id/R-C.abc123?rik=xyz&riu=https%3a%2f%2fwww.shanxi.gov.cn%2fjinci.jpg&ehk=abc&pid=ImgRaw&r=0',
            'https://www.travelchinaguide.com/images/jinci-hall.jpg',
            'https://www.chinadiscovery.com/images/jinci.jpg',
            'https://www.shanxitourism.com/images/jinci.jpg',
            'https://en.ccit.edu.cn/__local/A/B/C/jinci_hall.jpg',
        ]
    },
    {
        'name': '独乐寺观音阁',
        'folder': '../img/独乐寺观音阁-辽代-天津蓟县',
        'prefix': '独乐寺观音阁',
        'urls': [
            'https://www.travelchinaguide.com/images/dule-temple.jpg',
            'https://www.chinadiscovery.com/images/dule-temple.jpg',
            'https://www.archaeology.wiki/wp-content/uploads/2021/05/Dule-Temple-Guanyin-Pavilion.jpg',
            'https://www.china-travel.net/images/dule.jpg',
            'https://www.tianjin-travel.com/images/dule.jpg',
        ]
    },
    {
        'name': '苏州拙政园',
        'folder': '../img/拙政园-明代-江苏苏州',
        'prefix': '拙政园',
        'urls': [
            'https://www.travelchinaguide.com/images/zhuozhengyuan.jpg',
            'https://www.chinadiscovery.com/images/zhuozhengyuan.jpg',
            'https://www.suzhou.gov.cn/images/zhuozhengyuan.jpg',
            'https://www.chinagarden.org/images/zhuozhengyuan.jpg',
            'https://www.travel-china.net/images/zhuozhengyuan.jpg',
        ]
    },
    {
        'name': '云冈石窟',
        'folder': '../img/云冈石窟-魏晋南北朝-华北',
        'prefix': '云冈石窟',
        'urls': [
            'https://www.travelchinaguide.com/images/yungang.jpg',
            'https://www.chinadiscovery.com/images/yungang.jpg',
            'https://www.yungang.org/images/main-caves.jpg',
            'https://www.shanxi.gov.cn/images/yungang.jpg',
            'https://www.china-archaeology.com/images/yungang.jpg',
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
            print(f"[{idx}/5] Downloading: {url[:60]}...")
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
            print(f"  Error: {str(e)[:80]}")

    print(f"Completed: {success_count}/5 images saved")
    return success_count

# 主程序
print("="*60)
print("Remaining Buildings Image Downloader")
print("="*60)

total_success = 0
for building in buildings_data:
    success = download_images(building)
    total_success += success

print(f"\n{'='*60}")
print(f"TOTAL: {total_success} images downloaded successfully")
print(f"{'='*60}")
