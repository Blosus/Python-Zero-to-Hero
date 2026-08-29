class aritmetica():

    def __init__(self, operando1, operando2):
        self._operando1 = operando1
        self._operando2 = operando2

    def sumar(self):
        return print(f'Suma: {self._operando1 + self._operando2}')

    def resta(self):
        return print(f'Resta: {self._operando1 - self._operando2}')

    def multiplicacion(self):
        return print(f'Multi: {self._operando1 * self._operando2}')

    def division(self):
        return print(f'Division: {self._operando1 // self._operando2}')

objeto1 = aritmetica(10, 20)
objeto1.sumar()
objeto1.resta()
objeto1.division()
objeto1.multiplicacion()