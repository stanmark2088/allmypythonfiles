import sys

vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "v", "x", "y", "z"]
found_vowels = []
found_consonants = []
word = str(input("Write your word here: "))
if word.isnumeric():
    sys.exit("Please input a string!")

def alphabet_filter(word):
    for letter in word:
        if letter.isnumeric():
            continue
        if letter in vowels:
            found_vowels.append(letter)
        else:
            found_consonants.append(letter)
    return found_vowels, found_consonants        

print(alphabet_filter(word))
