# 5. We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies
# recursively (without loops or multiplication).

def ears(number):
    if number == 1:
        return 2
    else:
        return 2 + ears(number - 1)

print(ears(4))
