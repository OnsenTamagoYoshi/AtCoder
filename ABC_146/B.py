N = int(input())
S = input()

out = ''

for s in S:
    if ord(s) + N > 90:
        out = out + chr(64 + (ord(s) + N - 90))
    else:
        out = out + chr(ord(s) + N)

print(out)
