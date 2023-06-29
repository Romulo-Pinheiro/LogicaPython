players = []
while True:
    print('-' * 30)
    player_name = input('Nome do jogador: ').strip()
    matches = abs(int(input(f'Quantas partidas {player_name} jogou? ')))
    goals = []
    for i in range(1, matches + 1):
        goals.append(abs(int(input(f'Quantos gols na partida {i}? '))))
    player_data = {'Nome': player_name, 'Gols': goals, 'Total': sum(goals)}
    players.append(player_data.copy())
    condition = input('Quer continuar [S/N]? ').strip().upper()[0]
    if condition == 'N':
        break
print('-=' * 30)
print(f'{"cod" :<3} {"nome" :<15}{"gols" :<30}{"total" :>5}')
for index, p in enumerate(players):
    print(f'{index :>3} {p["Nome"] :<15}{str(p["Gols"]) :<30}{str(p["Total"]) :5}')
while True:
    print('-=' * 30)
    cod = int(input('Mostrar dados de qual jogador (999 para sair)? '))
    if 0 <= cod < len(players):
        print(f'-- LEVANTAMENTO DO JOGADOR {players[cod]["Nome"]}')
        for index, goal in enumerate(players[cod]["Gols"]):
            print(f'\tNo jogo {index + 1} fez {goal} gols.')
    elif cod == 999:
        break
    else:
        print(f'ERRO! Não existe jogador com código {cod}. Tente novamente!')
print('<<< VOLTE SEMPRE >>>')
