import sqlite3
import database.EquiposTable as EquiposTable


class JugadoresTable:

    def __init__(self):
        self.equipos_table = EquiposTable.EquiposTable()

    def createDatabase(self):
        # Crear la base de datos si no existe y crear la tabla
        conexion = sqlite3.connect("database/futbol.db")
        try:
            conexion.execute(
                """
                create table Jugadores (
                                    id integer primary key autoincrement,
                                    nombre text not null, 
                                    apellido text not null,                                     
                                    pais text not null,
                                    ciudad text not null,
                                    equipo_id integer not null,
                                    FOREIGN KEY (equipo_id) 
                                    REFERENCES Equipos (id) 
                                )"""
            )
        except sqlite3.OperationalError:
            print("La tabla jugadores ya existe")
        conexion.close()

    def create(self, datos):
        # Crear un nuevo jugador
        conexion = sqlite3.connect("database/futbol.db")
        cursor = conexion.cursor()
        cursor.execute(
            """
            insert into Jugadores (nombre, apellido, pais, ciudad, equipo_id) 
            values (?, ?, ?, ?, ?)""",
            (
                datos["nombre"],
                datos["apellido"],
                datos["pais"],
                datos["ciudad"],
                datos["equipo_id"],
            ),
        )
        conexion.commit()
        conexion.close()

    def find(self, nombre):
        # Buscar un jugador por nombre
        conexion = sqlite3.connect("database/futbol.db")
        cursor = conexion.cursor()
        cursor.execute(
            """
            select * from Jugadores where nombre = ?""",
            (nombre,),
        )
        Jugador = cursor.fetchall()
        conexion.close()
        return Jugador

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
                select * from Jugadores where equipo_id = ?""",
                (equipo[0],),
            )
            Jugadores = cursor.fetchall()
            conexion.close()
            return Jugadores
