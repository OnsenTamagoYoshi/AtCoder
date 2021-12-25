L, R = map(int, input().split())
S = list(input())

_S = S[L - 1:R][::-1]
S[L - 1:R] = _S
print("".join(S))
