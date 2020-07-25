"""Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the
squares of its digits, and repeat the process until the number equals 1
(where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not."""

def is_happy(n):
    previous_n = set()
    previous_n.add(n)
    while n != 1:
        str_n = str(n)
        digits = [int(d) for d in str_n]
        _sum = 0
        for digit in digits:
            _sum+=digit*digit
        n = _sum
        if n not in previous_n:
            previous_n.add(n)
        else:
            return False
            break
    return True

n = 19
print(is_happy(n))
