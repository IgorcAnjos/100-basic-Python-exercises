# Questão 5) Crie um programa que leira nome, sexo e a idade de vária pessoa, guardando os dados de cada um em um dicionário e todos os dicionário em uma lista. no final mostre A) Quantas pessoas foram cadastradas, B) A média de idade do grupo Uma lista com todas as mulheres D) Uma lista com todas as pessoas com idade acima da média.

Dadostemporários = dict()
Listageral = list()
SomaIdades = 0

while True:
  Dadostemporários['nome'] = str(input('Adicione o nome: '))
  Dadostemporários['idade'] = int(input('Adicione a idade: '))
  SomaIdades += Dadostemporários['idade']
  while True:
    Dadostemporários['Sexo'] = str(input('Adicione o sexo [M/F]')).upper().strip()[0]
    if not Dadostemporários['Sexo'] in 'MF':
      print('Escreva uma opção correta; ')
    else:
      break
  Listageral.append(Dadostemporários.copy())
  while True:
    val = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if not val in 'SN':
      print('Escreva direito')
    else:
      break
  if val == 'N':
    break

print(Dadostemporários)
print(f'Foram cadastradas {len(Listageral)}')
print(f' A média das idades é {(SomaIdades / len(Listageral))}')
print('As mulheres do grupo são: ', end = '')

for c in Listageral:
  if c['Sexo'] == 'F':
    print(f'{c["nome"]}. ', end = '')

print(f'\nAs pessoas com idade acima da média são: ', end = '' )
for c in Listageral:
  if c['idade'] > SomaIdades / len(Listageral):
    print(f'{c["nome"]}, com {c["idade"]}.')
