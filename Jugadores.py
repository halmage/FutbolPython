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

    def main(self):
        # menu principal
        while True:
            self.menu()
            match self.opcion:
                case "1":
                    # crear estadio
                    Otros.cargando(self)
                    system("clear")
                    Jugadores.create(self)
                case "2":
                    # salir
                    Otros.cargando(self)
                    system("clear")
                    break
