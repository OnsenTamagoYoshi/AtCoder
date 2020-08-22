import math

X, K, distance = map(int, input().split())

X = abs(X)

max_distance = K * distance

if max_distance <= X:
    print(X - max_distance)
else:
    # Xをdistanceで割って、何回の移動で0を超えるのかを判断
    over_zero_movecount = math.ceil(X / distance)

    # 0を超えたときの座標の絶対値
    over_zero_x = abs(X - over_zero_movecount * distance)
    # 1つ前の移動の絶対値
    over_zero_x_before = abs(X - (over_zero_movecount - 1) * distance)

    # 0を超えた後の残りの移動回数が偶数回の場合
    if (K - over_zero_movecount) % 2 == 0:
        print(over_zero_x)
    # 0を超えた後の残りの移動回数が奇数回の場合
    else:
        print(over_zero_x_before)
