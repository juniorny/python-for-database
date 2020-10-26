# show table status \G

import pymysql

host = 'localhost'
user = 'root'
password = 'root'
port = 3306

db = pymysql.connect(host=host, user=user, password=password, port=port, database='mysql')
print("数据库版本：", db.get_server_info())

cur = db.cursor()


# 查看当前连接数
def show_threads_connected(cursor):
    cursor.execute("show status like 'Threads_connected';")
    # for res in cur.fetchall():
    #     print(res)
    res = cur.fetchone()
    print("当前连接数：", res[1])
    return res[1]


# 查看最大连接数
def show_max_connections(cursor):
    cursor.execute("show variables like 'max_connections';")
    # for res in cur.fetchall():
    #     print(res)
    res = cur.fetchone()
    print("最大连接数：", res[1])
    return res[1]


# 查看试图连接MySQL服务器的次数，成功和失败的连接都算在内
def show_connections(cursor):
    cursor.execute("show status like 'Connections';")
    # for res in cur.fetchall():
    #     print(res)
    res = cur.fetchone()
    print("试图连接MySQL服务器的次数：", res[1])
    return res[1]


# 查询数据库表数目
def show_table_num(cursor, db_name):
    sql = "SELECT COUNT(*) TABLES, table_schema FROM information_schema.TABLES \
            WHERE table_schema = %s;"
    cursor.execute(sql, db_name)
    # for res in cur.fetchall():
    #     print(res)
    res = cur.fetchone()
    print("{}表数目：{}".format(res[1], res[0]))
    return res[0]


# 查询数据库所有表名称
def show_table_name(cursor, db_name):
    sql = "select table_name from information_schema.tables where table_schema=%s;"
    cursor.execute(sql, db_name)
    print('{}表名称列表：'.format(db_name))
    for res in cur.fetchall():
        print(res[0])


# 查询表行数
def show_table_count(cursor, table_name):
    sql = "SELECT COUNT(*) FROM {0};".format(table_name)
    cursor.execute(sql)
    # for res in cur.fetchall():
    #     print(res)
    res = cur.fetchone()
    print("{}行数：{}".format(table_name, res[0]))
    return res[0]


# 查询所有数据库容量大小
def show_db_size_all(cursor):
    sql = "select \
            table_schema, \
            sum(table_rows), \
            sum(truncate(data_length/1024/1024, 2)), \
            sum(truncate(index_length/1024/1024, 2)) \
            from information_schema.tables \
            group by table_schema \
            order by sum(data_length) desc, sum(index_length) desc;"
    cursor.execute(sql)
    for res in cur.fetchall():
        print("数据库：{}, 记录数：{}, 数据容量：{}MB, 索引容量：{}MB".format(res[0], res[1], res[2], res[3]))


# 查询指定数据库容量大小
def show_db_size(cursor, db_name):
    sql = "select \
            table_schema, \
            sum(table_rows), \
            sum(truncate(data_length/1024/1024, 2)), \
            sum(truncate(index_length/1024/1024, 2)) \
            from information_schema.tables \
            where table_schema=%s;"
    cursor.execute(sql, db_name)
    for res in cur.fetchall():
        print("数据库：{}, 记录数：{}, 数据容量：{}MB, 索引容量：{}MB".format(res[0], res[1], res[2], res[3]))


# 查询指定数据库所有表容量大小
def show_table_size_all(cursor, db_name):
    sql = "select \
            table_schema, \
            table_name, \
            table_rows, \
            truncate(data_length/1024/1024, 2), \
            truncate(index_length/1024/1024, 2) \
            from information_schema.tables \
            where table_schema=%s \
            order by data_length desc, index_length desc;"
    cursor.execute(sql, db_name)
    for res in cur.fetchall():
        print("数据库：{}, 表名：{}, 记录数：{}, 数据容量：{}MB, 索引容量：{}MB".format(res[0], res[1], res[2], res[3], res[4]))


# 查询指定数据库指定表容量大小
def show_table_size(cursor, db_name, tb_name):
    sql = "select \
            table_schema, \
            table_name, \
            table_rows, \
            truncate(data_length/1024/1024, 2), \
            truncate(index_length/1024/1024, 2) \
            from information_schema.tables \
            where table_schema=%s and table_name=%s\
            order by data_length desc, index_length desc;"
    cursor.execute(sql, (db_name, tb_name))
    for res in cur.fetchall():
        print("数据库：{}, 表名：{}, 记录数：{}, 数据容量：{}MB, 索引容量：{}MB".format(res[0], res[1], res[2], res[3], res[4]))


print("-"*40)
show_threads_connected(cur)
print("-"*40)
show_max_connections(cur)
print("-"*40)
show_connections(cur)
print("-"*40)
show_table_num(cur, 'mysql')
print("-"*40)
show_table_name(cur, 'mysql')
print("-"*40)
show_table_count(cur, 'user')
print("-"*40)
show_db_size_all(cur)
print("-"*40)
show_db_size(cur, 'mysql')
print("-"*40)
show_table_size_all(cur, 'mysql')
print("-"*40)
show_table_size(cur, 'mysql', 'user')

cur.close()
# db.commit()
db.close()
