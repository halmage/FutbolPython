import sqlite3


class JugadoresTable:
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
