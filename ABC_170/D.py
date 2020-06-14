import numpy as np

length = int(input())
As = list(map(int, input().split()))

As.sort()

# indexを数値と紐づけるために+1増やした数にする
check = np.zeros(10**6+1)

answer = 0

# 与えられた数列の小さいものから順にループ
for i in range(length):
    if check[As[i]] == 0:
        # 与えられた数値の倍数すべてに1を立てる
        # checkは0始まりのため、0と倍数要素に1が立つ
        check[::As[i]] = 1
        
        # checkリストが0の状態で数列の最後であればanswerへの加算は確定
        # また、同じ数字が複数ある場合はカウントさせない
        if  i == (length - 1) or  As[i] != As[i + 1]:
                answer = answer + 1

print(answer)
