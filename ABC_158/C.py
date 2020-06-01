import math

tax_8, tax_10 = map(int, input().split())

price_8_min = tax_8 / 0.08
price_8_max = (tax_8 + 0.99) / 0.08

price_10_min = tax_10 / 0.1
price_10_max = (tax_10 + 0.99) / 0.1

if max(price_8_min, price_10_min) <= min(price_8_max, price_10_max):
    print(math.ceil(max(price_8_min, price_10_min)))
else:
    print('-1')
