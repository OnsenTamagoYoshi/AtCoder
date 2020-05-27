import collections

num_of_employee = int(input())
employeenos = list(map(int, input().split()))

c = collections.Counter(employeenos)
for i in range(1, num_of_employee + 1):
    print(c[i])
