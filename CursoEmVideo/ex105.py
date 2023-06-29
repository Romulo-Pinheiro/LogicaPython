def notas(*pontos, sit=False):
    """
    Função que recebe notas e retorna um dicionário
    :param pontos: Notas dos alunos
    :param sit: Se for True, o dicionário também irá conter uma situação de acordo com a
                média dos alunos (BOA, RAZOÁVEL ou RUIM)
    :return: Dicionário com total de notas, maior nota, menor nota, média e situação (opcio-
             nal)
    """
    dicio = {'total': len(pontos), 'maior': max(pontos), 'menor': min(pontos)}
    media = sum(pontos) / len(pontos)
    dicio["média"] = f'{media :.2f}'
    if sit:
        if media >= 7:
            dicio["Situação"] = "Boa"
        elif media >= 6:
            dicio["Situação"] = "Razoável"
        else:
            dicio["Situação"] = "Ruim"
    return dicio

print(notas(9, 5, 6, sit=True))