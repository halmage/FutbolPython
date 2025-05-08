import sqlite3

# libreria externa
from faker import Faker


class EstadiosTable:
    def createDatabase(self):
        # Crear la base de datos si no existe y crear la tabla
        # Configurar Faker (español o inglés)
        fake = Faker(locale="es_ES")

        conexion = sqlite3.connect("database/futbol.db")
        try:
            conexion.execute(
                """
                CREATE TABLE Estadios (
                                    id integer primary key autoincrement,
                                    nombre text not null, 
                                    pais text not null,
                                    ciudad text not null 
                                )"""
            )
            # Generar e insertar 10 registros falsos
            lista_nombres = [
                "guaqueri",
                "chaima",
                "yanomami",
                "cumanagoto",
                "caiguire",
                "petare",
                "magolen",
                "petrines",
                "manchester",
                "queen",
            ]
            for n in range(10):
                nombre = lista_nombres[n]
                pais = fake.country().lower()
                ciudad = fake.city().lower()
                conexion.execute(
                    """
                    INSERT INTO Estadios (nombre, pais, ciudad)
                    VALUES (?, ?, ?)
                """,
                    (nombre, pais, ciudad),
                )
        except sqlite3.OperationalError:
            print("La tabla estadios ya existe")
        conexion.commit()
        conexion.close()

    def create(self, datos):

        # Configurar Faker (español o inglés)
        conexion = sqlite3.connect("database/futbol.db")
        conexion.execute(
            "INSERT INTO Estadios (nombre, pais, ciudad) VALUES (?,?,?)",
            (datos["nombre"], datos["pais"], datos["ciudad"]),
        )
        conexion.commit()
        conexion.close()

    def find(self, nombre):
        # Buscar un estadio
        conexion = sqlite3.connect("database/futbol.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Estadios WHERE nombre = ?", (nombre,))
        estadio = cursor.fetchone()
        conexion.close()
        return estadio

    def all(self):
        # Listar todos los estadios
        conexion = sqlite3.connect("database/futbol.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Estadios")
        estadios = cursor.fetchall()
        conexion.close()
        return estadios

    def update(self, dato, nombre, opcion):
        # Actualizar un registro de la tabla 'operaciones'
        conexion = sqlite3.connect("database/futbol.db")
        if opcion == "1":
            conexion.execute(
                "UPDATE Estadios SET nombre = '{}' WHERE nombre = '{}'".format(
                    dato, nombre
                )
            )
        elif opcion == "2":
            conexion.execute(
                "UPDATE Estadios SET pais = '{}' WHERE nombre = '{}'".format(
                    dato, nombre
                )
            )
        elif opcion == "3":
            conexion.execute(
                "UPDATE Estadios SET ciudad = '{}' WHERE nombre = '{}'".format(
                    dato, nombre
                )
            )
        conexion.commit()
        conexion.close()

    def delete(self, nombre):
        # Eliminar un registro de la tabla 'operaciones'
        conexion = sqlite3.connect("database/futbol.db")
        conexion.execute("DELETE FROM Estadios WHERE nombre ='{}'".format(nombre))
        conexion.commit()
        conexion.close()
