def round(number, ndigits=0):
    sign = 1 - 2 * (number < 0)
    z = 10 ** ndigits
    number = int(abs(number * z) + (abs(number) * 10 * z % 10 > 4))
    return sign * number / z