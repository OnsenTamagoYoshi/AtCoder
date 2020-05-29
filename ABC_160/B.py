X = int(input())

num_of_500 = X // 500
num_of_5 = (X % 500) // 5

print(str(num_of_500 * 1000 + num_of_5 * 5))
