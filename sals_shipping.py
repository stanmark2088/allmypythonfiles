# FREEFORM PROJECT (CALCULATING COSTS/GROUND/DRONE/BEST PRICE)


def shipping_cost_ground(weight):
    if weight <= 2:
        price_per_pound = 1.50
    elif weight <= 6:
        price_per_pound = 3.00
    elif weight <= 10:
        price_per_pound = 4.00
    else:
        price_per_pound = 4.75
    return 20 + (price_per_pound * weight)


print(shipping_cost_ground(8.4))

shipping_cost_premium = 125.00


def shipping_cost_drone(weight):

    if weight <= 2:
        price_per_pound = 4.50
    elif weight <= 6:
        price_per_pound = 9.00
    elif weight <= 10:
        price_per_pound = 12.00
    else:
        price_per_pound = 14.25
    return price_per_pound * weight


print(shipping_cost_drone(10))

# ii spunem print_cheapest_shipping_method pt ca func asta nu va returna nimic doar
# va printa care ii cea mai ieftina metoda( asta e pt noi sa stim ce face dar o putem numi
# cum vrem noi)


def print_cheapest_shipping_method(weight):

    ground = shipping_cost_ground(weight)
    premium = shipping_cost_premium
    # pretul este 125 intotdeauna , ii o variabila
    drone = shipping_cost_drone(weight)


if ground < drone and ground < premium:
    method = "standard ground"
    cost = ground
elif premium < ground and premiun < drone:
    method = "standard premium"
    cost = premium
else:
    method = "standard drone"
    cost = drone

    # .2f la final inseamna ca va printa un nr care are 2 decimale ca si float.
    #  punand paranteza de la print la inceput si final pe randuri diferite ne lasa
    # sa inseram si valorile in string

    print(
        "the cheapest value is $%.2f with %s shipping"
        % (cost, method)
    )

print(print_cheapest_shipping_method(4.8))
print(print_cheapest_shipping_method(41.5))
