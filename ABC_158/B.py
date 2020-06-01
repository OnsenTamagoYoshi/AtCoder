N, num_of_blue, num_of_red = map(int, input().split())

num_of_repetition = (N // (num_of_blue + num_of_red))
remainder_s = N % (num_of_blue + num_of_red)

count_b = num_of_blue * num_of_repetition + min(num_of_blue, remainder_s)

print(count_b)