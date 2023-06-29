from conta import Conta

class Banco:
    def __init__(self):
        self._lista_contas = []

    @property
    def lista_contas(self):
        return self._lista_contas

    def adiciona(self, *contas):
        for conta in contas:
            if isinstance(conta, Conta):
                self._lista_contas.append(conta)

    def get_conta(self, posicao=0):
        try:
            return self._lista_contas[posicao]
        except IndexError:
            return "ERRO: Posição Inválida"

    def get_total_contas(self):
        return len(self._lista_contas)
