# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/22 10:26
# 文件名称 : pymysql002.PY
# 开发工具 : PyCharm
from queue import Queue

import pymysql
import time
import threading

from gevent import monkey
monkey.patch_all()

RECORDS = 1000000
THREADNUMBERS = 10

class MysqlPool :
    __instance = None

    def __init__(self,host,port,user,password,db,charset,maxconn = 5):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        self.maxconn = maxconn

        self.pool = Queue(self.maxconn)
        try:
            for _ in range(self.maxconn):
                conn = pymysql.connect(host = self.host,
                                       port = self.port,
                                       user = self.user,
                                       password = self.password,
                                       database = self.db,
                                       charset = self.charset)
                conn.autocommit(True)
                self.pool.put(conn)
        except Exception as e :
            print(e)

    @classmethod
    def getInstance(cls,*args,**kwargs):
        try:
            if not cls.__instance :
                cls.__instance = MysqlPool(*args,**kwargs)
        except Exception as e:
            print(e)
            cls.__instance =None
        return cls.__instance

    def exec_sql(self,sql,data):
        try:
            conn = self.pool.get()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql,data) if data else cursor.execute(sql)
        except Exception as e :
            print(e)
        finally:
            cursor.close()
            self.pool.put(conn)


    def exec_sql_many(self,sql,data):
        try:
            conn = self.pool.get()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql,data) if data else cursor.executemany(sql)
        except Exception as e :
            print(e)
        finally:
            cursor.close()
            self.pool.put(conn)

    def fetch_one(self,sql,data):
        try:
            conn = self.pool.get()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            rslt = cursor.execute(sql,data) if data else cursor.execute(sql)

            return rslt,cursor.fetchone()
        except Exception as e:
            print(e)
            return None,None
        finally:
            cursor.close()
            self.pool.put(conn)

    def fetch_all(self, sql, data):
        try:
            conn = self.pool.get()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            rslt = cursor.execute(sql, data) if data else cursor.execute(sql)

            return rslt, cursor.fetchone()
        except Exception as e:
            print(e)
            return None, None
        finally:
            cursor.close()
            self.pool.put(conn)


    def close(self):
        for _ in range(self.maxconn):
            self.pool.get().close()

def doingInThread(num):
    sql = 'insert into tb1 (sname , class_id ,gender) values (%s,%s,%s)'
    data = (('cyw%d' %i , i , 'M') for i in range(num))
    obj.exec_sql_many(sql,data)


if __name__ == '__main__':
    start = time.time()

    obj = MysqlPool.getInstance(host = 'localhost',port = 3306,user = 'root',password = 'root',db = 'sql_test',charset='utf8',maxconn= THREADNUMBERS)

    t_list = []
    for _  in range(THREADNUMBERS):
        t = threading.Thread(target=doingInThread,args=(RECORDS/THREADNUMBERS,))
        t.start()
        t_list.append(t)

        for t in t_list:
            t.join()

    print("total time" ,time.time() - start)