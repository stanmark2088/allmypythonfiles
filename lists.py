# 1.Zip

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

# combina numele cu numele cainilor
names_and_dogs_names = zip(names, dogs_names)
# formand o pereche in functie de unde stau in list 1 cu 1 2 cu 2 etc ====uita=te la output
list_of_names_and_dogs_names = list(names_and_dogs_names)

print(list_of_names_and_dogs_names)

# 2. Append

# append = adds an elem to the list if empty
#   = if list exists , it adds an elem to the end of the list

orders = ["daisies", "periwinkle"]
print(orders)
orders.append("tulips")
print(orders)
orders.append("roses")
print(orders)

# 3.Range

# generates a list of no. instead of having to write all of them

my_range = range(10)
print(my_range)  # printeaza range (0,10)
print(list(my_range))  # printeaza [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# se pot face liste cu 2 arg sau cu 3 . cele cu 3 sar peste numerele din x in x in functie
# de cat e ultimul numar
my_range2 = range(2, 9, 2)
print(list(my_range2))
# [2, 4, 6, 8] asta e output-ul

# alt exepmplu
my_range3 = range(1, 100, 10)
print(list(my_range3))
# [1, 11, 21, 31, 41, 51, 61, 71, 81, 91] asta e output-ul

# exemplu putin mai dificil

first_names = ["Ainsley", "Ben", "Chani", "Depak"]
age = []
age.append(42)
print(list(age))
all_ages = age + [32, 41, 29]
print(list(all_ages))
name_and_age = zip(first_names, all_ages)
print(list(name_and_age))
ids = range(0, 4)

# output-ul este
# [42]
# [42, 32, 41, 29]
# [('Ainsley', 42), ('Ben', 32), ('Chani', 41), ('Depak', 29)]


# 4. Len

# Often, we’ll need to find the number of items in a list, usually called its length.
# We can do this using the function len. When we apply len to a list, we get the number
#  of elements in that list:

my_list = [1, 2, 3, 4, 5]
print(len(my_list))

# output = 5

# exercitiu 1

list1 = range(2, 20, 2)
list1_len = len(list1)
print(list1_len)
# output 9
list1 = range(2, 20, 3)
list1_len = len(list1)
print(list1_len)
# out put 6 pt ca am schimbat ultimul argument din 2 in 3

# 5. Selecting List Elements

# Chris is interviewing candidates for a job. He will call each candidate in order,
# represented by a Python list:
# calls = ['Ali', 'Bob', 'Cam', 'Doug', 'Ellie']
# First, he’ll call 'Ali', then 'Bob', etc.
# In Python, we call the order of an element in a list its index.
# Python lists are zero-indexed. This means that the first element in a list has index 0,
# rather than 1.


employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']
index4 = employees[4]
print(employees[4])
print(index4)
print(len(employees))
print(employees[6])
# Ryan
# Ryan
# output 7
# output Robert

# 6.Selecting List Elements II

# What if we want to select the last element of a list?
# We can use the index -1 to select the last item of a list, even when we don’t know how many elements are in a list.
# Consider the following list with 5 elements:
# list1 = ['a', 'b', 'c', 'd', 'e']
# If we select the -1 element, we get the final element, 'e':
#  print(list1[-1]) output = 'e'
# This is the same as selecting the element with index 4:
#  print(list1[4]) output = 'e'

# exercitiu

shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']
print(len(shopping_list))
last_element = shopping_list[-1]
print(last_element)
element5 = 'cereal'
print(element5)
# output
# 6
# cereal
# cereal

# 7.Slicing Lists

# Suppose we have a list of letters:
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# Suppose we want to select from b through f.
# e can do this using the following syntax: letters[start:end], where:
# start is the index of the first element that we want to include in our selection.
# In this case, we want to start at b, which has index 1.
# end is the index of one more than the last index that we want to include. The last
# element we want is f, which has index 5, so end needs to be 6.
# sublist = letters[1:6]
# print(sublist)
# This example would yield:
# ['b', 'c', 'd', 'e', 'f']
# Notice that the element at index 6 (which is g) is not included in our selection.
# Creating a selection from a list is called slicing.

# exercise

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

beginning = suitcase[0:4]
print(beginning)
middle = suitcase[2:4]
print(middle)
# output
# ['shirt', 'shirt', 'pants', 'pants']
# ['pants', 'pants']


