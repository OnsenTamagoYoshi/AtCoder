red, green, blue = map(int, input().split())
K = int(input())

for i in range(K):
    if red >= green:
        green = green * 2
    elif green >= blue:
        blue = blue * 2

if red < green and green < blue:
    print('Yes')
else:
    print('No')