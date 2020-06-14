N = int(input())
S = input()

half_i = len(S) // 2

if S[0:half_i] == S[half_i:]:
    print('Yes')
else:
    print('No')
