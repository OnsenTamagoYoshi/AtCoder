A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))
num_of_number = int(input())

numbers = []

for _ in range(num_of_number):
    numbers.append(int(input()))

for number in numbers:
    for i, A in enumerate(A1):
        if A in numbers:
            A1[i] = -1

    for i, A in enumerate(A2):
        if A in numbers:
            A2[i] = -1

    for i, A in enumerate(A3):
        if A in numbers:
            A3[i] = -1

# 横の確認
if A1.count(-1) == 3 or A2.count(-1) == 3 or A3.count(-1) == 3:
    print('Yes')
    exit()

# 縦の確認
V1_count = [A1[0], A2[0], A3[0]].count(-1)
V2_count = [A1[1], A2[1], A3[1]].count(-1)
V3_count = [A1[2], A2[2], A3[2]].count(-1)
if V1_count == 3 or V2_count == 3 or V3_count == 3:
    print('Yes')
    exit()

# 斜めの確認
D1_count = [A1[0], A2[1], A3[2]].count(-1)
D2_count = [A1[2], A2[1], A3[0]].count(-1)
if D1_count == 3 or D2_count == 3:
    print('Yes')
else:
    print('No')