numbers = [-5, 23, 0, -9, 12, 99, 105, -43]

n = len(numbers)
max = numbers[0]
min = numbers[0]


i = 1

while (i < n):
    if numbers[i] > max:
        max = numbers[i]
    if numbers[1] < min:
        min = numbers[i]

    i = i + 1
"""
suma = 0
suma = suma + numbers[0] = 0 + (-5) = -5
suma = suma + numbers[1] = -5 + 23 = 18
suma = suma + numebr[2] = 18 + 0 = 18\




uma = suma + numebr[7] =
"""

suma = 0

i = 0
while (i < n):
    suma = suma + numbers[i]
    i = i + 1
    print(suma)

print(".........................................")
print("suma cu while este " + str(suma))
print(".........................................")

suma = 0
# produs = 1 pt produs . 0 inmultit cu orice nr da 0
for i in range(0, n):
    print(i)
    suma = suma + numbers[i]
    #produs = produs * numbers[i]
    print(suma)

print(".........................................")
print("suma cu for este " + str(suma))
print(".........................................")

# suma = numbers [0] + numbers [1] + numbers [2] + numbers [3] +      + numbers [7]
average = suma / n


(max)
print(min)
print(average)
