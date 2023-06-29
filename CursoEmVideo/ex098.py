from time import sleep


def contador(start, end, step):
    local_step = abs(step)
    n = start
    if local_step == 0:
        local_step = 1
    print(f'Contagem de {start} até {end} de {local_step} em {local_step}')
    if start > end:
        local_step = - local_step
        while n >= end:
            print(n, end=' ')
            sleep(0.25)
            n += local_step
        print("FIM!")
    else:
        while n <= end:
            print(n, end=' ')
            sleep(0.25)
            n += local_step
        print('FIM!')


print('-=' * 30)
contador(1, 10, 1)
print('-=' * 30)
contador(10, 0, -2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
user_start = int(input('Início: '))
user_end = int(input('Fim: '))
user_step = int(input('Passo: '))
contador(user_start, user_end, user_step)
