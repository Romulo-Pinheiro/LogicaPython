print('='*32)
print(' '*8, 'Banco Pinheiro')
print('='*32)
valor = abs(int(input('Que valor você deseja sacar? R$')))
lista = [50, 20, 10, 1]
valor_cedula = totced = 0
while True:
    totced = valor // lista[valor_cedula]
    if totced > 0:
        print(f'Total de {totced} cédulas de R${lista[valor_cedula]}')
    valor %= lista[valor_cedula]
    if valor == 0:
        break
    valor_cedula += 1
print('='*32)
print('Obrigado! Volte sempre.')
