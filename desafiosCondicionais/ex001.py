#Questão 1) Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para um usuário tentar adivinhar qual o número que o computador pensou, o programa deverá escrever se o usuário venceu ou não.

import random

tent = int(input('Eu pensei em número de 1 a 5, tenta advinhar qual é: '))
n1 = random.randint(1, 5)

print(n1)

if tent == n1:
  print('Parabéns, você acertou!')
else:
  print('Infelizmente você errou, que peninha! \n o número que eu pensei era {}'.format(n1))
