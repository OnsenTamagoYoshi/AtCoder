N = int(input()) 
As = sorted(list(map(int, input().split())))

Sn = (As[0] + As[-1]) * (N + 1) / 2

print(int(Sn - sum(As)))