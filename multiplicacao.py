def multiplicacao(num1, num2):
    try:
        float(num1)
        try:
            float(num2)
            resultado = float(num1) * float(num2)
            return resultado
        except ValueError:
            return f'O segundo valor não é válido.'
    except ValueError:
        try:
            float(num2)
        except ValueError:
            return f'Os dois valores não são válidos.'
        return f'O primeiro valor não é válido'


n1 = input('Digite um primeiro valor: ')
n2 = input('Digite um segundo valor: ')
print(multiplicacao(n1, n2))
