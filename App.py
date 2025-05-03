# LLamada de la base de datos
from database.JugadoresTable import JugadoresTable
from database.EstadiosTable import EstadiosTable
from database.EquiposTable import EquiposTable
from database.JuegosTable import JuegosTable
from database.GolesTable import GolesTable

# LLamada de las clases
from Estadios import Estadios
from Equipos import Equipos
from Jugadores import Jugadores

# Librerias creada
from package.Otros import Otros

# Librerias externa
from os import system
import time


class App:

    def __init__(self):
        self.Estadios = Estadios()
        self.Equipos = Equipos()
        self.Jugadores = Jugadores()

    def creacionDeLaBaseDeDatos(self):
        Otros.cargando(self)
        # creacion de base de datos
        # Creando tabla estadios
        estadios_table = EstadiosTable()
        estadios_table.createDatabase()
        # Creando tabla equipos
        equipos_table = EquiposTable()
        equipos_table.createDatabase()
        # Creando tabla jugadores
        jugadores_table = JugadoresTable()
        jugadores_table.createDatabase()
        # Creando tabla juegos
        juegos_table = JuegosTable()
        juegos_table.createDatabase()
        # Creando tabla goles
        goles_table = GolesTable()
        goles_table.createDatabase()
        print("Base de datos creada correctamente")
        Otros.continuar(self)

    def menu(self):
        anuncio = """
        ****************
        |MENU PRINCIPAL|
        ****************
        """
        print(anuncio)
        print("0. Crear base de datos")
        print("1. Modulo estadio")
        print("2. Modulo equipos")
        print("3. Modulo jugadores")
        print("4. Salir")
        self.opcion = input("Elija una opcion: ")
        while self.opcion.isdigit() == False:
            print("ERROR: la variable opcion tiene que ser numerico")
            self.opcion = input("Ingrese una opcion: ")

    def main(self):
        while True:
            self.menu()
            match self.opcion:
                case "0":
                    # creacion de base de datos
                    App.creacionDeLaBaseDeDatos(self)
                    continue
                case "1":
                    Otros.cargando(self)
                    system("clear")
                    self.Estadios.main()
                    continue
                case "2":
                    Otros.cargando(self)
                    system("clear")
                    self.Equipos.main()
                    continue
                case "3":
                    Otros.cargando(self)
                    system("clear")
                    self.Jugadores.main()
                    continue
                case "4":
                    # salida del sistema
                    Otros.cargando(self)
                    print("Gracias por utilizar nuestro sistema")
                    time.sleep(1)
                    system("clear")
                    break
                case _:
                    print("Opcion incorrecta")
                    Otros.continuar(self)
                    system("clear")
                    continue


app = App()
app.main()
