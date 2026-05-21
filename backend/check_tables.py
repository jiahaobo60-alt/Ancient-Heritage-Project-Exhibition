import sqlite3, json
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [r[0] for r in c.fetchall()]
print('all tables:', tables)
# 检查文献表
if 'architecture_literature' in tables:
    c.execute('SELECT * FROM architecture_literature LIMIT 3')
    rows = c.fetchall()
    print('sample literatures:', rows)
else:
    print('literature table NOT found')
conn.close()
