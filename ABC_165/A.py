K = int(input())
from_A, to_B = map(int, input().split())

for i in range(from_A, to_B + 1):
    if i % K == 0:
        print('OK')
        exit()

print('NG')