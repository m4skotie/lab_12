def  z1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name}, Кухня:{self.cuisine_type}")
        def open_restaurant(self):
            print("Ресторан сейчас открыт.")

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors
        def show_flavors(self):
            print(f"Сорта мороженого в наличии: {self.flavors}")
    newRestaurant = IceCreamStand("Морожка", "Вкусная", ["Клубничный", "Шоколадный"])
    newRestaurant.show_flavors()
def z2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name}, Кухня:{self.cuisine_type}")
        def open_restaurant(self):
            print("Ресторан сейчас открыт.")

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors, position, worktime):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors
        def show_flavors(self):
            print(f"Сорта мороженого в наличии: {self.flavors}")
        def add_flavor(self, new_flavor):
            if new_flavor not in self.flavors:
                self.flavors.append(new_flavor)
        def remove_flavor(self, flavor_to_remove):
            if flavor_to_remove in self.flavors:
                self.flavors.remove(flavor_to_remove)
        def check_flavor(self, flavor_to_check):
            if flavor_to_check in self.flavors:
                print(f"Сорт '{flavor_to_check}' в наличии.")
            else:
                print(f"Сорт '{flavor_to_check}' не в наличии.")
    class IceCreamStick(IceCreamStand):
        def stick_ice_cream(self):
            print("Вы выбрали мороженое на палочке")
    class SoftIceCream(IceCreamStand):
        def soft_ice_cream(self):
            print("Вы выбрали мягкое мороженое")

    newRestaurant = IceCreamStand("Морожка", "Вкусная", ["Клубничный", "Шоколадный"], "Казанская улица, д. 39", "9:00 - 20:00")
    newRestaurant.show_flavors()
    newRestaurant.add_flavor(input("Какой сорт мороженого добавить? "))
    newRestaurant.show_flavors()
    newRestaurant.remove_flavor(input("Какой сорт мороженого убрать? "))
    newRestaurant.show_flavors()
    newRestaurant.check_flavor(input("Какой сорт мороженого проверить? "))

    newRestaurant1= IceCreamStick("Морожка", "Вкусная", ["Клубничный", "Шоколадный"], "Казанская улица, д. 39", "9:00 - 20:00")
    newRestaurant1.stick_ice_cream()
    newRestaurant2 = SoftIceCream("Морожка", "Вкусная", ["Клубничный", "Шоколадный"], "Казанская улица, д. 39", "9:00 - 20:00")
    newRestaurant2.soft_ice_cream()

z2()