import numpy as np

N = input()
A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

ans = np.dot(A, B)

if ans == 0:
    print('Yes')
else:
    print('No')


