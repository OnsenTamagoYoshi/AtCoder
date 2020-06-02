N, K = map(int, input().split())

n = 1

while True:
    if K ** n > N:
        break

    n = n + 1

print(n)