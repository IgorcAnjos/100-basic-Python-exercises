# Questão 4) Faça um programa que leia o ano de nascimento de um jovem e informe se ele: Ainda vai se alistar no  exercito, se está na hora ou se já passou do tempo de se alistar. mostrar quanto tempo falta ou passou do prazo.

from datetime import  datetime

anoAtual = datetime.now().year
anoNascimento = int(input('Escreva seu ano de nascimento: '))
idade = anoAtual - anoNascimento
anoAlistamento = idade - 18

if idade >= 18:
  if idade > 18:
    print('Você ja se alistou no exercito fazem {} anos'.format(anoAlistamento))
  else:
    print('Está na hora de se alistar no exercito meu caro soldado!')
else:
  print('Faltam {} anos para você se alistar no exercito!'.format(-anoAlistamento))
