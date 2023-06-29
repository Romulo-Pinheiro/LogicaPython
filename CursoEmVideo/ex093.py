player_name = input('Nome do jogador: ').strip()
matches = abs(int(input('Quantas partidas ele jogou? ')))
goals = []
for i in range(1, matches + 1):
    goals.append(abs(int(input(f'Quantos gols na partida {i}? '))))
player_data = {'Nome': player_name, 'Gols': goals, 'Total': sum(goals)}
print('-=' * 30)
print(player_data)
print('-=' * 30)
for k, v in player_data.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {player_data["Nome"]} jogou {matches} partidas.')
for index, goal in enumerate(goals):
    print(f'\t=> Na partida {index + 1}, fez {goal} gols')
print(f'Foi um total de {player_data["Total"]} gols')
