# Questão 10) Crie um programa que faça o computador jogar jokempo com você.

from random import randint
from time import sleep

m = 0
j = 0

while j < 3 and m < 3:
  itens = ('Pedra' , 'Papel' , 'Tesoura' )
  n1 = randint(0,2)
  print('''Suas opções:
  [ 0 ]Pedra
  [ 1 ]Papel
  [ 2 ]Tesoura''')
  n2 = int(input('Qual é sua jogada?'))
  print('JO')
  sleep(1)
  print('KEM')
  sleep(1)
  print('PÔ!!!')
  print('=-'*40)
  if n1 != n2:
    if n1 == 0 and n2 == 2:
     print('Dessa vez eu ganhei eu escolhi {} e você {}'.format(itens[n1] , itens[n2]))
     m += 1
    elif n1 == 1 and n2 == 0:
      print('Dessa vez eu ganhei, eu escolhei {} e você {}'.format(itens[n1] , itens[n2]))
      m += 1
    elif n1 == 2 and n2 == 1:
      print('Dessa vez eu ganhei, eu escolhi {} e você {}'.format(itens[n1] , itens[n2]))
      m += 1
    else:
      print('Você ganhou em, mas sua sorte não dura muito!! Eu escolhi {} e você {}'.format(itens[n1], itens[n2]))
      j +=1
  else:
      print('Empate, olha lá rapaz! Nós dois escolhemos {}'.format(itens[n1]))
  print('*'*80)
else:
  if m == 3:
    print('Como deu pra ver, eu ganhei de você humano!')
  else:
    print('Parabéns por ser mais capaz do que eu neste jogo, Você ganhou!')