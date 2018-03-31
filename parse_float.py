def parse_digit(digit):
    if digit == u"1":
        return 1
    if digit == u"2":
        return 2
    if digit == u"3":
        return 3
    if digit == u"4":
        return 4
    if digit == u"5":
        return 5
    if digit == u"6":
        return 6
    if digit == u"7":
        return 7
    if digit == u"8":
        return 8
    if digit == u"9":
        return 9
    if digit == u"0":
        return 0

def parse_float(value):
    total = 0.0
    multiplier = 1.0
    eeth = 1.0
    for digit in value[::-1]:
        if digit == "-":
            total *= -1.0
        elif digit == ".":
            total /= multiplier
            multiplier = 1.0
        elif digit == "e" or digit == "E":
            eeth = 10 ** -total
            total = 0.0
            multiplier = 1.0
        else:    
            total += parse_digit(digit) * multiplier
            multiplier *= 10
    return total / eeth


assert parse_float("1") == 1
assert parse_float("123") == 123
assert parse_float("3502940") == 3502940
assert parse_float("01") == 1
assert parse_float("002703") == 2703
assert parse_float("-123") == -123
assert parse_float("-003920") == -3920
assert parse_float("0.34") == 0.34
assert parse_float("3.0012") == 3.0012
assert parse_float("1503.2001") == 1503.2001
assert parse_float("-250.0") == -250
assert parse_float("-355.4920") == -355.492
assert parse_float("3748e-123") == 3.748e-120
assert parse_float("-000.23E-20") == -2.3e-21