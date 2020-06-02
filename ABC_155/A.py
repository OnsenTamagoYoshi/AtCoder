numbers = list(map(int, input().split()))

for i in range(1, 10):
    if numbers.count(i) == 2:
        print('Yes')
        exit()

print('No')