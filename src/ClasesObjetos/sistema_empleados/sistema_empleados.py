from src.ClasesObjetos.sistema_empleados.empleado import Empleado
from src.ClasesObjetos.sistema_empleados.empresa import Empresa

print('*** Sistema de Empleados ***')

# crear una instancia de una empresa
empresa1 = Empresa('Universidad Politecnica')

empresa1.contratar_empleaod('Rui', 'Ventas')
empresa1.contratar_empleaod('Maria', 'Marketing')
empresa1.contratar_empleaod('Pedro', 'Ventas')
empresa1.contratar_empleaod('Ana', 'Recursos Humanos')

#Obtener el total de objetos de tipo empleado
print(f'Total de empleados: {Empleado.obtener_total_empleados()}')

# Obtener el numero de empleados en el departamento de ventas
print(f'Empleados en el departamento Ventas: '
      f'{empresa1.obtener_numero_empleados_departamento('Ventas')}')