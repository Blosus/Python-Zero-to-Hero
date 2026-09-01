# Insertar registros desde python a MYSQL
import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost', #127.0.0.1
    user='root',
    password='lol123',
    database='personas_db'
)

# Ejecutar la sentencia insert
cursor = personas_db.cursor()
sentencia_sql = 'INSERT INTO personas(nombre, apellido, edad) VALUES (%s, %s, %s)'
valores = ('Rui', 'Veloso', 20)
cursor.execute(sentencia_sql, valores)
personas_db.commit()