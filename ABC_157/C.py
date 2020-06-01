digit, num_of_querys = map(int, input().split())

querys = []
for _ in range(num_of_querys):
    querys.append(list(map(int, input().split())))

guess_num = ['*'] * digit

for query in querys:
    # すでに数値が決まっていて、かつ別の数値が設定される場合
    if guess_num[query[0] - 1] != '*' and guess_num[query[0] - 1] != str(query[1]):
        print('-1')
        exit()
    # 2桁以上で左から1桁目に0が設定される場合
    elif digit >= 2 and query[0] == 1 and query[1] == 0:
        print('-1')
        exit()
    else:
        guess_num[query[0] - 1] = str(query[1])

for i, _ in enumerate(guess_num):
    if _ == '*':
        if i == 0:
            guess_num[i] = '1'
        else:
            guess_num[i] = '0'

print(''.join(guess_num))