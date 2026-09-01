# Borrar registros desde python a MYSQL
import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost', #127.0.0.1
    user='root',
    password='lol123',
    database='personas_db'
)

# Ejecutar la sentencia update
cursor = personas_db.cursor()
sentencia_sql = 'DELETE FROM personas WHERE id=%s'
valores = (1,)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print(f'Se borro exitosamente...')
cursor.close()
personas_db.close()