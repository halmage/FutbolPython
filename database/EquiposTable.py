import sqlite3


class EquiposTable:
    def createDatabase(self):
        # Crear la base de datos si no existe y crear la tabla
        conexion = sqlite3.connect("database/futbol.db")
        try:
            conexion.execute(
                """
                create table Equipos (
                                    id integer primary key autoincrement,
                                    nombre text not null, 
                                    pais text not null,
                                    ciudad text not null,
                                    estadio_id integer not null,
                                    FOREIGN KEY (estadio_id) 
                                    REFERENCES Estadios (id)  
                                )"""
            )
        except sqlite3.OperationalError:
            print("La tabla equipos ya existe")
        conexion.close()

    def create(self, datos):
        conexion = sqlite3.connect("database/futbol.db")
        conexion.execute(
            "insert into Equipos (nombre, pais, ciudad, estadio_id) values (?,?,?,?)",
            (datos["nombre"], datos["pais"], datos["ciudad"], datos["estadio_id"]),
        )
        conexion.commit()
        conexion.close()
