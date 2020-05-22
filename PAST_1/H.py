import numpy as np

num_of_cards = int(input())
zaiko = np.array(list(map(int, input().split())))
num_of_querys = int(input())
querys = [list(map(int, input().split())) for _ in range(num_of_querys)]
num_of_sales = 0

for query in querys:
    # 単品販売
    if query[0] == 1:
        x = query[1] - 1
        a = query[2]
        if zaiko[x] - a >= 0:
            zaiko[x] = zaiko[x] - a
            num_of_sales = num_of_sales + a

    # セット販売
    elif query[0] == 2:
        a = query[1]
        # 奇数番号のカードのみを対象にした在庫チェックで問題ない場合
        if np.all((zaiko[::2] - a) >= 0):
            np.put(zaiko, list(range(0, num_of_cards, 2)), zaiko[list(range(0, num_of_cards, 2))] - a)
            num_of_sales = num_of_sales + len(zaiko[::2]) * a

    # 全種類販売
    else:
        a = query[1]
        # 全カードを対象にした在庫チェックで問題ない場合
        if np.all((zaiko - a) >= 0):
            zaiko = zaiko - a
            num_of_sales = num_of_sales + num_of_cards * a

print(num_of_sales)
