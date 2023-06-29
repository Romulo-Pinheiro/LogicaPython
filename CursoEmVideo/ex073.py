teams = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza',
         'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
         'Atlético-GO', 'Santos', 'Ceará', 'Internacional',
         'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude',
         'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print('-=' * 18)
print(f'Lista de times do Campeonato Brasileiro em ordem de classoficação:\n{teams}')
print('-=' * 18)
print(f'Os 5 primeiros colocados foram:\n{teams[0:5]}')
print('-=' * 18)
print(f'Os últimos 4 colocados foram:\n{teams[-4:]}')
print('-=' * 18)
print(f'Lista de times em ordem alfabética:\n{sorted(teams)}')
print('-=' * 18)
print(f'A Chapecoense está na posição {teams.index("Chapecoense") + 1}°')
print('-=' * 18)
