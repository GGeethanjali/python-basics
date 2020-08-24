class Car:
    #     def __init__(self):
    #         print ("Engine started")
    #         self.name = "corolla"
    #         self.__make = "toyota"
    #         self._model = 1999

    def display_values(self, name):
        print("hey", name)


c = Car()
# print(c.name)
# print(c._model)
# print(c.__make)
c.display_values("anju")


class Audi(Car):
    def display_dimensions(self):
        self.display_values("inside child")


a = Audi()
# a.display_values("ciao")
a.display_dimensions()
