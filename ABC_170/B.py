num_of_animals, num_of_foot = map(int, input().split())

for i in range(num_of_animals + 1):
    # 鶴の数を0からインクリメント
    if 2 * i + 4 * (num_of_animals - i) == num_of_foot:
        print('Yes')
        exit()

print('No')