# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/9 16:39
# 文件名称 : PandasDemo06.PY
# 开发工具 : PyCharm

import numpy as np
import pandas as pd



dict_obj = {'key1' : ['a','b','a','b',
                      'a','b','a','a'],
            'key2' : ['one','one','two','three',
                      'two','two','one','three'],
            'data1' : np.random.randint(1,10,8),
            'data2' : np.random.randint(1,10,8)}
df_obj = pd.DataFrame(dict_obj)

# k2_sum = df_obj.groupby('key1').agg('sum')


# transform方法
# 方法2 使用transform
k1_sum_tf = df_obj.groupby('key1').transform(sum).add_prefix('sum_')
print(k1_sum_tf)

df_obj[k1_sum_tf.columns] = k1_sum_tf
print(df_obj)

# 自定义函数传入transform
def diff_mean(s):
    return s - s.mean()

print(df_obj.groupby('key1').transform(diff_mean))