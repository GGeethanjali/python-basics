from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        print("Some implementation!")

    def display_values(self):
        pass

    def walk(self):
        pass

    def jump(self):
        pass


class Dog(Animal):

    def __init__(self):
        self.name = 'dog'


    def make_sound(self):
        super().make_sound()
        print("I bark")


class Human(Animal):

    def make_sound(self):
        super().make_sound()
        print("I talk")


x = Animal()
x.make_sound()


# class Phone:
#     def __init__(self):
#         self.name = 'abc'
#
#     def switch_off(self):
#         pass
#
#
# class OnePlus(Phone):
#     def switch_off(self):
#         pass
#
#
# class iPhone(Phone):
#     def switch_off(self):
#         pass

# class Parent:
#     def __init__(self):
#         self.name = 'abc'
#         self.age = 25
#         self.spouse_name = 'xyz'
#
#
#     def display_parent_name_with_spouse_name(self):
#         self.__replace_letters()
#
#     def __replace_letters(self):
#         pass
#
#
# p = Parent()
# p.display_parent_name_with_spouse_name()

# what is abstraction
# why abstraction
# how abstraction can be achieved
# what are abstract classes
# difference between class and abstract class
# how abstract classes help in data hiding (cannot instantiate base class)
# difference between subclassing and abstract class
