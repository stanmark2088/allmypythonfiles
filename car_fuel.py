PETROL_PRICE_PER_LITRE = 5.55  # written in caps because it's a constant
print("*** Welcome to the fuel efficiency calculator!\n")
# we add an extra blank line after the message with \n
name = input("Enter your name: ")
# float is a function which converts values to floating-point numbers.
distance_travelled = float(input("Enter distance travelled in km: "))3
amount_paid = float(input("Enter monetary value of fuel bought for the trip: ron"))
fuel_consumed = amount_paid / PETROL_PRICE_PER_LITRE
efficiency_l_per_100_km = fuel_consumed / distance_travelled * 100
efficiency_km_per_l = distance_travelled / fuel_consumed
print("Hi, %s!" % name)
print("Your car's efficiency is %.2f litres per 100 km." %
      efficiency_l_per_100_km)
print("This means that you can travel %.2f km on a litre of petrol." %
      efficiency_km_per_l)
# we add an extra blank line before the message with \n
print("\nThanks for using the program.")
