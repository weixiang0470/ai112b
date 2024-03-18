# Maximize : 3x + 2y + 5z 
# Condition:
# x,y,z >= 0
# x + y <= 10
# 2x + z <= 9
# y + 2z <= 11

import math
import random


s=[0.0,0.0,0.0] #Initial x,y,z=0
def equation(s):
    return (3*s[0] + 2*s[1] + 5*s[2]) #return 3x + 2y + 5z
    #return (35*s[0] + 25*s[1])

def P(e, enew, T): # 模擬退火法的機率函數
    if (enew < e):
        return 1
    else:
        return math.exp((e-enew)/T)

def annealing(s, maxGens) : # 模擬退火法的主要函數

    sbest = s                              # sbest:到目前為止的最佳解
    ebest = equation(s)                # ebest:到目前為止的最低能量
    T = 100     # 從 100 度開始降溫               
    for gens in range(maxGens):            # 迴圈，最多作 maxGens 這麼多代。
        snew = neighbour(s)              # 取得鄰居解
        e    = equation(s)              # e    : 目前解的能量
        enew = equation(snew)               # enew : 鄰居解的能量
        T  = T * 0.995                     # 每次降低一些溫度

        if P(e, enew, T)>random.random():  # 根據溫度與能量差擲骰子，若通過
            s = snew                       # 則移動到新的鄰居解
            #print("{} T={:.5f} {}".format(gens, T, s)) # 印出觀察
        if enew > ebest:                 # 如果新解的能量比最佳解好，則更新最佳解。
            sbest = snew
            ebest = enew
    
    #print(f'solution: {sbest}')     # 印出最佳解
    return sbest                           # 傳回最佳解

def neighbour(s):
    #x,y,z = s[0],s[1],s[2]

    x = random.uniform(0.0,10.0)
    y = random.uniform(0.0,11.0)
    z = random.uniform(0.0,9.0)
    while True:
        if x+y > 10 or 2*x + z > 9 or y + 2*z > 11 or x<0 or y<0 or z<0:
        #if 0.32*x + 0.22*y < 8 or 0.11*x + 0.09*y<3 or 0.15*x + 0.1*y<4 or x<=0 or y<=0:
          x = random.uniform(0.0,10.0)
          y = random.uniform(0.0,11.0)
          z = random.uniform(0.0,9.0)
        else : break
    ns = [x,y,z]
    return ns

result = annealing(s,100000)
fail=0
while True:
  New_result = annealing(s,100000)
  if equation(result)>equation(New_result):fail+=1
  else:
    print(f'Result : {equation(result):.2f} , New Result : {equation(New_result):.2f}')
    result = New_result
    fail=0
  if fail>1000:break

print(f'Result : {equation(result):.2f} , x : {result[0]:.2f} , y : {result[1]:.2f} , z : {result[2]:.2f}')
