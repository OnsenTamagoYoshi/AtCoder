N, K = map(int, input().split())
points = list(map(int, input().split()))

for i in range(N - K):
    if points[i] < points[i + K]:
        print('Yes')
    else:
        print('No')
