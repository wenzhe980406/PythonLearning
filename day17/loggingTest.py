# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/6 16:43
# 文件名称 : logging.PY
# 开发工具 : PyCharm

import logging

# logging.basicConfig()
# logging.debug("this is a debug message")
# logging.info("this is a info message")
# logging.warning("this is a debug message")
# logging.error("this is a debug message")
# logging.critical("this is a debug message")


logging.basicConfig(filename='test.log',filemode="w",format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",level=logging.DEBUG)
logging.debug("this is a debug message")
logging.info("this is a info message")
logging.warning("this is a debug message")
logging.error("this is a debug message")
logging.critical("this is a debug message")