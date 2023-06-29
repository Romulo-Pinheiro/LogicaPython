def dobro(valor):
    resultado = 2 * valor
    return resultado


def metade(valor):
    resultado = valor / 2
    return resultado


def aumentar(valor, porcentagem):
    acrescimo = porcentagem / 100 * valor
    resultado = valor + acrescimo
    return resultado


def reduzir(valor, porcentagem):
    decrescimo = porcentagem / 100 * valor
    resultado = valor - decrescimo
    return resultado


# Exercício 108
def moeda(valor):
    valor_formatado = 'R$'
    valor_formatado += str((round(float(valor), 2))).replace('.', ',')
    if valor_formatado[-3] == ',':
        return valor_formatado
    valor_formatado += '0'
    return valor_formatado
