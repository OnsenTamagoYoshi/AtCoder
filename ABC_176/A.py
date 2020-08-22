N, X, T = map(int, input().split())

if N % X == 0:
    print(int(N / X) * T)
else:
    print(((N // X) + 1) * T)
