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

# class Parent1:
#     def __init__(self):
#         print("inside parent1 constructor")
#         # super().__init__("hey", "hello")
#
#     def printname(self):
#         print("byeeeee")
#
# class Child(Parent, Parent1): #left -> right, depth first
#     def __init__(self):
#         print("inside child constructor")
#         Parent.__init__(self)
#         Parent1.__init__(self)

a = Child()
a.printname()

# reuse, add func, override func
