def leiaInt(texto):
    """
    Uma espécie de input que só aceita valores inteiros
    :param texto: Texto a ser digitado pelo usuário
    :return: Valor de entrada após verificação
    """
    while True:
        try:
            resposta = input(texto)
            valido = int(resposta)
            return valido
        except (ValueError, TypeError):
            print('\033[1;31mErro: Por favor, digite um número inteiro válido!\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mO usuário preferiu não digitar esse número\033[m')
            return 0


def leiaFloat(texto):
    """
    Uma espécie de input que só aceita valores reais
    :param texto: Texto digitado pelo usuário
    :return: Valor de entrada após verificação
    """
    while True:
        try:
            resposta = input(texto)
            valido = float(resposta)
            return valido
        except (ValueError, TypeError):
            print('\033[1;31mErro: Por favor, digite um número inteiro válido!\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mO usuário preferiu não digitar esse número\033[m')
            return 0


valor1 = leiaInt('Digite um valor inteiro: ')
valor2 = leiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi: {valor1}\nO valor real digitado foi: {valor2}')