user_numbers = []
while True:
    value = int(input('Digite um número: '))
    if value in user_numbers:
        print('Valor duplicado! Não vou adicionar.')
    else:
        user_numbers.append(value)
        print('Valor adicionado com sucesso!')
    condition = input('Quer continuar [S/N]? ').strip().upper()
    while condition not in ['S', 'N']:
        condition = input('Resposta inválida! Quer continuar [S/N]? ').strip().upper()
    if condition == 'N':
        break
print('=-' * 30)
print(f'Você digitou os valores {sorted(user_numbers)}')
