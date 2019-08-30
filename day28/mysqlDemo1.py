# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/21 11:45
# 文件名称 : pymysql.PY
# 开发工具 : PyCharm

import pymysql

if __name__ == '__main__':
    # 1 连接数据库 #port默认为3306
    host , port , db , user , password ,charset = 'localhost' , 3306, 'jd', 'root', 'root', 'utf8'
    conn = pymysql.connect(
        host = host,
        port = port,
        user = user,
        password = password,
        database = db,
        charset = charset)
    print(type(conn))
    print(conn)
    # 2 获得游标对象
    cursor1 = conn.cursor()

    # 3 通过游标对象执行sql命令 --会发生注入问题
    # sql = 'select * from goods where cate_id = %s and brand_id = %s;'%(1,1)
    #为防止注入问题：采用参数化的方式
    sql = 'select * from goods where cate_id = %s and brand_id = %s;'
    rslt1 = cursor1.execute(sql,[1,1])
    print(rslt1)


    cursor2 = conn.cursor()
    rlst2 = cursor2.execute(sql,[1,2])
    print(rlst2)

    # 4 对于查询结果，通过游标获得查询结果
    while rslt1:
        rslt1 = cursor1.fetchone()
        if rslt1 :
            print(rslt1)


    while rlst2:
        rlst2 = cursor2.fetchone()
        if rlst2 :
            print(rlst2)
    # rec1 = cursor.fetchone()
    # print(rec1)

    # 关闭数据库连接
    cursor1.close()
    cursor2.close()
    conn.close()