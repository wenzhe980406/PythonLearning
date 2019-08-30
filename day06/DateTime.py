# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/22 13:37
# 文件名称 : DateTime.PY
# 开发工具 : PyCharm
#datetime
# import datetime
# #返回当前的日期,不带时间
import time
#
# print(datetime.date.today())
# #返回当前的日期和时间，到毫秒级
# print(datetime.datetime.today())
# print(datetime.datetime.now())
#
# #时间和字符串的转换，格式如下：
# #%Y -- 年份  四个数字     %y -- 两个数字（建议不要用）容易歧义
# str_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print(str_date,type(str_date))
#
# #如何把字符串转换成时间
# #strftime  -- string format time
# #strptime  -- string parse time
# #必须两个参数，第一个是需要转换的字符串，第二个是时间的格式，第一个字符一定要符合是第二个集合
# # date1 = datetime.datetime.strptime("20200101 01:01:01","%Y-%m-%d %H:%M:%S")
# # print(date1,type(date1))
#
# # today = datetime.date.strptime("2028-07-48","%Y%m%d")
#
#
# #计算两个日期之间的时间差
# dt2028 = datetime.datetime.strptime("2028-01-01","%Y-%m-%d")
# dt2019 = datetime.datetime.strptime("2009-01-01","%Y-%m-%d")
# today = datetime.datetime.today()
# delta = dt2028 - today
# print(delta)
# days = delta.days
# print(days)
# print(delta.seconds)
#
#
# #datetime对象的属性
#
# today = datetime.datetime.today()
# print(today.year,today.month,today.day,
#       today.hour,today.minute,today.weekday)

#时间戳的概念
#time,time()

# start_time = time.time()
# MAX_LIMIT = 10000000
#
# rslt = []
# for i in range(MAX_LIMIT) :
#     if(i % 2) :
#         rslt.append(i)
#
# print(len(rslt),rslt[0],rslt[-1])
# end_time = time.time()
#
# print("total last time :%.2f" %(end_time - start_time))
#
# #推导式
# start_time1 = time.time()
# rslt1 = [i for i in range(MAX_LIMIT) if i % 2]
#
# print(len(rslt1),rslt1[0],rslt1[-1])
# end_time1 = time.time()
# print("total last time :%.2f" %(end_time1 - start_time1))

#延迟输出
# string = "*" * 50
# for i in string:
#     print(i,end="")
#     time.sleep(1)

print(time.strftime('%Y',time.localtime()))#获取完整年份
print(time.strftime('%y',time.localtime()))#获取简写年份
print(time.strftime('%m',time.localtime()))#获取月
print(time.strftime('%d',time.localtime()))#获取日
print(time.strftime('%Y-%m-%d',time.localtime()))#获取年-月-日
print(time.strftime('%H',time.localtime()))#获取时，24小时制
print(time.strftime('%I',time.localtime()))#获取时，12小时制
print(time.strftime('%M',time.localtime()))#获取分
print(time.strftime('%S',time.localtime()))#获取秒
print(time.strftime('%H:%M:%S',time.localtime()))#获取时：分：秒
print(time.strftime('%a',time.localtime()))#本地简化星期
print(time.strftime('%A',time.localtime()))#本地完整星期
print(time.strftime('%b',time.localtime()))#本地简化月份
print(time.strftime('%B',time.localtime()))#本地完整月份
print(time.strftime('%c',time.localtime()))#本地日期和时间表示
print(time.strftime('%j',time.localtime()))#一年中的第几天
print(time.strftime('%p',time.localtime()))#一年中的第几天
print(time.strftime('%U',time.localtime()))#一年中的第几个星期
print(time.strftime('%w',time.localtime()))#星期几，星期天为开始
print(time.strftime('%W',time.strftime()))#一年中的第几个星期，星期一未开始
print(time.strftime('%x',time.localtime()))#本地日期表示
print(time.strftime('%X',time.localtime()))#本地时间表示
print(time.strftime('%z',time.localtime()))#当前时区
print(time.strftime('%%',time.localtime()))#输出%本身