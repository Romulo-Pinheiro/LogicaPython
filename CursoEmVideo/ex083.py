expression = [caracter for caracter in input('Digite a expressão: ').strip()]
nparentheses = (('(' in expression) and (')' in expression)) and (expression.count('(') == expression.count(')'))
if nparentheses:
    n_open = 0
    n_close = 0
    valid = True
    for elem in expression:
        if elem == '(':
            n_open += 1
            continue
        elif elem == ')':
            n_close += 1
        if n_close > n_open:
            valid = False
            break
    if valid:
        print('Essa expressão está válida!')
    else:
        print('Essa expressão não é válida!')
else:
    print('Essa expressão não é válida.')
