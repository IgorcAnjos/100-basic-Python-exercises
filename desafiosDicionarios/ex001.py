# Questão 1) Faça um programa que leia o nome e média de um aluno guardando também a situação em um dicionário. No final mostre o conteúdo da estrutura na tela.

geral = {}
nome = str(input('Digite o nome: '))
geral['nome'] = nome
media = float(input(f'Digite a média de {nome}: '))
geral['media'] = media

if geral['media'] >= 7:
  geral['situação'] = 'Aprovado'
else:
  geral['situação'] = 'Reprovado'

for k,v in geral.items():
  print(f'- {k} é {v}')
