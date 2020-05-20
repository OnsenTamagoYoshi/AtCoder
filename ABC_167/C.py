import numpy as np

num_of_books, num_of_algorithm, understanding = map(int, input().split())

books = []
for _ in range(num_of_books):
    books.append(list(map(int, input().split())))

mincost = -1
# 本1冊に対して買う買わないの2値があるため、2の冊数乗回ループ(bit全探索)
for i in range(2 ** num_of_books):

    # 購入する本のリスト
    bag = []
    totalcost = 0

    # 10進数iを購入のbitパターンとしたときのループ
    for j in range(num_of_books):
        # ビットを指定桁だけ右にシフトし、最下位ビット（購入の有無）をチェック
        # 1(0…1)と論理積を取ることで最下位ビットを確認できる
        if((i >> j) & 1):
            bag.append(books[j][1:])
            totalcost = totalcost + books[j][0]
        
    # すべての理解度が基準を超えているか
    # 購入した本の理解度の合計を算出し、すべて基準値以上か
    # (np.allで要素がすべてtrueか)
    if np.all(np.sum(np.array(bag), axis=0) >= understanding):
        if mincost == -1 or totalcost < mincost:
            mincost = totalcost 

print(mincost)