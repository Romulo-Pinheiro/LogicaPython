def leia_dinheiro(texto):
    while True:
        valor = input(texto).strip()
        novo_valor = ''
        nponto = 0
        for c in valor:
            if c == '.' or c == ',':
                nponto += 1
                continue
            else:
                novo_valor += c
        if novo_valor.isnumeric() and nponto <= 1:
            break
        print(f'\033[1;31mERRO: "{valor}" é um termo inválido!\033[m')
    novo_valor = valor.replace(',', '.')
    return float(novo_valor)

