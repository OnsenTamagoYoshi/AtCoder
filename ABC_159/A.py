import math

num_of_even, num_of_odd = map(int, input().split())

def combinations_count(n, r):
    if n < 2:
        return 0
    else:
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

if num_of_even == 1 and num_of_odd == 1:
    print('0')
else:
    print(combinations_count(num_of_odd, 2) + combinations_count(num_of_even, 2))
