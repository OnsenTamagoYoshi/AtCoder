H1, M1, H2, M2, K =map(int, input().split())

sum_m1 = H1 * 60 + M1
sum_m2 = H2 * 60 + M2

print(sum_m2 - sum_m1 - K)