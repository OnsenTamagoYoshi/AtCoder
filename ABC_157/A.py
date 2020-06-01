from decimal import Decimal, ROUND_HALF_UP

N = int(input())

result = Decimal(str(N/2)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
print(result)