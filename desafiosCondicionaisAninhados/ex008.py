# Questão 8) Refaça o desafio dos triangulos  acrescentando o recurso de mostrar que tipo de triangulo: equilatero, isosceles e escaleno.

print('Escreva o tamanho das vertices de um triangulo')
n1 = int(input('Vértice 1: '))
n2 = int(input('Vértice 2: '))
n3 = int(input('Vértice 3: '))

if n1 < n2 + n3 and n2 < n3 + n1 and n3 < n1 + n2:
  print('Os segmentos PODEM SE FORMAR um triangulo ', end='')
  if n1 == n2 == n3:
    print('EQUILATERO')
  elif n1!= n2 != n3 != n1:
    print('ESCALENO')
  else:
    print('ISOSCELES')
else:
  print('Os segmentos NÃO PODEM SE TORNAR UM TRIANGULO!')
