from gradientDescendent import *

def f(p):
    [x, y, z] = p
    return (x-1)**2+(y-2)**2+(z-3)**2

p0 = [Value(0), Value(0),Value(0)]

p_final = gradientDescendent(f,p0)

print(f'p_final=[[{p_final[0].data:.8f}],[{p_final[1].data:.8f}],[{p_final[2].data:.8f}]]')