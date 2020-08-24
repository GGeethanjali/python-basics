class Topping:
    def __init__(self, name, price_per_serving):
        self.name = name
        self.price_per_serving = price_per_serving


class Flavour:
    def __init__(self, name, price_per_scoop, is_topping_allowed):
        self.name = name
        self.price_per_scoop = price_per_scoop
        self.is_topping_allowed = is_topping_allowed


class IceCreamType:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class IceCream(object):
    def __init__(self, flavour, type, quantity, topping):
        self.__iceCreamType = type
        self.__flavour = flavour
        self.__topping = topping
        self.__quantity = quantity

    def calculate_total_cost(self):
        cost = (self.__flavour.price_per_scoop + self.__iceCreamType.price ) * float(self.__quantity)
        if self.__topping is None:
            return cost
        return cost + self.__topping.price_per_serving


def display_ice_cream_options():
    for flavour in flavours:
        for type in ice_cream_types:
            print(flavour.name,
                  type.name + " - " + str(calculate_total_per_serving(flavour.price_per_scoop, type.price)))


def calculate_total_per_serving(flavour_price, type_price):
    return flavour_price + type_price


def filter_flavour(selected_flavour_name):
    filtered_flavour = next((flavour for flavour in flavours if flavour.name.lower() == selected_flavour_name),
                            None)
    return filtered_flavour


def filter_type(selected_type_name):
    filtered_type = next((type for type in ice_cream_types if type.name.lower() == selected_type_name), None)
    return filtered_type


def filter_topping(topping_name):
    filtered_topping = next((topping for topping in toppings if topping.name.lower() == topping_name), None)
    return filtered_topping


def get_user_preference():
    while True:
        selected_flavour_name = input("select your preferred flavour: ").lower()
        selected_flavour = filter_flavour(selected_flavour_name)
        if selected_flavour is None:
            print("Not a valid choice.")
        else:
            break

    while True:
        selected_type_name = input("select your preferred type: ").lower()
        selected_type = filter_type(selected_type_name)
        if selected_type is None:
            print("Not a valid choice.")
        else:
            break

    quantity = input("enter the quantity: ")

    if selected_flavour.is_topping_allowed:
        display_toppings()
        is_topping_needed = input("do you want toppings?")
        if is_topping_needed == 'yes':
            while True:
                selected_topping_name = input("select your preferred topping: ").lower()
                selected_topping = filter_topping(selected_topping_name)
                if selected_topping is None:
                    print("Not a valid choice.")
                else:
                    break
        else:
            selected_topping = None
    else:
        selected_topping = None

    return selected_flavour, selected_type, quantity, selected_topping


def display_toppings():
    for topping in toppings:
        print(topping.name + " - " + str(topping.price_per_serving))


type1 = IceCreamType("Cone", 25)
type2 = IceCreamType("Stick", 15)
ice_cream_types = [type1, type2]

flavour1 = Flavour("Vanilla", 25, False)
flavour2 = Flavour("Mango", 30, False)
flavour3 = Flavour("Chocolate", 35, True)
flavours = [flavour1, flavour2, flavour3]

topping1 = Topping("Caramel", 10)
topping2 = Topping("Choco chips", 15)
toppings = [topping1, topping2]

display_ice_cream_options()
(selected_flavour, selected_type, quantity, selected_topping) = (get_user_preference())

ice_cream = IceCream(selected_flavour, selected_type, quantity, selected_topping)
print(ice_cream.calculate_total_cost())
