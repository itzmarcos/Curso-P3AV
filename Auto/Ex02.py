import copy



#CONDIGO 01





#  def multiplicar(*args):
#      total = 1
#      for arg in args:
#         total *= arg
#     return total

# resultado = multiplicar(2, 3, 4)
# #print(f"O valor da variável resultado é: {resultado}")

# def verificar_paridade(numero):
#     if numero % 2 == 0:
#         return "par"
#     else:
#         return "ímpar"

# numero = 9
# resultado = verificar_paridade(numero)
# print(f"O número {numero} é {resultado}.")



#CONDIGO 02





# def criar_multiplicador(multiplicador):
#     def multiplicar(numero):
#         return numero * multiplicador
#     return multiplicar


# duplicar = criar_multiplicador(2)
# triplicar = criar_multiplicador(3)
# print(duplicar(2))
# print(triplicar(3))

# p1 = {
#     'nome' : 'Marcos',
#     'sobrenome' : 'Antonio',
# }

# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
# p1.update({
#     'nome' : 'novo valor',
#     'idade' : 30,
# })

# p1.update(nome='novo valor', idade=30)

# tupla = ('nome', 'Marcos'),('idade', 30)
# lista = [['nome', 'Marcos'],['idade', 30]]
# p1.update(lista)
# print(p1)