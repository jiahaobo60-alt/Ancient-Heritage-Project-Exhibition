# -*- coding: utf-8 -*-
"""导出数据库数据到前端JSON文件"""
import sqlite3, json, os

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db.sqlite3')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'frontend', 'data')

def go():
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    cur = c.cursor()

    # 导出建筑
    cur.execute("SELECT b.*, d.dname as dynasty_name, r.rname as region_name, s.tname as type_name FROM architecture_building b LEFT JOIN architecture_dynasty d ON b.dynasty_id=d.did LEFT JOIN architecture_region r ON b.region_id=r.rid LEFT JOIN architecture_structure_type s ON b.structure_type_id=s.tid")
    buildings = []
    for row in cur.fetchall():
        buildings.append({
            "bid": row["bid"],
            "bname": row["bname"],
            "dynasty": row["dynasty_name"] if row["dynasty_name"] else "",
            "region": row["region_name"] if row["region_name"] else "",
            "structure_type": row["type_name"] if row["type_name"] else "",
            "roof_type": row["roof_type"] if row["roof_type"] else "",
            "dougong_style": row["dougong_style"] if row["dougong_style"] else "",
            "longitude": row["longitude"],
            "latitude": row["latitude"],
            "address": row["address"] if row["address"] else "",
            "introduction": row["introduction"] if row["introduction"] else "",
            "historical_value": row["historical_value"] if row["historical_value"] else "",
            "architectural_features": row["architectural_features"] if row["architectural_features"] else "",
            "liang_sicheng_note": row["liang_sicheng_note"] if row["liang_sicheng_note"] else "",
            "image_url": row["image_url"] if row["image_url"] else "",
        })
    out_path = os.path.join(OUT, 'buildings_static.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(buildings, f, ensure_ascii=False, indent=2)
    print("建筑导出: %d条 -> %s" % (len(buildings), out_path))

    # 导出文献
    cur.execute("SELECT * FROM architecture_literature")
    literatures = []
    for row in cur.fetchall():
        literatures.append({
            "lid": row["lid"],
            "lname": row["lname"],
            "author": row["author"],
            "dynasty": row["dynasty"],
            "publish_year": row["publish_year"],
            "literature_type": row["literature_type"],
            "summary": row["summary"],
            "key_points": row["key_points"],
            "contributions": row["contributions"],
            "publisher": row["publisher"],
            "edition": row["edition"] if row["edition"] else "",
            "pages": row["pages"] if row["pages"] else 0,
            "cover_image": row["cover_image"] if row["cover_image"] else "",
        })
    out_path = os.path.join(OUT, 'literatures_static.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(literatures, f, ensure_ascii=False, indent=2)
    print("文献导出: %d条 -> %s" % (len(literatures), out_path))

    # 导出元素
    cur.execute("SELECT * FROM architecture_element")
    elements = []
    for row in cur.fetchall():
        elements.append({
            "eid": row["eid"],
            "ename": row["ename"],
            "category": row["category"],
            "original_text": row["original_text"],
            "explanation": row["explanation"],
            "structure_description": row["structure_description"],
            "function_description": row["function_description"],
            "evolution": row["evolution"],
            "image_url": row["image_url"] if row["image_url"] else "",
        })
    out_path = os.path.join(OUT, 'elements_static.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(elements, f, ensure_ascii=False, indent=2)
    print("元素导出: %d条 -> %s" % (len(elements), out_path))

    # 导出朝代
    cur.execute("SELECT * FROM architecture_dynasty")
    dynasties = []
    for row in cur.fetchall():
        dynasties.append({
            "dynasty_id": row["did"],
            "dynasty_name": row["dname"],
        })
    out_path = os.path.join(OUT, 'dynasties_static.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(dynasties, f, ensure_ascii=False, indent=2)
    print("朝代导出: %d条 -> %s" % (len(dynasties), out_path))

    # 导出地区
    cur.execute("SELECT * FROM architecture_region")
    regions = []
    for row in cur.fetchall():
        regions.append({
            "region_id": row["rid"],
            "region_name": row["rname"],
        })
    out_path = os.path.join(OUT, 'regions_static.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(regions, f, ensure_ascii=False, indent=2)
    print("地区导出: %d条 -> %s" % (len(regions), out_path))

    # 导出结构类型
    cur.execute("SELECT * FROM architecture_structure_type")
    types = []
    for row in cur.fetchall():
        types.append({
            "structure_type_id": row["tid"],
            "type_name": row["tname"],
        })
    out_path = os.path.join(OUT, 'structure_types_static.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(types, f, ensure_ascii=False, indent=2)
    print("结构类型导出: %d条 -> %s" % (len(types), out_path))

    c.close()
    print("\n===== 全部导出完成 =====")

if __name__ == '__main__':
    go()
