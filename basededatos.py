import sqlite3 # Libreria importada

class BaseDatos: # Clase
    def __init__(self, nombre_bd="vehiculos.db"): # Clase definida con constructor 'init'. Contiene la base de datos
        self.nombre_bd = nombre_bd
        self.conexion = None

    def conectar(self): # Conexion
        self.conexion = sqlite3.connect(self.nombre_bd)
        self.crear_tabla() # Llama el metodo crear_tabla

    def crear_tabla(self):
        cursor = self.conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vehiculos (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       marca TEXT NOT NULL,
                       modelo TEXT NOT NULL,
                       anio INTEGER NOT NULL
                       )

        ''')
        self.conexion.commit()

    def insertar_vehiculo(self, vehiculo): # Metodo insertar vehiculo
        cursor = self.conexion.cursor()
        cursor.execute("INSERT INTO vehiculos (marca, modelo, anio) VALUES (?, ?, ?)", (vehiculo.marca, vehiculo.modelo, vehiculo.anio))
        self.conexion.commit()

    def listar_vehiculos(self): # Metodo listar vehiculos
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM vehiculos")
        return cursor.fetchall()
    
    def buscar_vehiculos(self, id_vehiculo): # Metodo buscar vehiculos
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM vehiculos where id = ?", (id_vehiculo,))
        return cursor.fetchone()
    
    def eliminar_vehiculo(self, id_vehiculo): # Metodo eliminar vehiculos
        cursor = self.conexion.cursor()
        cursor.execute("DELETE FROM vehiculos where id = ?", (id_vehiculo,))
        self.conexion.commit()

    def actualizar_vehiculo(self, id_vehiculo, nueva_marca, nuevo_modelo, nuevo_anio): # Metodo actualizar vehiculos
        cursor = self.conexion.cursor()
        cursor.execute("UPDATE vehiculos SET marca = ?, modelo = ?, anio = ? WHERE id = ?", (nueva_marca, nuevo_modelo, nuevo_anio, id_vehiculo))
        self.conexion.commit()

    def cerrar_conexion(self): # Metodo cerrar conexion
        if self.conexion:
            self.conexion.close()