import collections

num_of_numbers = int(input())
numbers = list(map(int, input().split()))
num_of_operation = int(input())

# intで初期化するため0が返る
cnt = collections.defaultdict(int)
# numbersに含まれる各数字の出現回数を保持
# for i in set(numbers):
#     cnt[i] = numbers.count(i)

# number.count(i)だとTLE,以下のループだと時間内に収まる
for i in numbers:
    cnt[i] += 1

# 初期状態の和を算出
ans = sum(numbers)

for i in range(num_of_operation):
    B, C = map(int, input().split())

    # 置換対象の数字が存在する場合
    if B in cnt:
        tmpB = cnt[B]
        tmpC = cnt[C]
        ans = ans - (B * tmpB) + (C * tmpB)

        cnt[C] = tmpC + tmpB
        cnt.pop(B)

    print(ans)


