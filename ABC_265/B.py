import numpy as np

N, M, T = map(int, input().split())

# 部屋ごとの消費時間
A = np.array(list(map(int, input().split())))

# 符号反転
A = -A

X = [0] * M
Y = [0] * M

# ボーナス部屋とボーナス時間の組み合わせ
for i in range(M):
    X[i], Y[i] = map(int, input().split())

    A[ X[i] - 1] = A[ X[i] - 1] + Y[i]

# この時点でAの合計値をTから引いてTが残っているならクリア
if T + np.sum(A) > 0:
    print('Yes')
else:
    print('No')
