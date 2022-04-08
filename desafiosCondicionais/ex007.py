# Questão 7) Desenvolva um desafio que leia o comprimento de 3 retas e diga se ele pode ou não formar um triangulo.

n9 = float(input('(1/3) retas: '))
n10 = float(input('(2/3) retas: '))
n11 = float(input('(3/3) retas: '))

if n9 + n10 > n9 and n9 + n11 > n10 and n10 + n11 > n9:
  print('Pode se formar um triangulo!')
else:
  print('Não vai se formar um triangulo!')
