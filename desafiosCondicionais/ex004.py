# Questão 4) Desenvolva um programa que leia a distancia de uma viagem e calcule a o preço dela, sendo R$0.50 por Km para viagens com até 200Km e R$0.45 para viagens mais longas.

dist = float(input('Qual a distancia da sua viagem em Km? '))

if dist > 200 :
  print('Sua viagem custará R${:.2f}'.format(dist*0.45))
else:
  print('Sua viagem custará R${:.2f}'.format(dist*0.50))
