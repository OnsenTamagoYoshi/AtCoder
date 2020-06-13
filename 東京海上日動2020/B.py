A, A_v = map(int, input().split())
B, B_v = map(int, input().split())
Ts = int(input())

# AがBより常に左にいることにする
if A > B:
    A, B = B, A

if A + A_v * Ts >= B + B_v * Ts:
    print('YES')
else:
    print('NO')