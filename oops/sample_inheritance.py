# class BaseClass:
#   Body of base class
# class DerivedClass(BaseClass):
#   Body of derived class

class GrandParent:
    def __init__(self):
        print("inside grandparent constructor")
        self.firstname = "abc"
        self.lastname = "xyz"

    def printname(self):
        print("grandd parent")

class Parent(GrandParent):
    def __init__(self):
        print("inside parent constructor")
        super().__init__()
        self.firstname = "abc"
        self.lastname = "xyz"

    def printname(self):
        print("byeeeee")


def display_details(gp):
    gp.printname()


a = Parent()

display_details(a)
