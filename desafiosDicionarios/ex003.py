# Questão 3) Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos ela vai se aposentar.

from datetime import date, datetime 

DadosTraballhador = dict()
DadosTraballhador['nome'] = str(input('Escreva o nome: '))
DadosTraballhador['nascimento'] = int(input('Escreva o ano de nascimento; '))
DadosTraballhador['idade'] = ((datetime.today().year) - (DadosTraballhador['nascimento']))
DadosTraballhador['CTPS'] = int(input('Escreva o número da CTPS [0 se não tiver]: '))

if DadosTraballhador['CTPS'] != 0:
  DadosTraballhador['Contribuição'] = int(input('Escreva quantos anos de contribuição tem: '))
  DadosTraballhador['Salario'] = float(input('Escreva foi o ultimo salário que rebeceu: '))
  if DadosTraballhador['Contribuição'] >= 35:
    DadosTraballhador['Para aposentar faltam'] = 'Já pode se aposentar!'
  else:
    DadosTraballhador['Para aposentar faltam'] = 35 - DadosTraballhador['Contribuição']  

for k, v in DadosTraballhador.items():
  print(f'- {k}: {v}')
