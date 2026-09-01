from src.PersonasDB.zona_fit_db.conexion import Conexion
from src.PersonasDB.zona_fit_db.cliente import Cliente
from zona_fit_db.conexion import Conexion


class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES (%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()

            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrio un error al seleccionar clientes: {e}')
            return []
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None:
                Conexion.cerrar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar un cliente: {e}')
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None:
                Conexion.cerrar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar un cliente: {e}')
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None:
                Conexion.cerrar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion =  None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR,valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            print(f'Ocurrio un error al insertar un cliente: {e}')
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None:
                Conexion.cerrar_conexion(conexion)


if __name__ == '__main__':
    # Insertar cliente
    # cliente1 = Cliente(nombre='Alejandra', apellido='Tellez', membresia=300)
    # clientes_insertados = ClienteDAO.insertar(cliente1)
    # print(f'Clientes insertados: {clientes_insertados}')

    # Actualizar cliente
    cliente_actualizar = Cliente(2, 'Alexa', 'Tellez', 400)
    cliente_actualizado = ClienteDAO.actualizar(cliente_actualizar)
    print(f'Clientes actualizados {cliente_actualizado}')

    # Seleccionar los clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)