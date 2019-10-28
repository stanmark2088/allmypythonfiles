# Write a Python program to convert a temperature given in degrees Fahrenheit
# to its equivalent in degrees Celsius. You can assume that T_c = (5/9) x (T_f - 32),
#  where T_c is the temperature in °C and T_f is the temperature in °F. Your program
# should ask the user for an input value, and print the output. The input and output
# values should be floating-point numbers.

# my version
print("\nWelcome to the fahrenheit to celsius calculator!\n")
name = input("Please tell us your name: ")
print("\nHello " + str(name) + "!")
fahrenheit_temperature = float(
    input("\nPlease enter Fahrenheit temperature: "))
print("\nThe temperature in Celsius is:")
celsius_temperature = (5 / 9) * (fahrenheit_temperature - 32)
print(celsius_temperature)
print(("\nThank you for using our calculator ") + str(name) + "!")

# their version
T_f = float(input("Please enter a temperature in °F: "))
T_c = (5/9) * (T_f - 32)
print("%g°F = %g°C" % (T_f, T_c))
