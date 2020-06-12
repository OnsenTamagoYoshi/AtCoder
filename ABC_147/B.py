S = input()

S_r = list(reversed(S))

hug = 0
for i in range(len(S) // 2):
    if S[i] != S_r[i]:
        hug = hug + 1

print(hug)
