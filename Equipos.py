# Importando tabla de base de datos
import database.EquiposTable as EquiposTable
import database.EstadiosTable as EstadiosTable


# Librerias creada
from package.Otros import Otros

# Librerias externa
from os import system
import time


class Equipos:
    def __init__(self):
        self.equipos_table = EquiposTable.EquiposTable()
        self.estadios_table = EstadiosTable.EstadiosTable()

    def menu(self):
        anuncio = """
        ****************
        |MODULO EQUIPOS|
        ****************
        """
        print(anuncio)
        print("1. Crear equipo")
        print("2. Buscar equipo")
        print("3. Listar equipos")
        print("4. Actualizar equipo")
        print("5. Eliminar equipo")
        print("6. Salir")
        self.opcion = input("Elija una opcion: ")
        while self.opcion.isdigit() == False:
            print("ERROR: la variable opcion tiene que ser numerico")
            self.opcion = input("Ingrese una opcion: ")

    def create(self):
        # creacion de equipo
        anuncio = """
        *****************************
        |INGRESO DE DATOS DEL EQUIPO|
        *****************************
        """
        print(anuncio)
        # Ingreso de nombre
        nombre = input("Ingrese el nombre del equipo: ").lower()
        while nombre.isalpha() == False:
            print("ERROR: la variable nombre tiene que ser caracter")
            nombre = input("Ingrese el nombre del equipo: ").lower()

        # Ingreso nombre del estadio
        while True:  # validar si el estadio existe
            estadio = input("Ingrese estadio donde reside equipo: ").lower()
            while estadio.isalpha() == False:
                print("ERROR: la variable estadio tiene que ser caracter")
                estadio = input("Ingrese estadio donde reside equipo: ").lower()

            data_estadio = self.estadios_table.find(estadio)

            if data_estadio:  # si el estadio existe
                break

            # si el estadio no existe
            print("Estadio no encontrado")
            if Otros.validarContinuacion(self):
                # si el usuario quiere continuar
                continue

            # si el usuario quiere salir
            break

        if data_estadio != None:  # si los datos del estadio son validos
            # Guardar datos en la tabla equipo
            estadio_id = data_estadio[0]
            datos = {
                "nombre": nombre,
                "estadio_id": estadio_id,
            }
            self.equipos_table.create(datos)
            print("Equipo creado correctamente")
            Otros.continuar(self)
            system("clear")

    def find(self):
        # buscar equipo
        anuncio = """
        *************************
        |BUSCAR DATOS DEL EQUIPO|
        *************************
        """
        print(anuncio)
        nombre = input("Ingrese el nombre del equipo: ").lower()
        equipo = self.equipos_table.find(nombre)
        if equipo:
            print("**************************")
            print(f"Nombre: {equipo[1]}")
            print(f"Estadio: {equipo[2]}")
            print(f"Pais: {equipo[3]}")
            print(f"Ciudad: {equipo[4]}")
            print("**************************")
        else:
            print("Equipo no encontrado")
        if Otros.seguir(self):
            # volver a buscar
            self.find()

    def all(self):
        # listar estadios
        anuncio = """
        *****************************************
        |LISTADO DE TODOS LOS EQUIPOS INGRESADOS|
        *****************************************
        """
        print(anuncio)
        data = self.equipos_table.all()
        for i in range(len(data)):
            print(f"Nombre: {data[i][0]}")
            print(f"Estadio: {data[i][1]}")
            print(f"Pais: {data[i][2]}")
            print(f"Ciudad: {data[i][3]}")
            print("**************************")
        Otros.continuar(self)

    def menuUpdate(self, nombre):
        # opcion de actualizar
        anuncio = f"""
        ********************************{Otros.asteriscos(nombre)}
        |ACTUALIZANDO DATOS DEL EQUIPO {nombre.upper()}|
        ********************************{Otros.asteriscos(nombre)}
        """
        while True:
            print(anuncio)
            print("1. Nombre")
            print("2. Salir")
            opcion = input("Elija una opcion: ")
            while opcion.isdigit() == False:
                print("ERROR: la variable opcion tiene que ser numerico")
                opcion = input("Ingrese una opcion: ")
            if opcion < "1" or opcion > "2":
                # Mensaje de error por que la opcion no esta en el rango
                print("ERROR: la variable opcion tiene que ser entre 1 y 3")
                Otros.continuar(self)
                continue
            else:
                return opcion

    def opcionesUpdate(self, opcion, nombre):
        match opcion:
            case "1":
                # actualizar nombre
                dato = input("Ingrese nuevo nombre del equipo: ").lower()
                while dato.isalpha() == False:
                    print("ERROR: la variable nombre tiene que ser caracter")
                    dato = input("Ingrese nuevo nombre del equipo: ").lower()
                self.equipos_table.update(dato, nombre)
                print("Datos actualizado correctamente")
            case "2":
                return 0
            case _:
                print("ERROR: la variable opcion tiene que ser entre 1 y 2")
                Otros.continuar(self)

    def update(self):
        # actualizar equipo
        anuncio = """
        ******************************
        |ACTUALIZAR DATOS DEL EQUIPO|
        ******************************
        """
        print(anuncio)
        nombre = input("Ingrese el nombre del equipo: ")
        equipo = self.equipos_table.find(nombre)

        if not equipo:
            # si el equipo no existe
            print("equipo no encontrado")
            if Otros.seguir(self):
                self.update()

        # si el equipo existe
        system("clear")
        opcion = Equipos.menuUpdate(self, nombre)
        Equipos.opcionesUpdate(self, opcion, nombre)

        if Otros.seguir(self):
            # si el usuario quiere continuar
            self.update()

    def delete(self):
        anuncio = """
        ***************************
        |ELIMINAR DATOS DEL EQUIPO|
        ***************************
        """
        print(anuncio)
        nombre = input("Ingrese el nombre del equipo: ")
        equipo = self.equipos_table.find(nombre)
        if equipo:
            # si el equipo existe
            print(f"Nombre: {equipo[0]}")
            print(f"Pais: {equipo[1]}")
            print(f"Ciudad: {equipo[2]}")
        else:
            # si el equipo no existe
            print("Equipo no encontrado")
            if Otros.seguir(self):
                # si el usuario quiere continuar
                self.delete()

        if Otros.seguir(self):
            self.equipos_table.delete(nombre)
            print("Datos eliminado correctamente")

    def main(self):
        # menu principal
        while True:
            self.menu()
            match self.opcion:
                case "1":
                    # crear estadio
                    Otros.cargando(self)
                    system("clear")
                    Equipos.create(self)
                case "2":
                    # buscar estadio
                    Otros.cargando(self)
                    system("clear")
                    Equipos.find(self)
                case "3":
                    # motrar listado Equipos
                    Otros.cargando(self)
                    system("clear")
                    Equipos.all(self)
                case "4":
                    # actualizar datos del estadio
                    Otros.cargando(self)
                    system("clear")
                    Equipos.update(self)
                case "5":
                    # eliminar datos del estadio
                    Otros.cargando(self)
                    system("clear")
                    Equipos.delete(self)
                case "6":
                    Otros.cargando(self)
                    system("clear")
                    break
