X, Y, N = map(int, input().split())

# 3個で買った方が安い場合
if (X * 3) >= Y:
    print((N // 3) * Y + (N % 3) * X)
# 1個ずつ買った方が安い場合
else:
    print(X * N)
