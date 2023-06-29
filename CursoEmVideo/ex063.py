n = abs(int(input('\033[1;30mQuantos termos da Sequência de Fibonacci você deseja visualizar? ')))
fibo = []
if n == 1:
    fibo = [0]
elif n > 1:
    fibo = [0, 1]
    while len(fibo) != n:
        fibo.append(fibo[-1] + fibo[-2])
print(f'Os {n} primeiros termos da sequência de Fibonacci são:\n \033[1;36m{fibo}')
