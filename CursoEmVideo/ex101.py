from time import gmtime
def voto(ano):
    """
    Retorna qual a situação de voto de acordo com o ano de nascimento
    :param ano: Ano de nascimento do usuário
    :return: Se, pela idade no ano atual, o usuário terá voto obrigatório, negado ou opcional
    """
    ano_atual = gmtime()[0]
    idade = ano_atual - ano
    if idade < 16:
        return 'VOTO NEGADO'
    elif 18 <= idade < 65:
        return 'VOTO OBRIGATÓRIO'
    else:
        return 'VOTO OPCIONAL'
    
    
ano_nasc = int(input('Ano de nascimento: '))
ano_atual = gmtime()[0]
print(f'Com {ano_atual - ano_nasc} anos: {voto(ano_nasc)}')
