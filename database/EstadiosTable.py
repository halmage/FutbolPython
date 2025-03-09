import sqlite3


class EstadiosTable:
    def createDatabase(self):
        # Crear la base de datos si no existe y crear la tabla
        conexion = sqlite3.connect("database/futbol.db")
        try:
            conexion.execute(
                """
                create table Estadios (
                                    id integer primary key autoincrement,
                                    nombre text not null, 
                                    pais text not null,
                                    ciudad text not null 
                                )"""
            )
        except sqlite3.OperationalError:
            print("La tabla estadios ya existe")
        conexion.close()
