decision = 'S'
values = []
while decision == 'S':
    n = int(input('Digite um número: '))
    values.append(n)
    decision = input('Quer continuar [S/N]? ').strip().upper()
    while decision not in ['S', 'N']:
        print('Resposta inválida. Tente novamente')
        decision = input('Quer continuar [S/N]? ').strip().upper()
even_numbers = []
odd_numbers = []
for v in values:
    if v % 2 == 0:
        even_numbers.append(v)
    else:
        odd_numbers.append(v)
print(f'A lista completa é: {values}')
print(f'A lista de pares é: {even_numbers}')
print(f'A lista de ímpares é: {odd_numbers}')
