import pymysql

host = 'localhost'
user = 'root'
password = 'root'
port = 3306

mysql = pymysql.connect(host=host, user=user, password=password, port=port, database='pythonDB')

print(mysql.get_server_info())

cursor = mysql.cursor()
# 创建数据库: pythonDB
# cursor.execute('CREATE DATABASE IF NOT EXISTS pythonDB DEFAULT CHARSET utf8 COLLATE utf8_general_ci;')

# 创建表: user
cursor.execute('drop table if exists user')
sql = """CREATE TABLE IF NOT EXISTS `user` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `name` varchar(255) NOT NULL,
        `age` int(11) NOT NULL,
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""

cursor.execute(sql)

insert = cursor.execute("insert into user values(1,'tom',18)")
print('添加语句受影响的行数：', insert)

# 另一种插入数据的方式，通过字符串传入值
sql = "insert into user values(%s, %s, %s)"
cursor.execute(sql, (3, 'kongsh', 20))

sql = "insert into user values(%s, %s, %s)"
insert = cursor.executemany(sql, [(4, 'wen', 20), (5, 'bob', 10), (6, 'test', 30)])
print('批量插入返回受影响的行数：', insert)

cursor.execute('select * from user;')
# while 1:
#     res = cursor.fetchone()
#     if res is None:
#         break
#     print(res)

# resTuple = cursor.fetchmany(3)
# print(type(resTuple))
# for res in resTuple:
#     print(res)

# 取所有数据
resTuple = cursor.fetchall()
print(type(resTuple))
print(resTuple)
print('共查询%d条数据' % len(resTuple))

# 更新一条数据
# update = cursor.execute("update user set age=100 where name='kongsh'")
# print('修改后受影响的行数为：', update)
# 查询一条数据
# cursor.execute('select * from user where name="kongsh";')
# print(cursor.fetchone())

# 更新2条数据
# sql = "update user set age=%s where name=%s"
# update = cursor.executemany(sql, [(15, 'kongsh'), (18, 'wen')])
# cursor.execute("select * from user where name in ('kongsh','wen');")
# print('更新数据：', cursor.fetchall())

# 删除1条数据
# cursor.execute("delete from user where id=1")
# cursor.execute("select * from user")
# print('删除数据', cursor.fetchall())

# 删除2条数据
# sql = "delete from user where id=%s"
# cursor.executemany(sql, [3, 4])
# cursor.execute("select * from user")
# print('删除数据：')
# for res in cursor.fetchall():
#     print(res)

mysql.begin()
# 修改前查询所有数据
cursor.execute("select * from user;")
print('修改前的数据为：')
for res in cursor.fetchall():
    print(res)

print('*'*40)
# 更新表中第1条数据
cursor.execute("update user set name='xiaoxiaoxiaoxiaoren' where id=5")

# 修改后查询所有数据
cursor.execute("select * from user;")
print('修改后的数据为：')
for res in cursor.fetchall():
    print(res)
print('*'*40)
# 回滚事务
mysql.rollback()
cursor.execute("select * from user;")
print('回滚事务后的数据为：')
for res in cursor.fetchall():
    print(res)

# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print(data)

# 查询有多少张表
cursor.execute("SELECT COUNT(*) TABLES, table_schema FROM information_schema.TABLES  WHERE table_schema = 'pythondb';")
print(cursor.fetchone())

# 查询所有表名
cursor.execute("select table_name from information_schema.tables where table_schema='pythondb';")
print(cursor.fetchone())

cursor.close()
mysql.commit()
mysql.close()
