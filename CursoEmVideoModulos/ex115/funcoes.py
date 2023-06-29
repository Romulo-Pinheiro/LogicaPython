def menu():
    print('\033[1;30m-' * 50)
    print('MENU PRINCIPAL'.center(50))
    print('-' * 50)
    print('\033[1;32m1\033[m - \033[1;36mVer pessoas cadastradas.\033[m')
    print('\033[1;32m2\033[m - \033[1;36mCadastrar nova pessoa.\033[m')
    print('\033[1;32m3\033[m - \033[1;36mSair do sistema.\033[m')
    print('\033[1;30m-\033[m' * 50)
    while True:
        try:
            opcao = int(input('\033[1;32mSUA OPÇÃO: \033[m'))
            if opcao not in range(1, 4):
                print('\033[1;31mERRO! DIGITE UMA OPÇÃO VÁLIDA.\033[m')
            else:
                return opcao
        except ValueError:
            print('\033[1;31mERRO! VOCÊ DEVE DIGITAR UM NÚMERO.\033[m')


def ver_cadastrados():
    try:
        with open('dados.txt', 'r') as dados:
            cadastrados = dados.readlines()
        print('\033[1;30m-'*50)
        print('PESSOAS CADASTRADAS'.center(50))
        print('-' * 50)
        for cadastro in cadastrados:
            if cadastro != '\n':
                print(cadastro.replace('\n', ''))
    except FileNotFoundError:
        print('\033[1;33mVocê ainda não realizou nenhum cadastro.')


def cadastrar():
    print('\033[1;30m-' * 50)
    print('NOVO CADASTRO'.center(50))
    print('-' * 50)
    while True:
        try:
            nome = input('\033[1;30mNome: ')
            while True:
                try:
                    idade = int(input('\033[1;30mIdade: '))
                except ValueError:
                    print('\033[1;31mERRO! A IDADE DEVE SER UM NÚMERO. TENTE NOVAMENTE\033[m')
                else:
                    break
        except KeyboardInterrupt:
            print('\033[1;31mDADO NÃO PREENCHIDO. TENTE NOVAMENTE\033[m')
        else:
            with open('dados.txt', 'a') as dados:
                dados.write(f'{nome :40} {idade :>3} anos\n')
            break
    print(f'\033[1;30mNovo registro de {nome} adicionado.\033[m')



