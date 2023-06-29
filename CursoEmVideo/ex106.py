while True:
    print('\033[1;30;42m~' * 27)
    print('  Sistema de ajuda PyHelp')
    print('~' * 27)
    command = input("\033[mFunção ou Biblioteca -> ")
    if command.upper() == "FIM":
        print('\033[1;30;41m~~' * 6)
        print('  ATÉ LOGO')
        print('~~' * 6)
        break
    print('\033[1;30;44m~' * 41)
    print(f"   Acessando o manual do comando '{command}'")
    print('~' * 41)
    print('\033[7;1;30m')
    help(command)
