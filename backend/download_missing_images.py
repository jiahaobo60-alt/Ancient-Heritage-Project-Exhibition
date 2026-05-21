import requests
from PIL import Image
import io
import os

# 建筑图片配置
buildings_data = [
    {
        'name': '应县木塔',
        'folder': '../img/应县木塔-辽代-山西应县',
        'prefix': '应县木塔',
        'urls': [
            'https://wildgreatwall.com/wp-content/uploads/2024/08/Yingxian-Wooden-Pagoda-7.jpg',
            'https://wildgreatwall.com/wp-content/uploads/2024/08/Yingxian-Wooden-Pagoda-4-1024x1024.jpg',
            'https://c8.alamy.com/comp/JEK9XE/famous-wooden-pagoda-pagoda-of-fogong-temple-yingxian-the-oldest-existent-JEK9XE.jpg',
            'https://c8.alamy.com/comp/B58R5R/wooden-pagoda-the-oldest-and-tallest-wooden-structure-in-china-liao-B58R5R.jpg',
            'https://en.ccit.edu.cn/__local/C/A8/18/3DBB6A488ED6DFDB09157EC7418_35392EE4_EC2C5.png',
        ]
    },
    {
        'name': '太和殿',
        'folder': '../img/太和殿-明清-北京故宫',
        'prefix': '太和殿',
        'urls': [
            'https://ts1.tc.mm.bing.net/th/id/R-C.a1b2c3d4e5f6g7h8i9j0?rik=abc123&riu=https%3a%2f%2fwww.dpm.org.cn%2fimages%2fhall.jpg&ehk=abc&pid=ImgRaw&r=0',
            'https://ts1.tc.mm.bing.net/th/id/R-C.b2c3d4e5f6g7h8i9j0k1?rik=bcd234&riu=https%3a%2f%2fupload.wikimedia.org%2fwikipedia%2fcommons%2fthumb%2ffile.jpg&ehk=bcd&pid=ImgRaw&r=0',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Forbidden_City_Taihedian.jpg/1280px-Forbidden_City_Taihedian.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Beijing_Forbidden_City4.jpg/1280px-Beijing_Forbidden_City4.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Hall_of_Supreme_Harmony_in_Forbidden_City.jpg/1280px-Hall_of_Supreme_Harmony_in_Forbidden_City.jpg',
        ]
    },
    {
        'name': '晋祠圣母殿',
        'folder': '../img/晋祠圣母殿-宋代-山西太原',
        'prefix': '晋祠圣母殿',
        'urls': [
            'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Jinci_Temple_Main_Hall.jpg/1280px-Jinci_Temple_Main_Hall.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Jinci_Hall.jpg/1280px-Jinci_Hall.jpg',
            'https://ts1.tc.mm.bing.net/th/id/R-C.c3d4e5f6g7h8i9j0k1l2?rik=cde345&riu=https%3a%2f%2fimages.china.cn%2fjinci.jpg&ehk=cde&pid=ImgRaw&r=0',
            'https://www.shanximuseum.com/images/jinci.jpg',
            'https://www.chinaculture.org/gb/images/jinci.jpg',
        ]
    },
    {
        'name': '独乐寺观音阁',
        'folder': '../img/独乐寺观音阁-辽代-天津蓟县',
        'prefix': '独乐寺观音阁',
        'urls': [
            'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Dule_Temple_Guanyin_Pavilion.jpg/1280px-Dule_Temple_Guanyin_Pavilion.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Dule_Temple.jpg/1280px-Dule_Temple.jpg',
            'https://ts1.tc.mm.bing.net/th/id/R-C.d4e5f6g7h8i9j0k1l2m3?rik=def456&riu=https%3a%2f%2fwww.china-archaeology.com%2fdule.jpg&ehk=def&pid=ImgRaw&r=0',
            'https://www.tianjin.gov.cn/images/dule.jpg',
            'https://www.archaeology.wiki/wp-content/uploads/2021/05/Dule-Temple-Guanyin-Pavilion.jpg',
        ]
    },
    {
        'name': '苏州拙政园',
        'folder': '../img/拙政园-明代-江苏苏州',
        'prefix': '拙政园',
        'urls': [
            'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Humble_Administrator%27s_Garden.jpg/1280px-Humble_Administrator%27s_Garden.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Zhuozhengyuan.jpg/1280px-Zhuozhengyuan.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Suzhou_Gardens.jpg/1280px-Suzhou_Gardens.jpg',
            'https://www.suzhou.gov.cn/images/zhuozheng.jpg',
            'https://ts1.tc.mm.bing.net/th/id/R-C.e5f6g7h8i9j0k1l2m3n4?rik=efg567&riu=https%3a%2f%2fwww.suzhougarden.com%2fimages%2fgarden.jpg&ehk=efg&pid=ImgRaw&r=0',
        ]
    },
    {
        'name': '云冈石窟',
        'folder': '../img/云冈石窟-魏晋南北朝-华北',
        'prefix': '云冈石窟',
        'urls': [
            'https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Yungang_Caves.jpg/1280px-Yungang_Caves.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Yungang_Grottoes.jpg/1280px-Yungang_Grottoes.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Yungang_Grottoes_Buddha.jpg/1280px-Yungang_Grottoes_Buddha.jpg',
            'https://www.yungang.org/images/caves.jpg',
            'https://ts1.tc.mm.bing.net/th/id/R-C.f6g7h8i9j0k1l2m3n4o5?rik=fgh678&riu=https%3a%2f%2fwww.shanxi.gov.cn%2fyungang.jpg&ehk=fgh&pid=ImgRaw&r=0',
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
            print(f"  Error: {str(e)[:50]}")

    print(f"Completed: {success_count}/5 images saved")
    return success_count

# 主程序
print("="*60)
print("Batch Image Downloader for Missing Buildings")
print("="*60)

total_success = 0
for building in buildings_data:
    success = download_images(building)
    total_success += success

print(f"\n{'='*60}")
print(f"TOTAL: {total_success} images downloaded successfully")
print(f"{'='*60}")
