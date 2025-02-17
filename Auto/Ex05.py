from datetime import datetime
import math
# ano_atual = datetime.now().year


# def voto(* idade):
#      idade = ano_atual - nasc
#      if idade <= 18:
#          print(f'Voce tem {idade} anos e esta Negado')
#      elif idade == 18:
#          print(f'Voce tem {idade} anos e é OPCIONAL')
#      else:
#          print(f'Voce tem {idade} anos e é OBRIGATORIO')



















# nasc = int(input('Digite sua idade: '))
# voto()

# def ficha(nome, gol):
#     if not nome and gol:
#         print(f'Jogador desconhecido e marcou {gol} no campeonato!')
#     else:
#         print(f'o Jogador {nome} fez {gol} gols no campeonato!')





# nome = str(input('Nome do jogador: '))
# gol = int(input('Quantidade de gols: '))
# ficha(nome, gol)




def leiaInt(n):
    while True:
        n = leiaInt('Digite um numero')
        if not n == int:
            print('ERRO 404')
        else:
            print(n)
            break



n = leiaInt('Digite um numero')
leiaInt()