class ManipuladorDeTributaveis:
    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            if isinstance(t, Tributavel):
                total += t.get_valor_imposto()
            else:
                print(f'{t.__repr__()} não é tributável.')
        return total

if	__name__	==	'__main__':
    from conta import Cliente, ContaCorrente, SeguroDeVida, ContaPoupanca, ContaInvestimento
    from tributavel import Tributavel
    cliente1 = Cliente('Pedro', 'Pereira', '111.111.111-11')
    cliente2 = Cliente('João', 'Santiago', '222.222.222-22')
    cliente3 = Cliente('Raimundo', 'Nonato', '333.333.333-33')
    cliente4 = Cliente('Rogério', 'Vilela', '444.444.444-44')
    cc1 = ContaCorrente(cliente1, '113-2', 1000, 1000)
    cc2 = ContaCorrente(cliente2, '113-2', 1000, 1000)
    seguro1 = SeguroDeVida(100.0, cliente3, '3437')
    seguro2 = SeguroDeVida(200.0, cliente4, '4347')
    cp1 = ContaPoupanca(cliente4, '223-2', 100, 200)
    cinv = ContaInvestimento(cliente3, '112-4', 100, 200)
    Tributavel.register(ContaCorrente)
    Tributavel.register(SeguroDeVida)
    Tributavel.register(ContaInvestimento)
    lista_tributaveis = [cc1, cliente1, cc2, seguro1, seguro2, cp1, cinv]
    manipulador = ManipuladorDeTributaveis()
    print(manipulador.calcula_impostos(lista_tributaveis))
    print(cc1.get_valor_imposto())
    print(seguro1.get_valor_imposto())
    print(cc2.get_valor_imposto())
    print(seguro2.get_valor_imposto())
    print(cinv.get_valor_imposto())