X = input()

ans = 0
if len(X) > 1001:
    # Xが大
    _X = int(X)
    for i in range(1001):
        if i != 0:
            ans = ans + int(X[:-i])
    ans = ans + int(X)
else:
    # Xが小
    _X = int(X)
    for i in range(len(X)):
        if i != 0:
            ans = ans + int(X[:-i])
    ans = ans + int(X)

print(ans)