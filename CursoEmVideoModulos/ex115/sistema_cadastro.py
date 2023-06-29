import funcoes

while True:
    opcao = funcoes.menu()
    if opcao == 1:
        funcoes.ver_cadastrados()
    elif opcao == 2:
        funcoes.cadastrar()
    elif opcao == 3:
        break
print('\033[1;30mAdeus...')
