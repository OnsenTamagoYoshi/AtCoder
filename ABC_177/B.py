S = str(input())
T = str(input())

max_equal_count = 0

for i in range(len(S) - len(T) + 1):
    equal_count = 0
    
    for j in range(len(T)):
        if S[i + j] == T[j]:
            equal_count = equal_count + 1

    if max_equal_count < equal_count:
        max_equal_count = equal_count

print(len(T) - max_equal_count)
