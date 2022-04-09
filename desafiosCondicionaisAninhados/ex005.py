# Questão 5) Crie um programa que leia duas notas e mostre sua media e informe se ele reprovou (menos que 5) está de recuperação entre (5 e 6), ou está aprovado (maior que 7.

n1 = float(input('Escreva sua 1° nota: '))
n2 = float(input('Escreva sua 2° nota: '))
media = (n1 + n2)/2

if media > 5:
  if media >= 6:
    print('Parabens! você esta aprovado! sua media foi {:.2f}'.format(media))
  else:
    print('Você está em recuperação, sua média foi {:.2f}'.format(media))
else:
  print('Você está reprovado, infelizmente sua média foi {:.2f}'.format(media))
