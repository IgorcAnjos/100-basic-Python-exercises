# Questão 2) Crie um programa onde 4 jogadores joguem um dadoe tenha resultados aleatórios. Guarde esses resultados em um dicionário. No final coloque esse dicionário em ordem sabendo que o vencedor tirou o maior número.

from random import randint
from operator import itemgetter

s = 0
ranking = dict()
jogadas = dict()

for c in range(0,4):
  jogadas[f'jogador{c+1}'] = randint(1,6)
  print(jogadas.items())
sorted(jogadas.keys())

print('=-' * 30)

ranking = sorted(jogadas.items(), key = itemgetter(1), reverse=True)

for i, c in enumerate(ranking):
  print(f'{i+1}° Lugar : {c[0]} com {c[1]}')
