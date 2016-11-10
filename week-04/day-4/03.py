# 3. Given a non-negative int n,
# return the sum of its digits recursively (no loops).
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
# while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

def sum_of_digits(number):
    if number < 10:
        return number
    else:
        return number % 10 + (sum_of_digits(int(number / 10)))


print(sum_of_digits(233534))
