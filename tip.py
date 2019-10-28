def tip(total, percentage):
    tip_calculator = (total * percentage) / 100
    return tip_calculator


print(tip(10, 25))
print(tip(0, 100))
print(tip(1400, 20))
