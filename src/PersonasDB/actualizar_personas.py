# Actualizar registros desde python a MYSQL
import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost', #127.0.0.1
    user='root',
    password='lol123',
    database='personas_db'
)

# Ejecutar la sentencia update
cursor = personas_db.cursor()
sentencia_sql = 'UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s'
valores = ('Ruiz', 'Gomez', 30, 4)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print('Se ha modificado la informacion...')
cursor.close()
personas_db.close()