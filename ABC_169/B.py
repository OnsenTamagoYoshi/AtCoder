N = int(input())
A = list(map(int, input().split()))

if A.count(0) >= 1:
    print(0)
    exit()

answer = 1
for _ in A:
    answer *= _
    if answer > 1000000000000000000:
        print('-1') 
        exit()

print(answer)
