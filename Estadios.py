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
        print("2. buscar estadio")
        print("3. Listar estadios")
        print("4. Actualizar estadio")
        print("5. Eliminar estadio")
        print("6. Salir")
        self.opcion = input("Elija una opcion: ")
        while self.opcion.isdigit() == False:
            print("ERROR: la variable opcion tiene que ser numerico")
            self.opcion = input("Ingrese una opcion: ")

    def create(self):
        # creacion de estadio
        anuncio = """
        *****************
        |CREANDO ESTADIO|
        *****************
        """
        print(anuncio)
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

    def find(self):
        # buscar estadio
        anuncio = """
        ******************************
        |BUSCAR DATOS DEL ESTADIO|
        ******************************
        """
        while True:
            print(anuncio)
            nombre = input("Ingrese el nombre del estadio: ").lower()
            estadio = self.estadios_table.find(nombre)
            if estadio:
                print(f"Nombre: {estadio[1]}")
                print(f"Pais: {estadio[2]}")
                print(f"Ciudad: {estadio[3]}")
            else:
                print("Estadio no encontrado")
            if Otros.seguir(self) == False:
                break

    def all(self):
        # listar estadios
        anuncio = """
        ******************************************
        |LISTADO DE TODOS LOS ESTADIOS INGRESADOS|
        ******************************************
        """
        print(anuncio)
        data = self.estadios_table.all()
        for i in range(len(data)):
            print(f"Nombre: {data[i][1]}")
            print(f"Pais: {data[i][2]}")
            print(f"Ciudad: {data[i][3]}")
            print("**************************")
        Otros.continuar(self)

    def opcionUpdate(self, nombre):
        # opcion de actualizar
        nombre = nombre.upper()
        anuncio = f"""
        ***************************************
        |ACTUALIZAR DATOS DEL ESTADIO {nombre}|
        ***************************************
        """
        while True:
            print(anuncio)
            print("1. Nombre")
            print("2. Pais")
            print("3. Ciudad")
            print("4. Salir")
            opcion = input("Elija una opcion: ")
            while opcion.isdigit() == False:
                print("ERROR: la variable opcion tiene que ser numerico")
                opcion = input("Ingrese una opcion: ")
            if opcion < "1" or opcion > "4":
                # Mensaje de error por que la opcion no esta en el rango
                print("ERROR: la variable opcion tiene que ser entre 1 y 3")
                Otros.continuar(self)
                continue
            else:
                return opcion

    def update(self):
        # actualizar estadio
        anuncio = """
        ******************************
        |ACTUALIZAR DATOS DEL ESTADIO|
        ******************************
        """
        seguir = True
        while seguir:
            print(anuncio)
            nombre = input("Ingrese el nombre del estadio: ")
            estadio = self.estadios_table.find(nombre)
            if estadio:
                print(f"Nombre: {estadio[1]}")
                print(f"Pais: {estadio[2]}")
                print(f"Ciudad: {estadio[3]}")
            else:
                print("Estadio no encontrado")
                seguir = Otros.seguir(self)
                if seguir:
                    continue
                else:
                    break
            seguir = Otros.seguir(self)
            if seguir:
                opcion = Estadios.opcionUpdate(self, nombre)
                match opcion:
                    case "1":
                        # actualizar nombre
                        dato = input("Ingrese nuevo nombre del estadio: ").lower()
                        while dato.isalpha() == False:
                            print("ERROR: la variable nombre tiene que ser caracter")
                            dato = input("Ingrese nuevo nombre del estadio: ").lower()
                        self.estadios_table.update(dato, nombre, opcion)
                        print("Datos actualizado correctamente")
                    case "2":
                        # actualizar pais
                        dato = input(
                            "Ingrese nuevo pais donde recide estadio: "
                        ).lower()
                        while dato.isalpha() == False:
                            print("ERROR: la variable pais tiene que ser caracter")
                            dato = input(
                                "Ingrese nuevo pais donde recide estadio: "
                            ).lower()
                        self.estadios_table.update(dato, nombre, opcion)
                        print("Datos actualizado correctamente")
                    case "3":
                        # actualizar ciudad
                        dato = input(
                            "Ingrese la nueva ciudad donde recide estadio: "
                        ).lower()
                        while dato.isalpha() == False:
                            print("ERROR: la variable ciudad tiene que ser caracter")
                            dato = input(
                                "Ingrese la nueva ciudad donde recide estadio: "
                            ).lower()
                        self.estadios_table.update(dato, nombre, opcion)
                        print("Datos actualizado correctamente")
                    case "4":
                        system("clear")
                        break
            else:
                break
            seguir = Otros.seguir(self)

    def delete(self):
        anuncio = """
        ****************************
        |ELIMINAR DATOS DEL ESTADIO|
        ****************************
        """
        seguir = True
        while seguir:
            print(anuncio)
            nombre = input("Ingrese el nombre del estadio: ")
            estadio = self.estadios_table.find(nombre)
            if estadio:
                print(f"Nombre: {estadio[1]}")
                print(f"Pais: {estadio[2]}")
                print(f"Ciudad: {estadio[3]}")
            else:
                print("Estadio no encontrado")
                seguir = Otros.seguir(self)
                if seguir:
                    continue
                else:
                    break
            seguir = Otros.seguir(self)
            if seguir:
                self.estadios_table.delete(nombre)
                print("Datos eliminado correctamente")
            else:
                break
            seguir = Otros.seguir(self)

    def main(self):
        while True:
            self.menu()
            match self.opcion:
                case "1":
                    # crear estadio
                    Otros.cargando(self)
                    system("clear")
                    Estadios.create(self)
                case "2":
                    # buscar estadio
                    Otros.cargando(self)
                    system("clear")
                    Estadios.find(self)
                case "3":
                    # motrar listado estadios
                    Otros.cargando(self)
                    system("clear")
                    Estadios.all(self)
                case "4":
                    # actualizar datos del estadio
                    Otros.cargando(self)
                    system("clear")
                    Estadios.update(self)
                case "5":
                    # eliminar datos del estadio
                    Otros.cargando(self)
                    system("clear")
                    Estadios.delete(self)
                case "6":
                    Otros.cargando(self)
                    system("clear")
                    break
