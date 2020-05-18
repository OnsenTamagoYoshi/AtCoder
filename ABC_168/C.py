import math

# A:時針の長さ
# B:分針の長さ
# H:時間
# M:分
A, B, H, M = map(int, input().split())

# 時針のなす角
H_angle = H * 30 + (M / 60 * 30)
# 分針のなす角
M_angle = M * 6

# 針のなす角
H_M_angle = abs(H_angle - M_angle)

cosHM = math.cos(math.radians(H_M_angle))

C2 = A**2 + B**2 - 2*A*B*cosHM

print(math.sqrt(C2))