# Challenge  1

# Create a function named in_range() that has three parameters named num,
# lower, and upper.
# The function should return True if num is greater than or equal to lower
#  and less than or equal to upper. Otherwise, return False.


def in_range(num, lower, upper):
    if (num >= lower) and (num <= upper):
        return True
    else:
        return False


print(in_range(10, 10, 10))
print(in_range(5, 10, 20))

# Challenge 2

# Create a function named movie_review() that has one parameter named rating.
# If rating is less than or equal to 5, return "Avoid at all costs!". If rating
# is between 5 and 9, return "This one was fun.". If rating is 9 or above,
# return "Outstanding!"


def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif (rating > 5) and (rating < 9):
        return "This one was fun."
    else:
        return "Outstanding!"


print(movie_review(9))
print(movie_review(4))
print(movie_review(6))

# Challenge 3

# Create a function named twice_as_large() that has two parameters named num1
#  and num2.
# Return True if num1 is more than double num2. Return False otherwise.


def twice_as_large(num1, num2):
    if num1 > 2 * num2:
        return True
    else:
        return False


print(twice_as_large(10, 5))
print(twice_as_large(11, 5))

# Challenge 4

# Create a function named large_power() that takes two parameters named
#  base and exponent.
# If base raised to the exponent is greater than 5000, return True, otherwise
# return False


def large_power(base, exponent):
    if (base ** exponent) > 5000:
        return True
    else:
        return False


print(large_power(2, 13))
print(large_power(2, 12))

# Challenge 5

# Create a function called divisible_by_ten() that has one parameter named num.
# The function should return True if num is divisible by 10, and False otherwise.
#  Consider how to use modulo (%) to check for divisibility.


def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False


print(divisible_by_ten(20))
print(divisible_by_ten(25))

# Challenge 6

# Create a function called max_num() that has three parameters named
#  num1, num2, and num3.
# The function should return the largest of these three numbers.If any of
# two numbers tie as the largest, you should return "It's a tie!".


def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return "It's a tie!"


        # aici am smecherit programul in idea ca nu am mai bagat
        # ca num1 = num2 , num 1 = num3 m etc am dat ca orice altceva s-ar intampla sa
        # apara this is a tie
print(max_num(-10, 0, 10))
print(max_num(-10, 5, -30))
print(max_num(-5, -10, -10))
print(max_num(2, 3, 3))

# Challenge 7

# Create a function called over_budget that has five parameters named budget,
#  food_bill, electricity_bill, internet_bill, and rent.
# The function should return True if budget is less than the sum of the other
# four parameters. You’ve gone over budget! Return False otherwise.


def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    if budget < (food_bill+electricity_bill+internet_bill+rent):
        return True
    else:
        return False


print(over_budget(100, 20, 30, 10, 40))
print(over_budget(80, 20, 30, 10, 30))

# Challenge 8

# Create a function named always_false() that has one parameter named num.
# Using an if statement, your variable num, and the operators >, and <, make
# it so your function will return False no matter what number is stored in num.
# An if statement that is always false is called a contradiction. You will rarely
# want to do this while programming, but it is important to realize it is possible
# to do this.

# varianta mea


def always_false(num):
    if num > (num+1) and num < (num-1):
        return True
    else:
        return False


print(always_false(0))
print(always_false(-1))
print(always_false(1))

# varianta codeacademy


def always_false(num):
    if (num > 0 and num < 0):
        return True
    else:
        return False


print(always_false(0))
print(always_false(-1))
print(always_false(1))

# Challenge 9

# Create a function named not_sum_to_ten() that has two parameters named
#  num1 and num2.
# Return True if num1 and num2 do not sum to 10. Return False otherwise.


def not_sum_to_ten(num1, num2):
    if num1 + num2 != 10:
        return True
    else:
        return False


print(not_sum_to_ten(9, -1))
print(not_sum_to_ten(9, 1))
print(not_sum_to_ten(5, 5))

# Challenge 10

# Create a function named same_name() that has two parameters named your_
# name and my_name.
# If our names are identical, return True. Otherwise, return False.


def same_name(your_name, my_name):
    if your_name == my_name:
        # A single equal sign is used to assign a value to a variable.
        # double equal is used to compare two values on both sides of a double equal.
        # Double equal will always result True or False.
        return True
    else:
        return False


print(same_name("Colby", "Colby"))
print(same_name("Tina", "Amber"))
