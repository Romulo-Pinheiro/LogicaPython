n = mqmil = total = preco_barato = 0
barato = ''
while True:
    n += 1
    produto = str(input('Nome do produto: '))
    preco = float(input('Valor do produto: R$'))
    total += preco
    if n == 1 or preco < preco_barato:
        barato = produto
        preco_barato = preco
    if preco > 1000:
        mqmil += 1
    continua = str(input('Quer continuar [S/N]? ')).strip().upper()
    while continua not in ['S', 'N']:
        print('Resposta inválida. Tente novamente.')
        continua = str(input('Quer continuar [S/N]? ')).strip().upper()
    if continua == 'N':
        break
print(f'Você gastou R${total :.2f} na compra')
print(f'Há {mqmil} produtos que custam mais que mil reais nessa compra.')
print(f'O produto mais barato é {barato}, custando R${preco_barato :.2f}')
