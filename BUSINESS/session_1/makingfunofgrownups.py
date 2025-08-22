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
# Se que el código es terrible, pero era para hacer todos los problemas en un solo archivo, de maneras no convencionales para que mis compañeros no me puedan copiar

class Problems():
    def __init__(self):
        methods = [func for func in dir(self) if callable(getattr(self, func)) and func.startswith('problem')]
        self.lowerbound = 1
        self.upperbound = len(methods)

    def problem1(self):
        def pideColores():
            colores = {}
            for i in range(2):
                colores[f"color_{i+1}"] = str(input(f"Introduce el color {i+1}: "))
            return colores

        def muestraColores(colores):
            for i in range(2):
                print(f"Color {i+1}: {colores[f'color_{i+1}']}")

        def mezclaColores(colores):
            color1 = colores.get("color_1", "").lower()
            color2 = colores.get("color_2", "").lower()
            if {"rojo", "azul"} == {color1, color2}:
                print("La mezcla es morado.")
            elif {"rojo", "amarillo"} == {color1, color2}:
                print("La mezcla es naranja.")
            elif {"azul", "amarillo"} == {color1, color2}:
                print("La mezcla es verde.")
            elif color1 == color2:
                print(f"La mezcla es {color1}.")
            else:
                print("No conozco esa mezcla.")

        colores = pideColores()
        muestraColores(colores)
        mezclaColores(colores)

    def problem2(self):
        def menu():
            print("Este menu es para ver que figura quieres sacar el area:")
            lista = ["Cuadrado", "Rectángulo", "Círculo", "Triángulo", "Trapecio"]
            for i, figura in enumerate(lista, 1):
                print(f"{i}. {figura}")
            opcion = input("Selecciona una opción: ")
            return opcion

        def area():
            figura = menu()
            if figura == "Cuadrado":
                lado = float(input("Introduce el lado del cuadrado: "))
                area = lado ** 2
                print(f"El área del cuadrado es: {area}")
            elif figura == "Rectángulo":
                base = float(input("Introduce la base del rectángulo: "))
                altura = float(input("Introduce la altura del rectángulo: "))
                area = base * altura
                print(f"El área del rectángulo es: {area}")
            elif figura == "Círculo":
                radio = float(input("Introduce el radio del círculo: "))
                area = 3.14159 * radio ** 2
                print(f"El área del círculo es: {area}")
            elif figura == "Triángulo":
                base = float(input("Introduce la base del triángulo: "))
                altura = float(input("Introduce la altura del triángulo: "))
                area = 0.5 * base * altura
                print(f"El área del triángulo es: {area}")
            elif figura == "Trapecio":
                base_mayor = float(input("Introduce la base mayor del trapecio: "))
                base_menor = float(input("Introduce la base menor del trapecio: "))
                altura = float(input("Introduce la altura del trapecio: "))
                area = ((base_mayor + base_menor) * altura) / 2
                print(f"El área del trapecio es: {area}")
            else:
                print("Figura no válida.")

        area()

    def problem3(self):
        def menuP3():
            print("Porfavor pon un número entre una a tres cifras")
            num = int(input(">>> "))
            return num

        def obtenercifras(num):
            num_str = str(num)
            if len(num_str) > 3:
                print("Hubo un error")
            else:
                print(f"El número de cifras es: {len(num_str)}")

        num = menuP3()
        obtenercifras(num)

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
