def middle(a, b, c):
    """Return the number among a, b, and c that is not the smallest or largest.
    Assume a, b, and c are all different numbers.
    """
    return sorted([a,b,c])[1]


def sum_digits(y: int) -> int:
    """
    Sum all the digits of y.
    """
    sum = 0
    while y > 0:
        digit = y % 10
        y //= 10
        sum += digit
    return sum


def double_eights(n: int) -> bool:
    """
    Return True if n has two eights in a row.
    """
    prev_eight = False
    while n > 0:
        digit = n % 10
        if digit == 8:
            if prev_eight:
                return True
            else:
                prev_eight = True
        else:
            prev_eight = False
        n //= 10
    return False    