# Importando tabla de base de datos
import database.EstadiosTable as EstadiosTable

# Librerias creada
from package.Otros import Otros

# Librerias externa
from os import system
import time


class Estadios:

    def __init__(self):
        self.estadios_table = EstadiosTable.EstadiosTable()

    def menu(self):
        anuncio = """
        ****************
        |MODULO ESTADIO|
        ****************
        """
        print(anuncio)
        print("1. Crear estadio")
        print("2. Listar estadios")
        print("3. Actualizar estadio")
        print("4. Eliminar estadio")
        print("5. Salir")
        self.opcion = input("Elija una opcion: ")
        while self.opcion.isdigit() == False:
            print("ERROR: la variable opcion tiene que ser numerico")
            self.opcion = input("Ingrese una opcion: ")

    def create(self):
        anuncio = """
        ******************************
        |INGRESO DE DATOS DEL ESTADIO|
        ******************************
        """
        print(anuncio)
        # creacion de estadio
        # Ingreso de nombre
        nombre = input("Ingrese el nombre del estadio: ").lower()
        while nombre.isalpha() == False:
            print("ERROR: la variable nombre tiene que ser caracter")
            nombre = input("Ingrese el nombre del estadio: ").lower()

        # Ingreso de pais
        pais = input("Ingrese pais donde reside estadio: ").lower()
        while pais.isalpha() == False:
            print("ERROR: la variable pais tiene que ser caracter")
            pais = input("Ingrese pais donde reside estadio: ").lower()

        # Ingreso de ciudad
        ciudad = input("Ingrese ciudad donde reside estadio: ").lower()
        while ciudad.isalpha() == False:
            print("ERROR: la variable ciudad tiene que ser caracter")
            ciudad = input("Ingrese ciudad donde reside estadio: ").lower()

        datos = {"nombre": nombre, "pais": pais, "ciudad": ciudad}

        self.estadios_table.create(datos)
        print("Estadio creado correctamente")
        Otros.continuar(self)

    def listarEstadios(self):
        Otros.cargando(self)
        # listar estadios
        self.estadios_table.listEstadios()
        Otros.continuar(self)

    def actualizarEstadio(self):
        Otros.cargando(self)
        # actualizar estadio
        id = input("Ingrese el id del estadio: ")
        nombre = input("Ingrese el nombre del estadio: ")
        capacidad = input("Ingrese la capacidad del estadio: ")
        ciudad = input("Ingrese la ciudad del estadio: ")
        self.estadios_table.updateEstadio(id, nombre, capacidad, ciudad)
        print("Estadio actualizado correctamente")
        Otros.continuar(self)

    def eliminarEstadio(self):
        Otros.cargando(self)
        # eliminar estadio
        id = input("Ingrese el id del estadio: ")
        self.estadios_table.deleteEstadio(id)
        print("Estadio eliminado correctamente")
        Otros.continuar(self)

    def main(self):
        while True:
            self.menu()
            match self.opcion:
                case "1":
                    # crear estadio
                    Otros.cargando(self)
                    system("clear")
                    Estadios.create(self)
                case "5":
                    Otros.cargando(self)
                    system("clear")
                    break
