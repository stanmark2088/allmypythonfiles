# 1.Create a list a which contains the first three odd positive integers and a list b which contains
#  the first three even positive integers.
# 2.Create a new list c which combines the numbers from both lists (order is unimportant).
# 3.Create a new list d which is a sorted copy of c, leaving c unchanged.
# 4.Reverse d in-place.
# 5.Set the fourth element of c to 42.
# 6.Append 10 to the end of d.
# 7.Append 7, 8 and 9 to the end of c.
# 8.Print the first three elements of c.
# 9.Print the last element of d without using its length.
# 10.Print the length of d.

# exrcise 1
a = [2, 4, 6]
b = [1, 3, 5]
# exercise 2
c = a + b
print(c)
# exercise 3
d = sorted(c)
print(d)
# exercise 4
d.reverse()
print(d)
# exercise 5
c[3] = 42
print(c)
# exercise 6
d.append(10)
print(d)
# exercise 7
c.extend([7, 8, 9])
print(c)
# exercise 8
print(c[:3])
print(c)
# exercise 9
print(d[-1])
print(d)
# exercise 10
print(len(d))
del d[2]
print(d)

# 1.Create a tuple a which contains the first four positive integers and a tuple b which
# contains the next four positive integers.
# 2.Create a tuple c which combines all the numbers from a and b in any order.
# 3.Create a tuple d which is a sorted copy of c.
# 4.Print the third element of d.
# 5.Print the last three elements of d without using its length.
# 6.Print the length of d.

# exercise 1
a = (1, 2, 3, 4)
b = (5, 6, 7, 8)
# exercise 2
c = a + b
print(c)
# exercise 3
d = sorted(c)
print(d)
# exercise 4
print(d[3])
# exercise 5
print(d[-3:])
# exercise 6
print(len(d))

# 1.Create a set a which contains the first four positive integers and a set b which contains
# the first four odd positive integers.
# 2.Create a set c which combines all the numbers which are in a or b (or both).
# 3.Create a set d which contains all the numbers in a but not in b.
# 4.Create a set e which contains all the numbers in b but not in a.
# 5.Create a set f which contains all the numbers which are both in a and in b.
# 6.Create a set g which contains all the numbers which are either in a or in b but not in both.
# 7.Print the number of elements in c.

# exercise 1
a = {1, 2, 3, 4}
b = {1, 3, 5, 7}
# exercise 2
c = set(a | b)
print(c)
# exercise 3
d = (a - b)
print(d)
# exercise 4
e = (b - a)
print(e)
# exercise 5
f = (a & b)
print(f)
# exercise 6
g = (a ^ b)
print(g)
# exercise 7
print(len(c))

# 1.Create a range a which starts from 0 and goes on for 20 numbers.
# 2.Create a range b which starts from 3 and ends on 12.
# 3.Create a range c which contains every third integer starting from 2 and ending at 50.

# exercise 1
a = range(0, 20)
print(list(a))
# exercise 2
b = range(3, 13)
print(list(b))
# exercise 4
c = range(2, 51, 3)
print(list(c))

# 1.Create a dict directory which stores telephone numbers (as string values), and populate it with
# these key-value pairs:

# Name	Telephone number
# Jane Doe	+27 555 5367
# John Smith	+27 555 6254
# Bob Stone + 27 555 5689
# 2.Change Jane’s number to +27 555 10243.
# 3.Add a new entry for a person called Anna Cooper with the phone number +27 555 3237
# 4.Print Bob’s number.
# 5.Print Bob’s number in such a way that None would be printed if Bob’s name were not in the dictionary.
# 6.Print all the keys. The format is unimportant, as long as they’re all visible.
# 7.Print all the values.

# exercise 1
tel_no = {"Jane Doe": "+27 555 5367",
          "John Smith": "+27 555 6254", "Bob Stone": "+27 555 5689", }
# exercise 2
tel_no["Jane Doe"] = "+27 555 10243"
# exercise 3
tel_no["Anna Cooper"] = "+27 555 3237"
# exercise 4
print(tel_no["Bob Stone"])
# exercise 5
print(tel_no.get("Bob Stone", None))
# exercise 6
print(tel_no.keys())
# exercise 7
print(tel_no.values())

