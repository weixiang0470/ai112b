from random import random, randint, choice
import numpy as np

courses = [
{'teacher': '  ', 'name':'　　', 'hours': -1},
{'teacher': '甲', 'name':'機率', 'hours': 2},
{'teacher': '甲', 'name':'線代', 'hours': 3},
{'teacher': '甲', 'name':'離散', 'hours': 3},
{'teacher': '乙', 'name':'視窗', 'hours': 3},
{'teacher': '乙', 'name':'科學', 'hours': 3},
{'teacher': '乙', 'name':'系統', 'hours': 3},
{'teacher': '乙', 'name':'計概', 'hours': 3},
{'teacher': '丙', 'name':'軟工', 'hours': 3},
{'teacher': '丙', 'name':'行動', 'hours': 3},
{'teacher': '丙', 'name':'網路', 'hours': 3},
{'teacher': '丁', 'name':'媒體', 'hours': 3},
{'teacher': '丁', 'name':'工數', 'hours': 3},
{'teacher': '丁', 'name':'動畫', 'hours': 3},
{'teacher': '丁', 'name':'電子', 'hours': 4},
{'teacher': '丁', 'name':'嵌入', 'hours': 3},
{'teacher': '戊', 'name':'網站', 'hours': 3},
{'teacher': '戊', 'name':'網頁', 'hours': 3},
{'teacher': '戊', 'name':'演算', 'hours': 3},
{'teacher': '戊', 'name':'結構', 'hours': 3},
{'teacher': '戊', 'name':'智慧', 'hours': 3}
]

teachers = ['甲', '乙', '丙', '丁', '戊']

rooms = ['A', 'B']

slots = [
'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'A37',
'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47',
'A51', 'A52', 'A53', 'A54', 'A55', 'A56', 'A57',
'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17',
'B21', 'B22', 'B23', 'B24', 'B25', 'B26', 'B27',
'B31', 'B32', 'B33', 'B34', 'B35', 'B36', 'B37',
'B41', 'B42', 'B43', 'B44', 'B45', 'B46', 'B47',
'B51', 'B52', 'B53', 'B54', 'B55', 'B56', 'B57',
]

sch=[0]* len(slots)
sch_init=[0]* len(slots)

def randSlot() :
    return randint(0, len(slots)-1)

def randCourse() :
    return randint(0, len(courses)-1)

def hillClimbing(sch, height, neighbor, max_fail):
    global sch_init
    sch_init = init(sch)
    fail = 0
    while True:
        nsch = neighbor(sch)
        if height(nsch)>height(sch):
            sch = nsch
            str(sch,height(sch),fail)
            fail = 0
        else:
            fail += 1
            if fail > max_fail:
                return sch,height(sch),fail

def neighbour(sch):
    fill=sch.copy()
    choose=randint(0,1)
    if choose == 0 :
        i=randSlot()
        fill[i]=randCourse()
    else :
        i=randSlot()
        j=randSlot()
        tmp=fill[i]
        fill[i]=fill[j]
        fill[j]=tmp
    return fill

def height(sch):
    courseCounts=[0]*len(courses)
    fill=sch.copy()
    score=0
    for si in range(len(slots)):
        courseCounts[fill[si]] +=1

        if si < len(slots)-1 and fill[si] == fill[si+1] and si%7 != 6 and si%7 != 3:
            score+=0.1
        if si%7 ==0 and fill[si]!=0:
            score-=0.08
        if (si%7==1 or si%7==2 or si%7==3 or si%7==4 or si%7==5 or si%7==6) and fill[si] ==0:
            score -=0.15
    
    for ci in range(len(courses)):
        if (courses[ci]['hours'] >= 0):
            score -= abs(courseCounts[ci] - courses[ci]['hours'])
    return score

def str(sch,score,fail) :    # 將解答轉為字串，以供印出觀察。
    outs = []
    fill = sch.copy()
    for i in range(len(slots)):
        c = courses[fill[i]]
        if i%7 == 0:
            outs.append('\n')
        outs.append(slots[i] + ':' + c['name'])
    print('score={:f} fail={:f} {:s}\n\n'.format(score,fail,' '.join(outs))) 

def init(sch):
    fill = [0] * len(slots)
    for i in range(len(slots)):
        fill[i] = randCourse()
    return fill


result,score,fail = hillClimbing(sch, height, neighbour, max_fail=90000)

str(result,score,fail)

str(sch_init,0,0)