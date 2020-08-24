class Parent:
    def __init__(self):
        self._protected_variable = 2
        self.__private_variable = 2
        self.public_variable = 2
        self.__pan_number = "ICRPG5612A"

    def get_pan_number(self):
        return self.__pan_number

    def print_pan_number(self):
        print(self.__pan_number)


p = Parent()
print(p.get_pan_number())
p.__pan_number = 10
print(p.__pan_number())

# getters and setters
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#
#     def print_values(self):
#         print(self._protected_variable)
#         print(self.__private_variable)
#         print(self.public_variable)


# p = Child()
# p.__private_variable = 10
# print(p.print_values())


# child.print_pan_number()
# child.pan_number = "hacked"
# child.print_pan_number()



# getters and setters
