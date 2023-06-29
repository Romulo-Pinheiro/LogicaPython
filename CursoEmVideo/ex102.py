def fatorial(n, show=False):
    """
    Realiza o cálculo de Fatorial de um número
    :param n: Número para calcular o fatorial
    :param show: Valor booleano que, se positivo, a função retorna uma string exibindo o
                 processo de fatorial de um número.
    :return: Fatorial em valor inteiro ou string
    """
    if n < 0:
        return '?'
    fat = 1
    calculo = f'{n}! = '
    for num in range(n, 0, -1):
        fat *= num
        if show:
            if num != 1:
                calculo += f'{num} * '
            else:
                calculo += f'{num} = '
    if show:
        calculo += f'{fat}'
        return calculo
    else:
        return fat


print(fatorial(5))