# FREEFORM PROJECT LEN'S PIZZA

# You work at Len’s Slice, a new pizza joint in the neighborhood.
# You are going to use your knowledge of Python lists to organize some
# f your sales data.
# If you get stuck during this project or would like to see an experienced
# developer work through it, click “Get Help“ to see a project walkthrough video.

toppings = ["pepperoni", "pineapple", "cheese",
            "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")
pizzas = list(zip(prices, toppings))
print(pizzas)
pizzas.sort()
print(pizzas)
cheapest_pizza = pizzas[0]
print(cheapest_pizza)
priciest_pizza = pizzas[-1]
print(priciest_pizza)
three_cheapest = pizzas[:3]
print(three_cheapest)
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
