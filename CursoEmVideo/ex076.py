products = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25,
            'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30,
            'Livro', 34.90)
print(f'{" Listagem de Preços ":-^70}')
for index, elem in enumerate(products):
    if index % 2 == 0:
        print(f'{elem :13} {"." * 25} R$ {products[index + 1] :7.2f}')
print('-'*70)
