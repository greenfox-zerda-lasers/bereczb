# 4. Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def calc(base, power):
    if power == 0:
        return 1
    else:
        return base * (calc(base, power - 1))

print(calc(3, 5))
