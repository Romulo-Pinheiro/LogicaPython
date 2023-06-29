def area(larg, comp):
    print(f'A área de um terreno {larg}x{comp} é de {larg * comp}m²')


print('Controle de Terrenos')
print('-' * 30)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
