def leiaInt(texto):
    """
    Uma espécie de input que só aceita valores inteiros
    :param texto: Valor a ser digitado pelo usuário
    :return: Erro se o valor não for inteiro ou o próprio valor se for inteiro.
    """
    resposta = input(texto)
    while not resposta.isdigit():
        print("\033[1;31mERRO! Digite um número inteiro válido\033[m")
        resposta = input(texto)
    return int(resposta)

print('-'*30)
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