# 8. Slicing Lists 2
# If we want to select the first 3 elements of a list, we could use the following code:
# >>> fruits = ['apple', 'banana', 'cherry', 'date']
# >>> print(fruits[0:3])
# ['apple', 'banana', 'cherry']
# When starting at the beginning of the list, it is also valid to omit the 0:
# >>> print(fruits[:3])
# ['apple', 'banana', 'cherry']
# We can do something similar when selecting the last few items of a list:
# >>> print(fruits[2:])
# ['cherry' , 'date']
# We can omit the final index when selecting the final elements from a list.
# If we want to select the last 3 elements of fruits, we can also use this syntax:
# >>> print(fruits[-3:])
# ['banana', 'cherry', 'date']
# We can use negative indexes to count backward from the last element.

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

print(suitcase[:3])
print(suitcase[0:3])
print(suitcase[4:])
print(suitcase[4:6])
print(suitcase[-3:])
# output
# ['shirt', 'shirt', 'pants']
# ['shirt', 'shirt', 'pants']
# ['pajamas', 'books']
# ['pajamas', 'books']
# ['pants', 'pajamas', 'books']

# 9. Counting
#
# Suppose we have a list called letters that represents the letters in the word
#  “Mississippi”:
# letters = ['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
# If we want to know how many times i appears in this word, we can use the
# function count:
#
# num_i = letters.count('i')
# print(num_i)
# This would print out: 4

# exercitiu

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake',
         'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake',
         'Jake', 'Cassie', 'Laurie']

jake_votes = votes.count('Jake')
print(jake_votes)
# output = 9

# 10. Sorting Lists 1
# Sometimes, we want to sort a list in either numerical (1, 2, 3, …) or
# alphabetical (a, b, c, …) order.
# We can sort a list in place using .sort(). Suppose that we have a list of names:
# names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
# print(names)
# This would print:
# ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
# Now we apply .sort():
# names.sort()
# print(names)
# And we get:
# ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
# Notice that sort goes after our list, names. If we try sort(names), we will get
# a NameError.
# sort does not return anything. So, if we try to assign names.sort() to a variable,
# our new variable would be None:
# sorted_names = names.sort()
# print(sorted_names)
# This prints:
# None
# Although sorted_names is None, the line sorted_names = names.sort() still edited names:
# >>> print(names)
# ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']

# exercitiu

addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place',
 '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
]
addresses.sort()
print(addresses)
# output:['10 Downing St.', '12 Grimmauld Place', '1600 Pennsylvania Ave',
#  '221 B Baker St.', '42 Wallaby Way', '742 Evergreen Terrace'

names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']

names.sort()
print(names)
# output = ['Albus', 'Harry', 'Hermione', 'Ron', 'Sirius']

cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']
# wrong because sort does not return anything. So, if we try to assign cities.sort() to a variable, our new variable would be None:
sorted_cities = cities.sort()
print(sorted_cities)
# output = None

cities.sort()
print(cities)
# output = ['London', 'Los Angeles', 'New York', 'Paris', 'Rome']

# 11. Sorting Lists 2

# A second way of sorting a list is to use sorted. sorted is different from .sort()
# in several ways:
# It comes before a list, instead of after.
# It generates a new list.
# Let’s return to our list of names:
# names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
# Using sorted, we can create a new list, called sorted_names:
# sorted_names = sorted(names)
# print(sorted_names)
# this yields the list sorted alphabetically:
# ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
# Note that using sorted did not change names:
# >>> print(names)
# ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']

# exercitii

games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

games_sorted = sorted(games)
print(games_sorted)
# output ['Minecraft', 'Pacman', 'Pokemon', 'Portal', 'Tetris', 'The Sims']
print(games)
# output ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

# both lists remain
# the game_sorted list is sorted alphabetically
# the game list remains the way it was


# FINAL EXERCISE WITH ALMOST EVERYTHING WE LEARNED

inventory= ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser',
'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed',
'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

inventory_len = len(inventory)
print(inventory_len)
# output: 19

first = inventory[0]
print(first)
# output: twin bed

last = inventory[-1]
print(last)
# output: pillow

inventory_2_6 = inventory[2: 6]
print(inventory_2_6)
# output : ['headboard', 'queen bed', 'king bed', 'dresser']

first_3 = inventory[: 3]
print(first_3)
# output : ['twin bed', 'twin bed', 'headboard']

twin_beds = inventory.count('twin bed')
print(twin_beds)
# output : 4

inventory.sort()
print(inventory)
# output : ['dresser', 'dresser', 'headboard', 'king bed', 'king bed', 'king bed', 'nightstand', 'nightstand', 'pillow', 'pillow', 'queen bed', 'sheets', 'sheets', 'table', 'table', 'twin bed', 'twin bed', 'twin bed', 'twin bed']
