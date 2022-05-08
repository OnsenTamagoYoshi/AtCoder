N, Q = map(int, input().split())
X = []
for _ in range(Q):
    X.append(int(input()))

# リストには1...Nの自然数が並んでいる
result_list = list(range(1, N+1))

# 普通にループしたらおそらくTLEになる
for i in range(Q):

    # X[i]の値のインデックスを取得
    tmp_index = result_list.index(X[i])
    # もし最終インデックスなら左隣と値交換
    if tmp_index == len(result_list) - 1:
        result_list[tmp_index - 1], result_list[tmp_index] = result_list[tmp_index], result_list[tmp_index - 1]
    # そうでないなら右隣と交換
    else:
        result_list[tmp_index + 1], result_list[tmp_index] = result_list[tmp_index], result_list[tmp_index + 1]

print(*result_list)
