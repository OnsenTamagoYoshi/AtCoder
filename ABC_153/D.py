import math

H = int(input())

n = 1
# 1体のモンスターを消滅させるまでの回数
while H > 1:
    H = math.floor(H / 2)
    n = n + 1

attack = 0
# 分裂ごとにモンスターが倍になるため、回数を2倍する
for i in range(n):
    attack = attack + 2 ** i

print(attack)
