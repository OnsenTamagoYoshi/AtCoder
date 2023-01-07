import numpy as np
T = int(input())

for _ in range(T):
    N = int(input())
    num_list = np.array(list(map(int, input().split())))

    ans = np.sum(num_list % 2)

    print(ans)