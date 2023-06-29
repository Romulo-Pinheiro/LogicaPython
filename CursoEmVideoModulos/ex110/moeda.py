def moeda(valor):
    valor_formatado = 'R$'
    valor_formatado += str((round(float(valor), 2))).replace('.', ',')
    if valor_formatado[-3] == ',':
        return valor_formatado
    valor_formatado += '0'
    return valor_formatado


def dobro(valor, formatar=False):
    resultado = 2 * valor
    if formatar:
        return moeda(resultado)
    return resultado


def metade(valor, formatar=False):
    resultado = valor / 2
    if formatar:
        return moeda(resultado)
    return resultado


def aumentar(valor, porcentagem, formatar=False):
    acrescimo = porcentagem / 100 * valor
    resultado = valor + acrescimo
    if formatar:
        return moeda(resultado)
    return resultado


def reduzir(valor, porcentagem, formatar=False):
    decrescimo = porcentagem / 100 * valor
    resultado = valor - decrescimo
    if formatar:
        return moeda(resultado)
    return resultado


def resumo(valor, acrescimo, decrescimo):
    print('-' * 32)
    print(f'{"RESUMO DO VALOR" :^32}')
    print('-' * 32)
    print(f'{"Preço Analisado:" :22} {moeda(valor)}')
    print(f'{"Dobro do Preço:" :22} {dobro(valor, True)}')
    print(f'{"Metade do Preço:" :22} {metade(valor, True)}')
    print(f'{f"{acrescimo}% de Aumento:" :22} {aumentar(valor, acrescimo, True)}')
    print(f'{f"{decrescimo}% de Redução:" :22} {reduzir(valor, decrescimo, True)}')
    print('-' * 32)
