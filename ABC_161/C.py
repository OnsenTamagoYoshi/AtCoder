N, K = map(int, input().split())

div_result = N // K
div_remainder = N % K
abs_value = abs(div_remainder - K)

if div_remainder <= abs_value:
    if div_result == 0:
        print(N)
    else:
        print(div_remainder)
else:
    print(abs_value)
