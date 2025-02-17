class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

class Aluno(Pessoa):
    ...

class Professor:
    ...

p1 = Aluno('Aluno', 'Lucas')
print(p1.nome)
print(p1.sobrenome)