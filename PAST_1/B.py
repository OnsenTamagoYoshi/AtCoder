N = int(input())
A = [int(input()) for _ in range(N)]

for i in range(N - 1):
    diff = A[i + 1] - A[i]

    if diff == 0:
        print('stay')
    elif diff < 0:
        print('down ' + str(abs(diff)))
    else:
        print('up ' + str(diff))
