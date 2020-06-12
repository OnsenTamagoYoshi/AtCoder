A, B, K = map(int, input().split())

if K - A <= 0:
    print(str(A - K) + ' ' + str(B))
else:
    print('0 ' + str(max(0, B - (K - A))))
