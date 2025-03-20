import sqlite3


class JuegosTable:
    def createDatabase(self):
        # Crear la base de datos si no existe y crear la tabla
        conexion = sqlite3.connect("database/futbol.db")
        try:
            conexion.execute(
                """
                create table Juegos (
                                    id integer primary key autoincrement,
                                    equipo_local_id integer not null,
                                    equipo_visitante_id integer not null,
                                    estadio_id integer not null,
                                    goles_locales,
                                    goles_visitantes,
                                    FOREIGN KEY (equipo_local_id)
                                    REFERENCES Equipos (id)
                                    FOREIGN KEY (equipo_visitante_id)
                                    REFERENCES Equipos (id)
                                    FOREIGN KEY (estadio_id)
                                    REFERENCES Estadios (id)
                                )"""
            )
        except sqlite3.OperationalError:
            print("La tabla juegos ya existe")
        conexion.close()
