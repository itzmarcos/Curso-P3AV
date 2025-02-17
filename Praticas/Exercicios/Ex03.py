#CONDIGO 01



# tentativas = 0
# perguntas = [
#     {
#         'Pergunta' : 'Quanto é a metade de 2 + 2',
#         'Opcoes' : ['1', '2', '3', '4'],
#     },
#     {
#         'Pergunta' : 'Quanto é 120*2',
#         'Opcoes' : ['25', '240', '300', '140'],
#     },]
# qtd_acertos = 0
# for pergunta in perguntas:
#     print('Pergunta:', pergunta['Pergunta'])
#     print()

#     opcoes = pergunta['Opcoes']
#     for i, opcao in enumerate(opcoes):
#         print (f'{i})', opcao)
#     print()

#     escolha = input('Escolha uma opcao: ')

#     acertou = False
#     escolha_int = None
#     quantidade_opcoes = len(opcoes)

#     if escolha.isdigit():
#         escolha_int = int(escolha)

#     if escolha_int is not None:
#         if escolha_int >= 0 and escolha_int < quantidade_opcoes:
#             if opcoes[escolha_int] == pergunta['Resposta']:
#                 acertou = True
#     if acertou:
#         qtd_acertos += 1
#         print('Acertou')
#     else:
#         print('Errou')

#     print()
# print(f'Você acertou, com {qtd_acertos} vezes')





#CONDIGO 02

# EX. SET


# lista_de_num = [
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 1, 2, 3, 4, 5, 5, 6, 7],
#     [1, 2, 3, 4, 3, 5, 6, 2, 7],
# ]

# def encontra_primeiro_duplicado(lista_de_num):
#     num_chec =  set()
#     primeiro_duplicado = -1
#     for num in lista_de_num:
#         if num in num_chec:
#             primeiro_duplicado = num

#         num_chec.add(num)
        
#     print()
#     print()
#     return primeiro_duplicado
# for lista in lista_de_num:
#    print(
#        lista, encontra_primeiro_duplicado(lista))



#CONDIGO 03



# import copy

# from dados import produtos

# novos_produtos = [
#     {**p, 'preco:': round(p['preco']*1.1, 2)}
#     for p in copy.deepcopy(produtos)
    
# ]

# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')

# produtos_ordenados_por_nome = sorted(
#     copy.deepcopy(produtos),
#     key=lambda p: p['nome'],
#     reverse=True
# )
# print(*produtos, sep='\n')
# print()


# produtos_ordenados_por_preco = sorted(
#      copy.deepcopy(produtos),
#      key=lambda p: p['preco'],
# )



#CONDIGO 04




# #ENDIG


# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')
# print()
# print(*produtos_ordenados_por_nome, sep= '\n')
# print()
# print(*produtos_ordenados_por_preco, sep= '\n')

# def soma(x, y):
#     return x + y

# def multplicar(x, y):
#     return x * y

# def executar(funcao, x):
#     def interna (y):
#         return funcao(x, y)
#     return interna

# soma_com_cinco = executar(soma, 5)
# multplicar_por_dez = executar(multplicar, 10)
# print(soma_com_cinco(5))