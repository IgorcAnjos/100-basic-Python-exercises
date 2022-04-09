# Questão 7) Crie um programa que leia a idade de um atleta e informe sua categoria, até 9 mirim, até 14 infantil, até 19 juvenil, até 20 senior, acima de 20 master

from datetime import date

n1 = date.today().year
nasc = int(input('Seu ano de nascimento: '))
anos = n1-nasc

if anos > 9:
  if anos > 20:
    print('Sua idade é {}, categoria é Master!'.format(anos))
  elif anos == 19:
    print('Sua idade é {}, categoria é Sênior!'.format(anos))
  elif 15 <= anos < 19:
    print('Sua idade é {}, categoria é Juvenil!'.format(anos))
  elif 9 < anos < 15:
    print('Sua idade é {}, categoria é infantil!'.format(anos))
else:
  print('Sua idade é {},categoria é Mirim'.format(anos))
