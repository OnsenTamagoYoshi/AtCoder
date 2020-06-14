import numpy as np

length = int(input())
As = list(map(int, input().split()))

# 1が1つでもいた場合　または
# 長さが1　または　すべて同じ数字のみの場合
# ⇒0確定
if 1 in As or len(set(As)) == 1:
    print(0)
    exit()

As.sort(reverse=True)
As = np.array(As)

out = 0
while len(As) > 0:
    # 末尾(最小値)を取得してリストから削除
    e = As[-1]
    As = np.delete(As, -1)
    
    # 重複がある場合
    if e in As:
        # 割り切れたもののインデックス抽出
        tmp = np.where(As % e == 0)
        tmp_ones = np.ones(len(As), dtype=bool)
        tmp_ones[tmp] = False
        As = As[tmp_ones]
    # 重複がない場合
    else:
        out = out + 1
        # 割り切れたもののインデックス抽出
        tmp = np.where(As % e == 0)
        tmp_ones = np.ones(len(As), dtype=bool)
        tmp_ones[tmp] = False
        As = As[tmp_ones]

print(out)
