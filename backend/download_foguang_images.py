import requests
from PIL import Image
import io
import os

# 图片URL列表（从Bing搜索提取）
image_urls = [
    'https://www.archaeology.wiki/wp-content/uploads/2017/09/Foguang_temple_EN-1200x900.jpg',
    'https://ts1.tc.mm.bing.net/th/id/R-C.1c474f4351ae14aadae043166a1f2110?rik=qQJx37zdANw0JA&riu=http%3a%2f%2fwww.artmuseum.tsinghua.edu.cn%2fen%2fcpsj_english%2fzlxx%2fzlhg%2f201708%2fW020170815393662441458.jpg&ehk=SivOJTNyhfrX4dsOx5Nzu1pSiJyiJrZ%2fyMN0v8lGIOA%3d&risl=&pid=ImgRaw&r=0',
    'https://news.cgtn.com/news/2025-03-29/Foguang-Temple-s-Great-East-Hall-A-Tang-Dynasty-treasure-1C7XjM3YlGM/img/277c112a64cc4f8381759eb0b34d070c/277c112a64cc4f8381759eb0b34d070c-1280.png',
    'https://c8.alamy.com/comp/W863JW/a-view-of-foguang-temple-also-known-as-the-buddha-light-temple-on-mountain-wutai-in-foguang-village-doucun-town-wutai-county-yizhou-city-north-c-W863JW.jpg',
    'https://insideinside.org/wp-content/uploads/2023/11/Wutai_Foguang_Si_2013.08.28_11-00-05.jpg',
]

# 创建文件夹
output_dir = '../img/佛光寺东大殿-唐代-山西五台山'
os.makedirs(output_dir, exist_ok=True)

# 下载并转换图片
success_count = 0
for idx, url in enumerate(image_urls[:5], 1):  # 只下载5张
    try:
        print(f'Downloading image {idx}: {url}')
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        
        # 使用Pillow打开并转换为JPG
        img = Image.open(io.BytesIO(response.content))
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # 保存为JPG
        output_path = os.path.join(output_dir, f'佛光寺东大殿_{idx}.jpg')
        img.save(output_path, 'JPEG', quality=92)
        
        size_kb = os.path.getsize(output_path) / 1024
        print(f'  Saved: {output_path} ({size_kb:.1f} KB)')
        success_count += 1
        
    except Exception as e:
        print(f'  Error: {e}')

print(f'\nDownload completed: {success_count}/5 images saved to {output_dir}')
