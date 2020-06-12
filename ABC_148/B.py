N = int(input())
S, T = input().split()

out = ''
for i in range(N):
    out = out + S[i] + T[i]

print(out)
