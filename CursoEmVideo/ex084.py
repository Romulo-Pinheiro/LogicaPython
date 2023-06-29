names = []
data = []
max_weight = 0
min_weight = 0
while True:
    data.append(input('Digite o seu nome: '))
    data.append(abs(float(input('Digite o seu peso (Kg): '))))
    names.append(data[:])
    data.clear()
    cond = input('Quer continuar [S/N]? ').strip().upper()
    if cond[0] == 'N':
        break
print('-='*30)
print(f'Ao todo você cadastrou {len(names)} pessoas.')
for i, n in enumerate(names):
    if i == 0:
        max_weight = n[1]
        min_weight = n[1]
    elif n[1] > max_weight:
        max_weight = n[1]
    elif n[1] < min_weight:
        min_weight = n[1]
print(f'O maior peso foi de {max_weight}Kg. Peso de', end=' ')
for n in names:
    if n[1] == max_weight:
        print(n[0], end=' ')
print(f'\nO menor peso foi de {min_weight}Kg. Peso de', end=' ')
for n in names:
    if n[1] == min_weight:
        print(n[0], end=' ')

