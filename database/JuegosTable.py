import sqlite3


class JuegossTable:
    def createDatabase(self):
        # Crear la base de datos si no existe y crear la tabla
        conexion = sqlite3.connect("database/futbol.db")
        try:
            conexion.execute(
                """
                create table Juegos (
                                    id integer primary key autoincrement,
                                    FOREIGN KEY (equipo_locale_id)
                                    REFERENCES Equipos (id),
                                    FOREIGN KEY (equipo_visitante_id)
                                    REFERENCES Equipos (id),
                                    FOREIGN KEY (estadio_id)
                                    REFERENCES Estadios (id),
                                    goles_locales,
                                    goles_visitantes,
                                )"""
            )
        except sqlite3.OperationalError:
            print("La tabla juegos ya existe")
        conexion.close()
