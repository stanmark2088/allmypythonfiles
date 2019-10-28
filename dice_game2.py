import random

while True:
    try:  # cand input() primeste
        attacker_units = int(input("How many units attack: "))
    except ValueError:
        attacker_units = -1
    if attacker_units > 0 and attacker_units <= 3:
        break

while True:
    try:
        defender_units = int(input("How many units defend: "))
    except ValueError:
        defender_units = -1
    if defender_units > 0 and defender_units < 3:
        break

# daca attacker_units e 3 atunci rezultatul va fi [None, None, None]
attacker = [None] * attacker_units
defender = [None] * defender_units
# acum avem arrayurile, sa punem numere aleatoare in ele, in loc de "None"
for i in range(len(attacker)):
    attacker[i] = random.randrange(1, 6)

for i in range(len(defender)):
    defender[i] = random.randrange(1, 6)

attacker.sort()
defender.sort()

attacker_lost = 0
defender_lost = 0

for i in range(0, 2):
    if attacker[i] > defender[i]:
        defender_lost = defender_lost + 1
    else:
        attacker_lost = attacker_lost + 1

print("Dice:")
print("Attacker: ", attacker)
print("Defender:", defender)
print("Outcome:")
print("Attacker lost", attacker_lost, "unit", end="")
if attacker_lost == 0 or attacker_lost > 1:
    print("s")  # s followed by newline
else:
    print("")  # newline

print("Defender lost", defender_lost, "unit", end="")
if defender_lost == 0 or defender_lost > 1:
    print("s")  # s followed by newline
else:
    print("")  # newline
