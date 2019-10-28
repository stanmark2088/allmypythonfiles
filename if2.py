def greater_than(x, y):
    if x > y:
        return x
    if y > x:
        return y
    if x == y:
        return "These numbers are the same"


# numerele trebuiesc definite
x = 1
y = 1

print(greater_than(x, y))


def graduation_reqs(credits):
    if credits >= 120:
        return "You have enough credits to graduate!"
    if credits < 120:
        return "It's like Budapest all over again"


credits = 80
print(graduation_reqs(80))


