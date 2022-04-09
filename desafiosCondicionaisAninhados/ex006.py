#Questão 6) Crie um programa que leia a idade de um atleta e informe sua categoria, até 9 mirim, até 14 infantil, até 19 juvenil, até 20 senior, acima de 20 master.

idade = int(input('Idade do atleta: '))

if idade > 20:
  print('Com {} anos sua categoria é master'.format(idade))
elif idade == 20:
  print('Com {} anos sua categoria é senior'.format(idade))
elif idade > 14:
  print('com {} anos sua categoria é juvenil'.format(idade))
elif idade > 9:
  print('Com {} anos sua categoria é infantil'.format(idade))
else:
  print('Com {} anos sua categoria é mirim'.format(idade))
