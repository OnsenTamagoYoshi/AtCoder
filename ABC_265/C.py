H, W = map(int, input().split())

G = []
for i in range(H):
    G.append(input())

now_i = 0
now_j = 0

mugenflag = 0

for i in range(H*W):
    now_value = G[now_i][now_j]
    if now_value == 'U':
        if now_i != 0:
            now_i = now_i - 1
        else:
            break

    elif now_value == 'D':
        if now_i != H - 1:
            now_i = now_i + 1
        else:
            break

    elif now_value == 'L':
        if now_j != 0:
            now_j = now_j - 1
        else:
            break

    else:
        if now_j != W - 1:
            now_j = now_j + 1
        else:
            break

    # 最終行にたどり着いたら無限と判定
    if i == (H*W - 1):
        mugenflag = 1

if mugenflag == 0:
    print( str(now_i + 1) + ' ' + str(now_j + 1))
else:
    print( str(-1) )