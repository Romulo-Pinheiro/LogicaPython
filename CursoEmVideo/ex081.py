decision = 'S'
values = []
while decision == 'S':
    n = int(input('Digite um número: '))
    values.append(n)
    decision = input('Quer continuar [S/N]? ').strip().upper()
    while decision not in ['S', 'N']:
        print('Resposta inválida. Tente novamente')
        decision = input('Quer continuar [S/N]? ').strip().upper()
values.sort(reverse = True)
print(f'Foram digitados {len(values)} números')
print(f'A lista ordenada de forma decrescente: {values}')
if 5 in values:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')