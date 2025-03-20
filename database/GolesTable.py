import sqlite3


class GolesTable:
    def createDatabase(self):
        # Crear la base de datos si no existe y crear la tabla
        conexion = sqlite3.connect("database/futbol.db")
        try:
            conexion.execute(
                """
                create table Goles (
                                    id integer primary key autoincrement,
                                    jugador_id integer not null,
                                    equipo_id integer not null,
                                    estadio_id integer not null,
                                    cantidad_goles,
                                    FOREIGN KEY (jugador_id) 
                                    REFERENCES Jugadores (id)
                                    FOREIGN KEY (equipo_id) 
                                    REFERENCES Equipos (id)
                                    FOREIGN KEY (estadio_id) 
                                    REFERENCES Estadios (id)
                                )"""
            )
        except sqlite3.OperationalError:
            print("La tabla goles ya existe")
        conexion.close()
