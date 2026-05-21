import json
import os
from django.conf import settings
from django.db import connection
import django

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel.settings')
django.setup()

from api.models import Dynasty, Province, Scenery, Category

def import_building_data():
    """导入建筑数据到数据库"""
    
    # 读取JSON数据
    json_file = os.path.join(settings.BASE_DIR.parent, 'frontend', 'data', 'buildings_static.json')
    
    with open(json_file, 'r', encoding='utf-8') as f:
        buildings = json.load(f)
    
    # 创建朝代映射
    dynasty_mapping = {
        '汉代': 1,
        '魏晋南北朝': 2,
        '唐代': 3,
        '宋代': 4,
        '辽金': 5,
        '元代': 6,
        '明代': 7,
        '清代': 8
    }
    
    # 创建地区映射
    province_mapping = {
        '华北': 1,
        '华东': 2,
        '华中': 3,
        '华南': 4,
        '西南': 5,
        '西北': 6,
        '东北': 7
    }
    
    # 创建分类映射
    category_mapping = {
        '殿宇': 1,
        '佛塔': 2,
        '楼阁': 3,
        '园林': 4,
        '民居': 5,
        '城墙': 6,
        '石窟': 7,
        '陵墓': 8
    }
    
    # 导入建筑数据
    imported_count = 0
    for building in buildings:
        try:
            # 检查是否已存在
            existing = Scenery.objects.filter(sid=building['bid']).first()
            if existing:
                print(f"建筑 {building['bname']} 已存在，跳过")
                continue
            
            # 获取朝代ID
            dynasty_id = dynasty_mapping.get(building['dynasty'], 3)
            
            # 获取地区ID
            province_id = province_mapping.get(building['region'], 1)
            
            # 获取分类ID
            category_name = building.get('structure_type', '殿宇')
            category_id = category_mapping.get(category_name, 1)
            
            # 创建建筑记录
            scenery = Scenery.objects.create(
                sid=building['bid'],
                sname=building['bname'],
                pid=province_id,
                did=dynasty_id,
                label=building['bid'],
                introduction=building.get('introduction', ''),
                category=category_id,
                city=building.get('address', ''),
                longitude=building.get('longitude'),
                latitude=building.get('latitude')
            )
            
            imported_count += 1
            print(f"成功导入建筑: {building['bname']} (ID: {building['bid']})")
            
        except Exception as e:
            print(f"导入建筑 {building.get('bname', '未知')} 时出错: {str(e)}")
    
    print(f"\n数据导入完成！共导入 {imported_count} 条建筑记录")

def import_dynasty_data():
    """导入朝代数据"""
    dynasties = [
        {'did': 1, 'dname': '汉代'},
        {'did': 2, 'dname': '魏晋南北朝'},
        {'did': 3, 'dname': '唐代'},
        {'did': 4, 'dname': '宋代'},
        {'did': 5, 'dname': '辽金'},
        {'did': 6, 'dname': '元代'},
        {'did': 7, 'dname': '明代'},
        {'did': 8, 'dname': '清代'}
    ]
    
    for dynasty in dynasties:
        Dynasty.objects.get_or_create(
            did=dynasty['did'],
            defaults={'dname': dynasty['dname']}
        )
    
    print("朝代数据导入完成！")

def import_province_data():
    """导入地区数据"""
    provinces = [
        {'pid': 1, 'pname': '华北'},
        {'pid': 2, 'pname': '华东'},
        {'pid': 3, 'pname': '华中'},
        {'pid': 4, 'pname': '华南'},
        {'pid': 5, 'pname': '西南'},
        {'pid': 6, 'pname': '西北'},
        {'pid': 7, 'pname': '东北'}
    ]
    
    for province in provinces:
        Province.objects.get_or_create(
            pid=province['pid'],
            defaults={'pname': province['pname']}
        )
    
    print("地区数据导入完成！")

def import_category_data():
    """导入分类数据"""
    categories = [
        {'cid': 1, 'cname': '殿宇'},
        {'cid': 2, 'cname': '佛塔'},
        {'cid': 3, 'cname': '楼阁'},
        {'cid': 4, 'cname': '园林'},
        {'cid': 5, 'cname': '民居'},
        {'cid': 6, 'cname': '城墙'},
        {'cid': 7, 'cname': '石窟'},
        {'cid': 8, 'cname': '陵墓'}
    ]
    
    for category in categories:
        Category.objects.get_or_create(
            cid=category['cid'],
            defaults={'cname': category['cname']}
        )
    
    print("分类数据导入完成！")

if __name__ == '__main__':
    print("开始导入数据...")
    
    # 导入基础数据
    import_dynasty_data()
    import_province_data()
    import_category_data()
    
    # 导入建筑数据
    import_building_data()
    
    print("所有数据导入完成！")
