def largest_number(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z

    print(largest_number(2, 6, 9))
    # e corect dar nu imi da output-ul...
