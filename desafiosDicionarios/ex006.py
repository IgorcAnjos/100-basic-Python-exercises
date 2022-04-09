# Questão 6) Aprimore o desafio 93 para que elefuncione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador

AproveitamentoJogador = dict()
Listageral = list()
while True:
  s = 0
  print('=== Campeonato Brasileiro de Fotebolas!! ===')
  AproveitamentoJogador['nome'] = str(input('Escreva o nome: '))
  AproveitamentoJogador['Partidas jogadas'] = int(input('Quantidade de partidas jogadas: '))
  for c in range(0, AproveitamentoJogador['Partidas jogadas']):
    AproveitamentoJogador[f'Gols feitos na {c+1}° partida: '] = int(input(f'Quantidade de gols feitos na {c+1}° partida: '))
    s += AproveitamentoJogador[f'Gols feitos na {c+1}° partida: ']
  AproveitamentoJogador['Total de gols'] = s
  Listageral.append(AproveitamentoJogador.copy())
  while True:
    val = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if not val in 'SN':
      print('Escreva direito: ')
    else:
      break
  if val == 'N':
    break
for p, c in enumerate(Listageral):
  print(f'{p+1} {c["nome"]}')
while True:
  n = int(input('Digite o número de um jogador para ver mais detalhes: '))
  if n > len(Listageral) or n <= 0:
    print('Esse número não está disponível!')
  else:    
    for k, v in enumerate(Listageral):
      if k == n-1:
        for key, value in v.items():
          print(f'{key:<27}{value}')
  while True:
    val = str(input('[S/N] Quer continuar: ')).upper().strip()[0]
    if not val in 'SN':
      print('Escreveu errado otário')
    else:
      break
  if val == 'N':
    break
print('Acabou...')
