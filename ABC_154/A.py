S, T = input().split()
A, B = map(int, input().split())
U = input()

if U == S:
    A = A - 1
else:
    B = B - 1

print(str(A) + ' ' + str(B))