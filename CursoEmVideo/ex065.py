soma = 0
qnt = 0
escolha = 'S'
maior = 0
menor = 0
while escolha == 'S':
    qnt += 1
    n = int(input(f'\033[1;30mDigite o {qnt}° número que deseja calcular: '))
    if qnt == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    escolha = input('Quer continuar [S/N]? ').strip().upper()
    while escolha not in ['S', 'N']:
        print('Sua resposta não é válida. Tente novamente: ')
        escolha = input('Quer continuar [S/N]? ').strip().upper()
media = soma / qnt
print(f'''A média entre os valores digitados é: {media}
O maior valor citado foi: {maior}
O menor valor citado foi: {menor}''')
