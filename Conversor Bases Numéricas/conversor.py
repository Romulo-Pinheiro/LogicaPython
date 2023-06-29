from funcoes import decimal, conversor

numero = str(input('Informe um valor qualquer: ')).upper()
base_numero = 0
while base_numero not in [2, 8, 10, 16]:
    print('''Informe sua base:
    [  2 ] Binária
    [  8 ] Octal
    [ 10 ] Decimal
    [ 16 ] Hexadecimal''')
    base_numero = int(input('Digite aqui: '))
base_conversao = 0
while base_conversao not in [2, 8, 10, 16]:
    print('''Para qual base deseja converter:
    [  2 ] Binária
    [  8 ] Octal
    [ 10 ] Decimal
    [ 16 ] Hexadecimal''')
    base_conversao = int(input('Digite aqui: '))
numero = decimal(numero, base_numero)
if base_conversao == 10:
    print(numero)
else:
    print(conversor(numero, base_conversao))
