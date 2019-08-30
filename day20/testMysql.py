# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/9 9:05
# 文件名称 : testMysql.PY
# 开发工具 : PyCharm

import pymysql

# # 打开数据库连接
# # db = pymysql.connect("localhost", "test", "root", "root")
# db = pymysql.connect(user='root', password='root', database='test', charset='utf8')
#
#
# cursor = db.cursor()
# query = ("select * from test1")
# cursor.execute(query)
# for (id, name,cardId,cardPswd) in cursor:
#     print(id, name,cardId,cardPswd)
# cursor.close()
# db.close()
#
#
# #####`````````````````````````````````````````````````````
# # 打开数据库连接
# db = pymysql.connect(user='root', password='root', database='test', charset='utf8')
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#
# # 使用预处理语句创建表
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""
#
# cursor.execute(sql)
#
# # 关闭数据库连接
# db.close()

#############``````````````````````````````````````````````

# 打开数据库连接
db = pymysql.connect(user='root', password='root', database='test', charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO TEST1(username,\
       password,信用卡号,信用卡密码) \
       VALUES ('%s', '%s',  %s,  '%s')" % \
      ('wmn', 'mnjiang', 84562154, 685423)
try:
    # 执行sql语句
    cursor.execute(sql)
    # 执行sql语句
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()
finally:
    # 关闭数据库连接
    db.close()

