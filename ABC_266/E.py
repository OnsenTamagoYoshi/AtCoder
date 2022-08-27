import math

def ExValue(val):
    retval = 0
    for i in range(val):
        retval = retval + (1/6) * (i + 1)
        
    return retval

def ExValue_Upper(val):
    retval = 0
    for i in range(val, 7):
        retval = retval + (1/6) * (i)
        
    return retval

N = int(input()) 

before_ExValue = 0
for i in range(N):
    if N == 1:
        print(3.5)
        exit()
    else:
        if i == 0:
            before_ExValue = 3.5
        else:
            # before_ExValueより高い出目が出たらその時点で離脱
            # 低かったら次にかける
            before_ExValue = ExValue_Upper(math.ceil(before_ExValue)) + (before_ExValue * (1/6) *math.floor(before_ExValue))
            
print(before_ExValue)