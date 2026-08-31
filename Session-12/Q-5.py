from functools import reduce

prices = [120, 80, 150, 60]

total = reduce(lambda x,y : x + y, prices)

print(f"Total bill amount: Rs.{total}")

