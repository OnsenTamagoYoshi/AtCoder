a, b = map(int, input().split())

if a == b:
    print(str(a) * b)
else:
    l = []
    l.append(str(a) * b)
    l.append(str(b) * a)
    l.sort()
    print(l[0])