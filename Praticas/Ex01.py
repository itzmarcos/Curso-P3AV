# import os
# lista = []


#CONDIGO 01







# while True:
#     print('Selecione uma opção')
#     opção = input('[i]nserir', '[a]pagar', '[l]istar')
#     if opção == 'i':
#         nome = input('Nome: ')
#         list.append(nome)
#     elif opção == 'a':
#         indice_str = input(
#             'Escolha o índice para apagar: '
#         )
#         try:
#             indice = int(indice_str)
#             del lista[indice]
#         except ValueError:
#             print('Por favor digite numero int.')
#         except IndexError:
#             print('índice não existe na lista')
#         except Exception:
#             print('Erro desconhecido')
#     elif opção == 'l':
#         os.system('clear')

#         if len(lista) == 0:
#             print('Nada para lsitar')

#         for i, nome in enumerate(lista):
#             print(i,nome)




#CONDIGO 02




# lista = [ 
#     'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Luiz'}
# ]
# for item in lista:
#     if isinstance (item , set):
#         print('SET')
#         item.add(5)
#         print(item, isinstance(item, set))
#     elif isinstance(item, str):
#         print('STR')
#         print(item.upper)
#     else:
#         print('Outro')
