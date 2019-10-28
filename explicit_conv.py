# this is for integers!
import math
i = math.ceil(6.342)
print(i)
a = math.floor(7.986)
print(a)
b = round(5.499)
print(b)
# output
# ceil rounds up so 7
# floor rounds down so 7
# round rounds to closest no. so 5

# this is for strings

# concatenate
print("3%d" % 4)
print("3" + str(4))

# exerciti


# 1.Convert "8.8" to a float.
# 2.Convert 8.8 to an integer (with rounding).
# 3.Convert "8.8" to an integer (with rounding).
# 4.Convert 8.8 to a string.
# 5.Convert 8 to a string.
# 6.Convert 8 to a float.
# 7.Convert 8 to a boolean.

a_1 = float("8.8")
a_2 = math.round(8.8)
a_3 = math.round("8.8")
a_4 = "%g" % 8.8
a_5 = "%d" % 8
a_6 = float(8)
a_7 = bool(8)
