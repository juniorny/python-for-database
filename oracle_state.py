import cx_Oracle

# 建立和数据库系统的连接
# db = cx_Oracle.connect('''zhong/123456@192.168.133.129:1522/orcl''')
# db = cx_Oracle.connect('''zhong/123456''')
# db = cx_Oracle.connect('''system/csg12345''')
# db = cx_Oracle.connect('''sys/change_on_install''', mode=cx_Oracle.SYSDBA)
db = cx_Oracle.connect('''sys/11ysc.Age@192.168.133.129:1522/orcl''', mode=cx_Oracle.SYSDBA)
print('数据库版本：', db.version)

cur = db.cursor()

# 不要加分号
sql = "select value from v$parameter where name ='processes'"
cur.execute(sql)
print("数据库允许的最大连接数：", cur.fetchone()[0])
for res in cur:
    print(res[0])

sql = "select count(username) from v$session"
cur.execute(sql)
for res in cur:
    print("当前会话数：{}".format(res[0]))

# sql = "select segment_name, round(bytes/1024/1024, 2) \
#         from user_segments \
#         where segment_type = 'TABLE' \
#         ORDER BY bytes DESC, blocks DESC"
# cur.execute(sql)
# for res in cur:
#     print("表名：{}, 大小：{}MB".format(res[0], res[1]))
#
# sql = "select * from tb_user"
# cur.execute(sql)
# for res in cur:
#     print(res)

# sql = "SELECT * FROM dba_tablespaces"
# cur.execute(sql)
# for res in cur:
#     print(res)

# 关闭连接，释放资源
cur.close()
# 提交更改
# db.commit()
db.close()
