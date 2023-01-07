# 参考
# https://qiita.com/Kept1994/items/20333987a6d73f435f6d#%E7%B4%A0%E5%9B%A0%E6%95%B0%E5%88%86%E8%A7%A3
def getDivisors(n: int):
    lowerDivisors, upperDivisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lowerDivisors.append(i)
            if i != n // i:
                upperDivisors.append(n//i)
        i += 1
    return lowerDivisors + upperDivisors[::-1]

T = int(input())

for _ in range(T):
    N = int(input())
    
    num_list = getDivisors(N)

    p = 0
    q = 0

    if N % (num_list[2] * num_list[2]) == 0:
        p = num_list[2]
        q = num_list[1]
    else:
        p = num_list[1]
        q = num_list[2]

    print(str(p) + ' ' + str(q))
