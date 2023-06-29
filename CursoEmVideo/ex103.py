def ficha(nome='<desconhecido>', gols='0'):
    """
    Retorna uma ficha com nome do jogador e número de gols
    :param nome: Nome do jogador. Por padrão, desconhecido.
    :param gols: Número de gols do jogador. Por padrão, 0.
    :return: Ficha com nome do jogador e número de gols.
    """
    if nome == '':
        nome = '<desconhecido>'
    if not gols.isdigit():
        gols = '0'
    return f'O jogador {nome} marcou {gols} gols'


print('-'*30)
nome_jogador = input('Nome do jogador: ').strip()
ngols = input('Número de gols: ').strip()
print(ficha(nome_jogador, ngols))
