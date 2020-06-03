N = int(input())
Ps = list(map(int, input().split()))

answer = 0
min_num = 2 * 10 ** 5 + 1
for p in Ps:
    min_num = min(p, min_num)
    if min_num >= p:
        answer = answer + 1

print(answer)