from engine import Value
import numpy as np
from numpy.linalg import norm


#Add gradientDescendent 
def gradientDescendent(f, p0, h=0.01, max_loops=100000, dump_period=1000):
    p = p0.copy()
    for i in range(max_loops):
        fp = f(p)
        #print('fp=',fp)
        fp.backward() # 計算梯度 gp
        #print('p=',p)
        gp=[]
        for paras in p:
            gp.append(paras.grad)
        glen = norm(gp) # norm = 梯度的長度 (步伐大小)
        #if i%dump_period == 0: 
            #print(f'{i}:f(p)={fp} p={p} gp={gp} glen={glen}')
        if glen < 0.00001: # 如果步伐已經很小了，那麼就停止吧！
            break
        gh = np.multiply(gp, -1*h) # gh = 逆梯度方向的一小步
        p +=  gh # 向 gh 方向走一小步
    #print(f'{i}:f(p)={fp} p={p} gp={gp} glen={glen}')
    return p # 傳回最低點！