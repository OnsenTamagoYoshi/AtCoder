X, Y = map(int, input().split())

if X >= Y:
    print('0')
else:
    if (Y - X) % 10 == 0:
        print(str((Y - X) // 10))
    else:
        print(str((Y - X) // 10 + 1))
