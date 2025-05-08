import sqlite3

# libreria externa
from faker import Faker


class EquiposTable:
    def createDatabase(self):
        # Crear la base de datos si no existe y crear la tabla
        # Configurar Faker (español o inglés)
        fake = Faker(locale="es_ES")
        conexion = sqlite3.connect("database/futbol.db")
        try:
            conexion.execute(
                """
                create table Equipos (
                                    id integer primary key autoincrement,
                                    nombre text not null, 
                                    estadio_id integer not null,
                                    FOREIGN KEY (estadio_id) 
                                    REFERENCES Estadios (id)  
                                )"""
            )
            # Generar e insertar 10 registros falsos
            lista_nombres = [
                "trueno",
                "maimi",
                "villaloid",
                "barcelona",
                "colimpio",
                "bucaramanga",
                "petardos",
                "dragones",
                "beans",
                "pelotudos",
            ]
            for n in range(10):
                nombre = lista_nombres[n]
                estadio_id = n + 1
                conexion.execute(
                    """
                    INSERT INTO Equipos (nombre, estadio_id)
                    VALUES (?, ?)
                """,
                    (nombre, estadio_id),
                )
        except sqlite3.OperationalError:
            print("La tabla equipos ya existe")
        conexion.commit()
        conexion.close()

    def create(self, datos):
        conexion = sqlite3.connect("database/futbol.db")
        conexion.execute(
            "insert into Equipos (nombre, estadio_id) values (?,?)",
            (datos["nombre"], datos["estadio_id"]),
        )
        conexion.commit()
        conexion.close()

    def find(self, nombre):
        conexion = sqlite3.connect("database/futbol.db")
        cursor = conexion.cursor()
        cursor.execute(
            """SELECT Equipos.nombre, Estadios.pais, Estadios.ciudad FROM 
               Equipos INNER JOIN Estadios ON Equipos.estadio_id = Estadios.id WHERE Equipos.nombre=?""",
            (nombre,),
        )
        equipo = cursor.fetchone()
        conexion.close()
        return equipo

    def all(self):
        conexion = sqlite3.connect("database/futbol.db")
        cursor = conexion.cursor()
        cursor.execute(
            """select Equipos.nombre, Estadios.pais, Estadios.ciudad from 
               Equipos inner join Estadios ON Equipos.estadio_id = Estadios.id""",
        )
        equipos = cursor.fetchall()
        conexion.close()
        return equipos

    def update(self, dato, nombre):
        print(dato, "--", nombre)
        # Actualizar un registro de la tabla 'operaciones'
        conexion = sqlite3.connect("database/futbol.db")
        conexion.execute(
            "UPDATE Equipos SET nombre = '{}' WHERE nombre = '{}'".format(dato, nombre)
        )
        conexion.commit()
        conexion.close()

    def delete(self, nombre):
        # Eliminar un registro de la tabla 'operaciones'
        conexion = sqlite3.connect("database/futbol.db")
        conexion.execute("DELETE FROM Equipos WHERE nombre ='{}'".format(nombre))
        conexion.commit()
        conexion.close()
