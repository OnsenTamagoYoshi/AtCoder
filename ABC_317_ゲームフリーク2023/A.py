N, H, X = map(int, input().split())
Ps = list(map(int, input().split()))

for i in range(N):
    if H + Ps[i] >= X:
        print(i + 1)
        break
