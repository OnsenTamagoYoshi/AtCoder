import numpy as np

N, W = map(int, input().split())
Weights = list(map(int, input().split()))

Weights = sorted(Weights)

good_numbers = np.zeros(sum(Weights[-3:]) + 1)

# 重りの数はたかだか300個
for i, i_weight in enumerate(Weights):
    # 重りに存在する重さなら1を格納
    good_numbers[i_weight] = 1

    # iで処理中の次のインデックス以降を確認
    for j, j_weight in enumerate(Weights[i+1:]):

        good_numbers[i_weight + j_weight] = 1

        # jで処理中の次のインデックス以降を確認
        for k, k_weight in enumerate(Weights[i+1+j+1:]):

            good_numbers[i_weight + j_weight + k_weight] = 1

print(int(sum(good_numbers[:W+1])))