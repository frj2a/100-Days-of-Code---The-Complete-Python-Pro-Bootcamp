
# def add(*args):
#     result = 0
#     for arg in args:
#         result += arg
#     return result
#
# print(add(3, 4, 5, 6, 7))


# def calculate(n, **kwargs):
#     # print(type(kwargs))
#     # print(kwargs)
#     # for (key, value) in kwargs.items():
#     #     print(key, value)
#     # print(kwargs["add"])
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
# calculate(2, add=3, multiply=5)


# class Car:
#
#     def __init__(self, **kwargs):
#         self.make = kwargs["make"]
#         self.model = kwargs["model"]
#
# my_car = Car(make="Nissan", model="GT-R")
# print(my_car.make, my_car.model)



class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.make, my_car.model, my_car.color, my_car.seats)
