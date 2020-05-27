# 参考
# https://note.com/tanon_cp/n/n2eb2bb1d69f9#OH0EO
import math
import collections

K = int(input())

# intで初期化するため0が返る
cnt = collections.defaultdict(int)
for i in range(1, K + 1):
    for j in range(1, K + 1):
        key = math.gcd(i, j)
        # 最大公約数をkeyにし、同じ最大公約数の出現回数を保持
        cnt[key] = cnt[key] + 1

total = 0
for k in range(1, K + 1):
    for key in cnt.keys():
        # 出現済みの最大公約数との最大公約数を取り、出現回数分を加算する
        total = total + math.gcd(k, key) * cnt[key]

print(total)
