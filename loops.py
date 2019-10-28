# 1.For loops

board_games = ['Settlers of Catan', 'Carcassone',
               'Power Grid', 'Agricola', 'Scrabble']

sport_games = ['football', 'football - American',
               'hockey', 'baseball', 'cricket']

for game in board_games:
    print(game)
# output : 'Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble'
for sport in sport_games:
    print(sport)
# output : 'football', 'football - American', 'hockey', 'baseball', 'cricket'

# 2. Using range in loops

promise = "I will not chew gum in class"

for i in range(0, 6):
    print(promise)
# output : I will not chew gum in class
# I will not chew gum in class
# I will not chew gum in class
# I will not chew gum in class
# I will not chew gum in class
# I will not chew gum in class

iris = "diseara..."

for x in range(0, 11):
    print(iris)
# output :
# diseara ...
# diseara ...
# diseara ...
# diseara ...
# diseara ...
# diseara ...
# diseara ...
# diseara ...
# diseara ...
# diseara ...
# diseara ...

# 3. Infinite Loops

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
    # students_period_A.append(student) this will be an infinite loop
    students_period_B.append(student)
    print(student)

    # outout:Alex Briana Cheri Daniele

# 4. Break

items_on_sale = ["blue_shirt", "striped_socks",
                 "knit_dress", "red_headband", "dinosaur_onesie"]

print("Checking the sale list!")
for item in items_on_sale:
    print(item)
    if item == "red_headband":  # it stops at knit dress because this is what we were searcing for
        break
print("End of search!")

# output =
# Checking the sale list!
# blue_shirt
# striped_socks
# knit_dress
# End of search!

dog_breeds_available_for_adoption = [
    'french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    if dog_breed == dog_breed_I_want:
        print("They have the dog I want!")
        break

# check output

# 5. Break

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
    if i < 21:
        continue
    print(i)

# 6. While loops

dog_breeds = ['bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']

index = 0
while index < len(dog_breeds):
    print(dog_breeds[index])
    index += 1

# exemplu 2

all_students = ["Alex", "Briana", "Cheri", "Daniele",
                "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
    student = all_students.pop()
    students_in_poetry.append(student)

print(students_in_poetry)

# 7. Nested Loops

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
    print(location)
    for element in location:
        scoops_sold += element

print(scoops_sold)

# 8. List comprehension

# printeaza numai anumite lucruri din lista

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = []

for height in heights:
    if height > 161:
        can_ride_coaster.append(height)
        print(can_ride_coaster)

# 9. More List Comprehension

# change celsius to fahrenheit using loops

celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [celsius_value * 9/5 + 32 for celsius_value in celsius]
print(fahrenheit)


# final exercise

ingle_digits = range(10)
squares = []

for item in single_digits:
    print(item)
    squares.append(item**2)

cubes = [item**3 for item in single_digits]
print(cubes)
