'''
#       Day 1: Business Class (3rd semester?)
#       Andrés Rodríguez Cantú ─ A01287002
#
#       Copyright (C) Tecnológico de Monterrey
#
#       File: main.py
#
#       Created:                08/22/2025
#       Last Modified:          08/22/2025
'''
class Main:
    def __init__(self):
        pass

class A:
    def printA(self):
        print("This is class A")

class B:
    def printB(self):
        print("This is class B")

class C:
    def printC(self):
        print("This is class C")

class D:
    def printD(self):
        print("This is class D")

class E:
    def printE(self):
        print("This is class E")


if __name__ == "__main__":
    # Create instances of all classes except Main
    instances = {
        name.lower(): cls()
        for name, cls in globals().items()
        if isinstance(cls, type) and name not in ["Main"]
    }

    # Optionally inject them into local/global namespace
    globals().update(instances)

    main = Main()

    # Now you can use them directly as variables
    a.printA()
    b.printB()
    c.printC()
    d.printD()
    e.printE()
