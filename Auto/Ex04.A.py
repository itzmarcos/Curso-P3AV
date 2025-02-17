class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome




class Fabricante:
    def __init__(self, nome):
        self.nome = nome



ferrari = Carro('Ferrari')
mercedes = Fabricante('Mercedes')
motor_1_1 = Motor('1.1')
ferrari.fabricante = mercedes
ferrari.motor = motor_1_1
print(ferrari.nome, ferrari.fabricante.nome, ferrari.motor.nome)
