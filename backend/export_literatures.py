import sqlite3, json

LIT_TYPE_MAP = {
    'ancient': '古代典籍',
    'textbook': '学术专著',
    'research': '研究文献',
    'atlas': '图谱图集',
    'journal': '期刊论文',
    'other': '其他'
}

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
c.execute("""
    SELECT lid, lname, author, dynasty, publish_year, literature_type,
           summary, key_points, contributions, publisher, edition, pages, cover_image, pdf_url
    FROM architecture_literature ORDER BY lid
""")
lits = []
for row in c.fetchall():
    lid, lname, author, dynasty, yr, ltype, summary, kp, contrib, pub, edition, pages, cover, pdf = row
    lits.append({
        'lid': lid,
        'lname': lname or '',
        'author': author or '',
        'dynasty': dynasty or '',
        'publish_year': yr,
        'literature_type': ltype or '',
        'literature_type_display': LIT_TYPE_MAP.get(ltype, ltype or ''),
        'summary': summary or '',
        'key_points': kp or '',
        'contributions': contrib or '',
        'publisher': pub or '',
        'edition': edition or '',
        'pages': pages,
        'cover_image': cover or '',
        'pdf_url': pdf or ''
    })
conn.close()

with open('../frontend/data/literatures_static.json', 'w', encoding='utf-8') as f:
    json.dump({'results': lits}, f, ensure_ascii=False, indent=2)
print('Done:', len(lits), 'literatures')
