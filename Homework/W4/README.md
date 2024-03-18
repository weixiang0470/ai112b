# 作業參考老師的模擬退火法框架

# Result
- Maximize : 3x + 2y + 5z 
    - Condition:
        1. x,y,z >= 0
        2. x + y <= 10
        3. 2x + z <= 9
        4. y + 2z <= 11
    - Result, code : `linear2.py`
```
Result : 34.35 , New Result : 34.36
Result : 34.36 , New Result : 34.37
Result : 34.37 , New Result : 34.37
Result : 34.37 , New Result : 34.39
Result : 34.39 , x : 3.40 , y : 6.60 , z : 2.20
```
- 狗糧的結果, 程式碼 : `linear.py`
```
Result : 941.89 , New Result : 942.71
Result : 941.89 , New Result : 943.42
Result : 941.89 , New Result : 944.26
Result : 941.89 , New Result : 941.65
Result : 941.65 , New Result : 940.50
Result : 940.50 , New Result : 942.30
Result : 940.50 , New Result : 941.67
Result : 940.50 , New Result : 941.84
Result : 940.50 , New Result : 941.73
Result : 940.50 , New Result : 942.29
Result : 940.50 , New Result : 943.05
Result : 940.50 , New Result : 943.56
Result : 940.50 , New Result : 942.12
Result : 940.50 , New Result : 942.52
Result : 940.50 , New Result : 944.43
Result : 940.50 , New Result : 940.59
Result : 940.50 , x : 24.02 , y : 4.00
```