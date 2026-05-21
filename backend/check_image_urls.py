import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel.settings')

import django
django.setup()

from api import models_architecture as m

print("=" * 60)
print("AncientBuilding 图片 URL 检查结果")
print("=" * 60)

for b in m.AncientBuilding.objects.select_related('dynasty','region','structure_type').all():
    img = b.image_url or "(空)"
    print(f"[{b.bid}] {b.bname} | {b.dynasty.dname} | {b.region.rname} | img={img}")

print("=" * 60)
print(f"共 {m.AncientBuilding.objects.count()} 条记录")
