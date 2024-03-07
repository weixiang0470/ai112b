from random import randint
import numpy as np
import matplotlib.pyplot as plt
citys = [
    (0,0),(0,3),
    (0,2),(0,1),
    (1,0),(1,3),
    (2,0),(2,3),
    (3,0),(3,3),
    (3,1),(3,2)
]
citys2 ={
    6:(0,0),  1:(0,1),  14:(0,2),    3:(0,3),    12:(1,3),    8:(2,3),
    11:(3,3),  7:(3,2),  5:(3,1),    9:(3,0),    10:(2,0),   0:(1,0),
    4:(2,2),    13:(2,1),  2:(1,2), 15:(1,1),
 }


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    #print('From :',p1,'to',p2,' distance:',((x2-x1)**2+(y2-y1)**2)**0.5) 
    return ((x2-x1)**2+(y2-y1)**2)**0.5

def pathLength(p):
    dist = 0
    plen = len(p)
    for i in range(plen):
        #tmp = distance(citys2[i], citys2[(i+1)%plen])
        dist += distance(citys2[p[i]], citys2[p[(i+1)%plen]])
        #print('city2[i]:',citys[p[i]],' citys2[(i+1)%plen]:',citys[p[(i+1)%plen]])
        #print('From :',i,'to',(i+1)%12,' distance:',tmp)
    return dist

def neighbor(p):
    p2=p.copy()
    #np.random.shuffle(p2)
    c1tmp=-1
    c2tmp=-1
    long=len(p)-1
    while(c1tmp==c2tmp):
        c1tmp = randint(1,long)
        c2tmp = randint(1,long)
    tmp=p2[c1tmp]
    p2[c1tmp]=p2[c2tmp]
    p2[c2tmp]=tmp
    return p2
    

def hillClimbing(p, pathLength, neighbor, max_fail=90000):
    fail = 0
    while True:
        np = neighbor(p)
        print('pathLength(np) : ',pathLength(np),'pathLength(p) : ',pathLength(p))
        if pathLength(np)<pathLength(p):
            p = np
            fail = 0
        else:
            fail += 1
            if fail > max_fail:
                return p

path = [i for i in range(len(citys2))]
result = hillClimbing(path,pathLength,neighbor,90000)
path.append(path[0])
print('Init path : ',path)   
print('Init pathLength : ', pathLength(path))

result.append(result[0])
print('Final path : ',result)
for i in range(len(result)):
    #print('From :',citys2[result[i]],'to',citys2[result[(i+1)%len(result)]])
    print('Next:',citys2[result[i]])
print('Final pathLength : ', pathLength(result))


x=[]
y=[]
x2=[]
y2=[]
for i in range(len(result)):
    x1,y1 = citys2[result[i]]
    x.append(x1)
    y.append(y1)
    x1,y1=citys2[path[i]]
    x2.append(x1)
    y2.append(y1)

plt.rcParams["figure.figsize"] = [8, 8]
plt.rcParams["figure.autolayout"] = True
plt.title("Line graph")
plt.plot(x2, y2, color="blue",linestyle='dotted',marker='x',label='Startpath')
plt.plot(x, y, color="red",linestyle='dashdot',marker='o',label='Finalpath')
plt.legend(loc='best')
plt.xlabel(f'Init_Path_Start: {citys2[path[0]]} Final_Path_Start: {citys2[result[0]]}')
plt.show()
