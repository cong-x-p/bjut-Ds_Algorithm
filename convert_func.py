def convert(length: float):
    price = 0
    if 0 <= length < 6:
        price = 3
    elif 6 <= length < 12:
        price = 4
    elif 12 <= length < 22:
        price = 5
    elif 22 <= length < 32:
        price = 6
    elif 32 <= length < 52:
        price = 7
    elif 52 <= length < 72:
        price = 8
    elif 72 <= length < 92:
        price = 9
    return price
