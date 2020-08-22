N = str(input())
array = list(map(int, N))

total = sum(array)

if total % 9 == 0:
    print('Yes')
else:
    print('No')