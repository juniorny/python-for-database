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
# sql = "select username from v$session"
cur.execute(sql)
# for res in cur:
#     print(res)
for res in cur:
    print("当前会话数：{}".format(res[0]))

# 查看表的大小
# sql = "select segment_name, round(bytes/1024/1024, 2) \
#         from user_segments \
#         where segment_type = 'TABLE' \
#         ORDER BY bytes DESC"
# cur.execute(sql)
# for res in cur:
#     print("表名：{}, 大小：{}MB".format(res[0], res[1]))

# 查看表空间物理名称及大小
# sql = "SELECT tablespace_name, \
#         file_id, \
#         file_name, \
#         round(bytes / (1024 * 1024), 0) \
#         FROM dba_data_files \
#         ORDER BY tablespace_name"

# 查询Oracle正在执行的sql语句及执行该语句的用户
# sql = "select a.username, a.sid, b.SQL_TEXT, b.SQL_FULLTEXT \
#         from v$session a, v$sqlarea b \
#         where a.sql_address = b.address"

# 查看数据库实例状态
# sql = "SELECT instance_name, host_name, startup_time, status, database_status \
#         FROM v$instance"

# 查看数据库信息
# sql = "SELECT NAME, log_mode, open_mode \
#         FROM v$database"

# 查看控制文件的状态
# sql = "SELECT status, NAME \
#         FROM v$controlfile"

# 查看表空间的状态
# sql = "SELECT tablespace_name, status FROM dba_tablespaces"

# 查看数据文件的状态
# sql = "SELECT NAME, status \
#         FROM v$datafile"

# 查看无效对象
# sql = "SELECT owner, object_name, object_type, status \
#         FROM dba_objects \
#         WHERE status != 'VALID' \
#         AND owner != 'SYS' \
#         AND owner != 'SYSTEM'"

# 资源检查
# sql = "SELECT resource_name, initial_allocation, CURRENT_UTILIZATION, max_utilization, limit_value \
#         FROM v$resource_limit"

# 数据库连接状态
# sql = "SELECT sid, serial#, username, program, machine, status \
#         FROM v$session"

# 检查表空间使用情况
# sql = '''SELECT f.tablespace_name, a.total "total (M)", f.free "free (M)", \
#         round((f.free / a.total) * 100, 2) "% Free" \
#         FROM (SELECT tablespace_name, SUM(bytes / (1024 * 1024)) total \
#         FROM dba_data_files \
#         GROUP BY tablespace_name) a, \
#         (SELECT tablespace_name, round(SUM(bytes / (1024 * 1024))) free \
#         FROM dba_free_space \
#         GROUP BY tablespace_name) f \
#         WHERE a.tablespace_name = f.tablespace_name(+) \
#         ORDER BY "% Free"'''

# 表空间是否具有自动扩展空间
# sql = "SELECT t.tablespace_name, d.file_name, d.autoextensible, d.bytes, d.maxbytes, d.status \
#         FROM dba_tablespaces t, dba_data_files d \
#         WHERE t. tablespace_name = d. tablespace_name \
#         ORDER BY tablespace_name, file_name"

# 检查数据库的等待事件
# sql = "SELECT sid, event, p1, p2, p3, wait_time, seconds_in_wait \
#         FROM v$session_wait \
#         WHERE event NOT LIKE 'SQL%' \
#         AND event NOT LIKE 'rdbms%'"

# 查找前十条性能差的sql
sql = "SELECT * \
        FROM (SELECT parsing_user_id executions, sorts, command_type, disk_reads, sql_text \
        FROM v$sqlarea \
        ORDER BY disk_reads DESC) \
        WHERE rownum < 10"

cur.execute(sql)
for res in cur:
    print(res)

# 查询zhong用户下的表tb_user
# sql = "select * from tb_user"
# cur.execute(sql)
# for res in cur:
#     print(res)

# 关闭连接，释放资源
cur.close()
# 提交更改
# db.commit()
db.close()
