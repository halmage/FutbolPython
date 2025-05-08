# Importando tabla de base de datos
import database.JugadoresTable as JugadoresTable
import database.EquiposTable as EquiposTable


# Librerias creada
from package.Otros import Otros

# Librerias externa
from os import system
import time


class Jugadores:

    def __init__(self):
        self.jugadores_table = JugadoresTable.JugadoresTable()
        self.equipos_table = EquiposTable.EquiposTable()

    def menu(self):
        anuncio = """
        ****************
        |MODULO JUGADORES|
        ****************
        """
        print(anuncio)
        print("1. Crear jugador")
        print("2. buscar jugador")
        print("3. Listar jugadores")
        print("4. Actualizar jugador")
        print("5. Eliminar jugador")
        print("6. Salir")
        self.opcion = input("Elija una opcion: ")
        while self.opcion.isdigit() == False:
            print("ERROR: la variable opcion tiene que ser numerico")
            self.opcion = input("Ingrese una opcion: ")

    def create(self):
        # creacion de jugador
        anuncio = """
        ******************************
        |INGRESO DE DATOS DEL JUGADOR|
        ******************************
        """
        print(anuncio)
        # Ingreso de nombre
        nombre = input("Ingrese el nombre del jugador: ").lower()
        while nombre.isalpha() == False:
            print("ERROR: la variable nombre tiene que ser caracter")
            nombre = input("Ingrese el nombre del jugador: ").lower()
        # Ingreso de apellido
        apellido = input("Ingrese el apellido del jugador: ").lower()
        while apellido.isalpha() == False:
            print("ERROR: la variable apellido tiene que ser caracter")
            apellido = input("Ingrese el apellido del jugador: ").lower()
        # Ingreso de pais
        pais = input("Ingrese pais donde reside jugador: ").lower()
        while pais.isalpha() == False:
            print("ERROR: la variable pais tiene que ser caracter")
            pais = input("Ingrese pais donde reside jugador: ").lower()
        # Ingreso de ciudad
        ciudad = input("Ingrese ciudad donde reside jugador: ").lower()
        while ciudad.isalpha() == False:
            print("ERROR: la variable ciudad tiene que ser caracter")
            ciudad = input("Ingrese ciudad donde reside jugador: ").lower()
        # Ingreso de equipo
        validarContinuacion = True
        while validarContinuacion:  # validar si el estadio existe
            equipo = input("Ingrese equipo donde reside el jugador: ").lower()
            while equipo.isalpha() == False:
                print("ERROR: la variable equipo tiene que ser caracter")
                equipo = input("Ingrese equipo donde reside el jugador: ").lower()

            data_equipo = self.equipos_table.find(equipo)

            if data_equipo:  # si el equipo existe
                validarContinuacion = False
            else:  # si el equipo no existe
                print("Equipo no encontrado")
                validarContinuacion = Otros.validarContinuacion(self)
                if validarContinuacion:  # si el usuario quiere continuar
                    continue
                else:  # si el usuario quiere salir
                    break

        if data_equipo != None:  # si los datos del estadio son validos
            # Guardar datos en la tabla jugador
            equipo_id = data_equipo[0]
            datos = {
                "nombre": nombre,
                "apellido": apellido,
                "pais": pais,
                "ciudad": ciudad,
                "equipo_id": equipo_id,
            }
            self.jugadores_table.create(datos)
            print("Jugador creado correctamente")
            Otros.continuar(self)
            system("clear")

    def find(self):
        # buscar jugador
        anuncio = """
        *********************
        |BUSQUEDA DE JUGADOR|
        *********************
        """
        while True:
            print(anuncio)
            # Ingreso de nombre
            identificacion = input("Ingrese la identificacion del jugador: ").lower()
            while identificacion.isalnum() == False:
                print("ERROR: la variable identificacion tiene que ser caracter")
                identificacion = input(
                    "Ingrese el identificacion del jugador: "
                ).lower()
            # buscar jugador
            data_jugador = self.jugadores_table.find(identificacion)
            if data_jugador:
                # Mostrar datos del jugador
                print("**************************")
                print(f"Identificacion: {data_jugador[0]}")
                print(f"Nombre: {data_jugador[1]}")
                print(f"Apellido: {data_jugador[2]}")
                print(f"Pais: {data_jugador[3]}")
                print(f"Ciudad: {data_jugador[4]}")
                print(f"Equipo: {data_jugador[5]}")
                print("**************************")
            else:
                print("Jugador no encontrado")
            if Otros.seguir(self) == False:
                break

    def all(self):
        # listar todos los jugadores
        anuncio = """
        *******************************************
        |LISTADO DE TODOS LOS JUGADORES POR EQUIPO|
        *******************************************
        """
        print(anuncio)
        # Ingreso de nombre
        nombre_equipo = input("Ingrese el nombre del equipo: ").lower()
        while nombre_equipo.isalpha() == False:
            print("ERROR: la variable equipo tiene que ser caracter")
            nombre_equipo = input("Ingrese el nombre del equipo: ").lower()
        # buscar equipo
        data_jugadores = self.jugadores_table.all(nombre_equipo)
        if data_jugadores == None:
            print("Equipo no encontrado")
            validarContinuacion = Otros.validarContinuacion(self)
            if validarContinuacion:
                # si el usuario quiere continuar
                system("clear")
                self.all()
            else:
                # si el usuario quiere salir
                system("clear")
                return
        else:
            # Mostrar datos del jugador
            print("**************************")
            for i in range(len(data_jugadores)):
                print(f"Nombre: {data_jugadores[i][1]}")
                print(f"Nombre: {data_jugadores[i][2]}")
                print(f"Pais: {data_jugadores[i][3]}")
                print(f"Ciudad: {data_jugadores[i][4]}")
                print("**************************")
            Otros.continuar(self)

    def main(self):
        # menu principal
        while True:
            self.menu()
            match self.opcion:
                case "1":
                    # crear jugador
                    Otros.cargando(self)
                    system("clear")
                    Jugadores.create(self)
                case "2":
                    # buscar un jugador
                    Otros.cargando(self)
                    system("clear")
                    Jugadores.find(self)
                case "3":
                    # buscar todos los jugadores de un equipo
                    Otros.cargando(self)
                    system("clear")
                    Jugadores.all(self)
                case "4":
                    # salir
                    Otros.cargando(self)
                    system("clear")
                    break
