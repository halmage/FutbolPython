import sqlite3
import database.EquiposTable as EquiposTable

# libreria externa
from faker import Faker


class JugadoresTable:

    def __init__(self):
        self.equipos_table = EquiposTable.EquiposTable()

    def createDatabase(self):
        # Crear la base de datos si no existe y crear la tabla
        # Configurar Faker (español o inglés)
        fake = Faker(locale="es_ES")
        conexion = sqlite3.connect("database/futbol.db")
        try:
            conexion.execute(
                """
                CREATE TABLE Jugadores (
                                    id integer primary key autoincrement,
                                    identificacion text not null,
                                    nombre text not null, 
                                    apellido text not null,                                     
                                    pais text not null,
                                    ciudad text not null,
                                    equipo_id integer not null,
                                    FOREIGN KEY (equipo_id) 
                                    REFERENCES Equipos (id) 
                                )"""
            )
            # Generar e insertar 110 registros falsos
            for _ in range(10):
                identificacion = fake.random_int(min=10000000, max=99999999)
                nombre = fake.first_name().lower()
                apellido = fake.last_name().lower()
                pais = fake.country().lower()
                ciudad = fake.city().lower()
                equipo_id = fake.random_int(min=1, max=10)
                conexion.execute(
                    """
                        INSERT INTO Jugadores (identificacion, nombre, apellido, pais, ciudad, equipo_id) 
                        VALUES (?, ?, ?, ?, ?, ?)""",
                    (identificacion, nombre, apellido, pais, ciudad, equipo_id),
                )
        except sqlite3.OperationalError:
            print("La tabla jugadores ya existe")
        conexion.commit()
        conexion.close()

    def create(self, datos):
        # Crear un nuevo jugador
        conexion = sqlite3.connect("database/futbol.db")
        cursor = conexion.cursor()
        cursor.execute(
            """
            INSERT INTO Jugadores (identificacion, nombre, apellido, pais, ciudad, equipo_id) 
            VALUES (?, ?, ?, ?, ?, ?)""",
            (
                datos["identificacion"],
                datos["nombre"],
                datos["apellido"],
                datos["pais"],
                datos["ciudad"],
                datos["equipo_id"],
            ),
        )
        conexion.commit()
        conexion.close()

    def find(self, identificacion):
        # Buscar un jugador por la identificacion
        conexion = sqlite3.connect("database/futbol.db")
        cursor = conexion.cursor()
        cursor.execute(
            """
            SELECT Jugadores.identificacion, 
                   Jugadores.nombre,
                   Jugadores.apellido, 
                   Jugadores.pais,
                   Jugadores.ciudad,
                   Equipos.nombre
                   FROM Jugadores INNER JOIN Equipos ON 
                   Jugadores.equipo_id = Equipos.id WHERE 
                   Jugadores.identificacion=?""",
            (identificacion,),
        )
        jugador = cursor.fetchone()
        conexion.close()
        return jugador

    def all(self, nombre_equipo):
        # Obtener todos los jugadores
        conexion = sqlite3.connect("database/futbol.db")
        cursor = conexion.cursor()
        equipo = self.equipos_table.find(nombre_equipo)
        if equipo == None:
            conexion.close()
            return None
        else:
            cursor.execute(
                """
                SELECT * FROM Jugadores WHERE equipo_id = ?""",
                (equipo[0],),
            )
            Jugadores = cursor.fetchall()
            conexion.close()
            return Jugadores
