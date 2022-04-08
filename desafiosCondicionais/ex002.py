# Questão 2) Escreva um programa que leia a velocidade de um carro, se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado, a multa vai custar R$7,00 para cada km/h a cima do limite.

velocidade = float(input('Velocidade do carro: '))

if velocidade <= 80 :
  print('Está dentro do limite de velocidade da via.')
else:
  print('Você ultrapassou o limite da via, será multade em R$ {}'.format((velocidade - 80)*7))
