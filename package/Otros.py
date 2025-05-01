# Librerias externa
from os import system
import time


class Otros:
    def cargando(self):
        for i in range(2):
            print(".")
            time.sleep(0.5)  # Pausa de 1 segundo para visualizar el resultado

    def continuar(self):
        # Validar si el usuario quiere continuar
        print("Presione la tecla enter para continuar...")
        input()
        Otros.cargando(self)
        system("clear")

    def seguir(self):
        # Validar si el usuario quiere seguir eliminando
        respuesta = input("Quieres seguir realizando operaciones (y/n): ")
        while (
            respuesta != "y"
            and respuesta != "Y"
            and respuesta != "n"
            and respuesta != "N"
        ):
            print("ERROR: la variable respuesta tiene que ser (y|Y) o (n|N)")
            respuesta = input("Quieres seguir realizando operaciones (y/n): ")

        if respuesta == "y" or respuesta == "Y":
            Otros.cargando(self)
            system("clear")
            return True
        else:
            Otros.cargando(self)
            system("clear")
            return False

    def validarContinuacion(self):
        # Validar si el usuario quiere seguir eliminando
        respuesta = input("Quieres seguir realizando operaciones (y/n): ")
        while (
            respuesta != "y"
            and respuesta != "Y"
            and respuesta != "n"
            and respuesta != "N"
        ):
            print("ERROR: la variable respuesta tiene que ser (y|Y) o (n|N)")
            respuesta = input("Quieres seguir realizando operaciones (y/n): ")

        if respuesta == "y" or respuesta == "Y":
            return True
        else:
            Otros.cargando(self)
            system("clear")
            return False
