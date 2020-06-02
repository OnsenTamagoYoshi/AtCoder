N = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    if number % 2 == 0:
        if number % 3 != 0 and number % 5 != 0:
            print('DENIED')
            exit()

print('APPROVED')