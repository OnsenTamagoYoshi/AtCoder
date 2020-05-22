import numpy as np

N = int(input())
A = [int(input()) for _ in range(N)]

A_cor = list(range(1, N + 1))
set_A = set(A)
set_A_cor = set(A_cor)

if len(set_A_cor - set_A) == 0:
    print('Correct')
else:
    x = list(set_A_cor - set_A)[0]
    A = np.array(A)
    # 0から始まる整数列のそれぞれの出現回数配列
    count = np.bincount(A)
    # 出現回数配列の最大要素のインデックス抽出(今回はそれが重複値と一致)
    y = np.argmax(count)
    print(str(y) + ' ' + str(x))
