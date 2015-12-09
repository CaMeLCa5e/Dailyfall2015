def getdigits(n):
    if n < 10:
        return [n]
    return getdigits(n/10) + [n%10]

print getdigits(123)    