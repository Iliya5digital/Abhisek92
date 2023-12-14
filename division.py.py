def divide(a, b):
    if a == 0:
        return 0
    if b == 1:
        return a
    if b == -1:
        return -a

    negative = (a < 0) ^ (b < 0)

    # Convert a and b to positive
    a = abs(a)
    b = abs(b)

    quotient = 0
    while a >= b:
        shift = 0
        while a >= (b << shift):
            shift += 1
        shift -= 1
        quotient += (1 << shift)
        a -= (b << shift)
    if negative:
        quotient = -quotient
    return quotient