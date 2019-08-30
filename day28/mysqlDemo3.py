# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/21 15:37
# 文件名称 : mysqlDemo3.PY
# 开发工具 : PyCharm
import pymysql


class MysqlDb:
    def __init__(self,host,port,username,password,db,charset="utf8"):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.db = db
        self.charset = charset
        try:
            self.__conn = pymysql.connect(
                        host = self.host,
                        port = self.port,
                        database = self.db,
                        user = self.username,
                        password = self.password,
                        charset = self.charset)
            self.__cursor = self.__conn.cursor()
        except Exception as e:
            print(e)
            self.__conn = None
            self.__cursor = None

    @property
    def conn(self):
        return self.__conn

    @property
    def cursor(self):
        return self.__cursor

    def __del__(self):
        self.close()

    def close(self):
        print("正在关闭DB.")
        if self.cursor:
            self.cursor.close()
            self.__cursor = None
        if self.conn:
            self.conn.close()
            self.__conn = None

    def exec_sql(self,sql,params):
        return self.cursor.execute(sql,params)

    def cud(self,sql,params):
        try:
            rownums = self.exec_sql(sql,params)
            print("成功！") if rownums else print("失败")
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

    def query(self,sql,params):
        try:
            rslt = self.exec_sql(sql,params)
            while rslt:
                rslt = self.cursor.fetchone()
                yield rslt
        except Exception as e :
            print(e)
            return None

if __name__ == '__main__':
    mysql = MysqlDb(host="localhost",
                    port=3306,
                    username = "root" ,
                    password = 'root',
                    db="creditcard"
                    )

    # # cat_id = input("catid:")
    # # brand_id = input("brandid:")
    # # sql = 'select id,name,price from goods where cate_id = %s and brand_id = %s'
    # # for item in mysql.query(sql,[cat_id,brand_id]):
    # #     print(item)
    #
    # name = input("请输入新增商品名：")
    # cate_id = input("请输入新增商品类别id：")
    # brand_id = input("请输入新增商品品牌id：")
    # price = input("请输入新增商品市场价格：")
    # insert_sql = """
    #         insert into goods
    #         (name, cate_id,brand_id,price)
    #         values
    #         (%s,%s,%s,%s)
    #     """
    #
    # mysql.cud(insert_sql, [name, cate_id, brand_id, price])

    update_sql = "update users set %s = %s where username = %s"
    role = 'role'.replace('\'','')
    mysql.cud(update_sql,[role,1,'admin'])



