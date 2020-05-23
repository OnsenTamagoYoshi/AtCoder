import numpy as np

num_of_member = int(input())
heights = np.array(list(map(int, input().split())), dtype=np.int64)

# 身長の和のリスト[A1+A2, A1+A3, …, A1+AN, A2+A3,　…]
height_sums = np.array([], dtype=np.int64)
for i, height in enumerate(heights):
    height_sums = np.hstack((height_sums, heights[i] + heights[i+1:]))

# 番号の差の絶対値のリスト[1, 2, …, N-1, 1, 2, …, N-2, …]
diffs = np.array([], dtype=np.int64)
for i in range(num_of_member, 1, -1):
    diffs = np.hstack((diffs, np.arange(1, i)))

# 身長の和から番号の差の絶対値を引き、0になれば一致と判定
checks = height_sums - diffs

print(np.count_nonzero(checks == 0))