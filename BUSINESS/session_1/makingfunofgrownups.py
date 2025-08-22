'''
#       Day 1: Business Class (3rd semester?)
#       Andrés Rodríguez Cantú ─ A01287002
#
#       Copyright (C) Tecnológico de Monterrey
#
#       File: makingfunofgrownups.py
#
#       Created:                08/22/2025
#       Last Modified:          08/22/2025
'''
class Problems():
    def __init__(self):
        methods = [func for func in dir(self) if callable(getattr(self, func)) and func.startswith('problem')]
        self.lowerbound = 1
        self.upperbound = len(methods)

    def problem1(self):
        self.x = 17
        if self.x < 20:
            print("x is less than 20")

    def problem2(self):
        self.prendido = 1
        if self.prendido:
            print("La llave esta abierta")

    def problem3(self):
        self.a = 5
        self.b = 7
        if self.a < self.b:
            print("Verdadero")

    def problem4(self):
        self.age = int(input("Introduce tu edad: "))
        if self.age >= 18:
            print("Eres mayor de edad")
        else:
            print("Eres menor de edad")

    def problem5(self):
        self.key = "contraseña"
        self.password = input("Introduce la contraseña: ")
        if self.password == self.key:
            print("Acceso concedido")
        else:
            print("Acceso denegado")
    
    def problem6(self):
        self.income = float(input("Introduce tu ingreso: "))
        if self.income < 10000:
            self.tax = 5
        elif self.income < 20000:
            self.tax = 15
        elif self.income < 35000:
            self.tax = 20
        elif self.income < 60000:
            self.tax = 25
        else:
            self.tax = 40
        print(f"Tu impuesto es: {self.tax}%")

    def problem7(self):
        self.name = input("Introduce tu nombre: ")
        self.gender = input("Introduce tu género (M/F): ").upper()
        if self.gender == "M":
            if self.name.lower() < "m":
                self.group = "A"
            else:
                self.group = "B"
        elif self.gender == "F":
            if self.name.lower() < "m":
                self.group = "C"
            else:
                self.group = "D"
        print(f"Grupo asignado: {self.group}")

    def index(self):
        __index = int(input(f"Pon el número del ejercicio (Entre el {self.lowerbound} y el {self.upperbound}): "))
        __list = []
        for i in range(self.lowerbound, self.upperbound + 1):
            method = getattr(self, f"problem{i}", None)
            if method:
                __list.append(method)
        if 1 <= __index <= len(__list):
            __list[__index - 1]()
        else:
            print("Índice fuera de rango\n")

if __name__ == "__main__":
    problems = Problems()
    problems.index()
