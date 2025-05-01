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

    def find(self, nombre):
        conexion = sqlite3.connect("database/futbol.db")
        cursor = conexion.cursor()
        cursor.execute("select * from Equipos where nombre=?", (nombre,))
        equipo = cursor.fetchone()
        conexion.close()
        return equipo

    def all(self):
        conexion = sqlite3.connect("database/futbol.db")
        cursor = conexion.cursor()
        cursor.execute("select * from Equipos")
        equipos = cursor.fetchall()
        conexion.close()
        return equipos

    def update(self, dato, nombre, opcion):
        # Actualizar un registro de la tabla 'operaciones'
        conexion = sqlite3.connect("database/futbol.db")
        if opcion == "1":
            conexion.execute(
                "UPDATE Equipos SET nombre = '{}' WHERE nombre = '{}'".format(
                    dato, nombre
                )
            )
        elif opcion == "2":
            conexion.execute(
                "UPDATE Equipos SET pais = '{}' WHERE nombre = '{}'".format(
                    dato, nombre
                )
            )
        elif opcion == "3":
            conexion.execute(
                "UPDATE Equipos SET ciudad = '{}' WHERE nombre = '{}'".format(
                    dato, nombre
                )
            )
        conexion.commit()
        conexion.close()
