import math

X = int(input())

# √nまでで判定すればいい
def is_prime(n):
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

while True:
    if is_prime(X):
        print(X)
        exit()

    X = X + 1
