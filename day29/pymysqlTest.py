# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/22 10:08
# 文件名称 : pymysqlTest.PY
# 开发工具 : PyCharm

import pymysql
import time

RECORDS = 1000000

if __name__ == '__main__':
    strat = time.time()
    try:
        conn= pymysql.connect(host = 'localhost',port = 3306,user = 'root',password = 'root',database = 'sql_test',charset='utf8')
        conn.autocommit(True)
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        sql = 'insert into tb1(sanme,class_id,gender) values (%s,%s,%s)'
        data = (("刘京东%d"%i,i,"M") for i in range(RECORDS))
        rlst = cursor.executemany(sql,data)

        print("插入成功") if rlst else print("失败")
        print("total time :",time.time() - strat)
    except Exception as e :
        print(e)

    finally:
        cursor.close()
        conn.close()

