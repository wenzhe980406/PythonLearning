# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/4 10:36
# 文件名称 : matplotlabDemo.PY
# 开发工具 : PyCharm
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.figure(figsize=(10,6),dpi=80)
plt.plot(X,C,color='blue',linewidth=2.5,linestyle='-')
plt.plot(X,S,color='red',linewidth=2.5,linestyle='-')
plt.xlim(X.min()*1.1,X.max()*1.1)
plt.ylim(C.min()*1.1,C.max()*1.1)
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],
           [r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])
plt.yticks([-1,0,+1])
# plt.show()

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

t = 2 * np.pi/3
plt.plot([t,t][0,np.cos(t)],color ='blue',linewidth=1.5,linestyle='--')
plt.scatter([t,],[np.cos(t)],50,color='blue')



plt.show()


plt.contourf