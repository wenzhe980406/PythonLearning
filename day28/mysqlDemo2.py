# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/21 14:15
# 文件名称 : mysqlDemo2.PY
# 开发工具 : PyCharm
import pymysql

if __name__ == '__main__':
    conn = pymysql.connect(user = 'root',password = 'root',database = 'jd',charset = 'utf8')

    cursor = conn.cursor()

    #执行增C 改U 删D --CUD
    # name = input("name:")
    # cate_id = input('CATE_ID:')
    # brand_id = input("brand_id:")
    # price = input("price:")

    # insert_sql = """
    #     insert into goods
    #     (name ,cate_id,brand_id,price)
    #     values
    #     (%s,%s,%s,%s)
    # """

    # rownum = cursor.execute(insert_sql,[name,cate_id,brand_id,price])

    # id = input("id:")
    # price = input("price:")
    #
    # update_sql = """
    #     update goods set price=%s where id = %s
    # """
    # rownum = cursor.execute(update_sql,[price,id])

    id = input("id:")

    sql = 'delete from goods where id=%s'

    rownum = cursor.execute(sql,[id])
    print("增加成功！") if rownum else print("失败！")

    conn.commit()

    cursor.close()
    conn.close()
