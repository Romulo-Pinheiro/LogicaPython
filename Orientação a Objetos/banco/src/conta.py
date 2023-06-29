# Exercício: Criando uma classe em Python. 8.13 Na apostila da Caelum

from time import gmtime
import abc
from tributavel import *

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @property
    def cpf(self):
        return self._cpf


class Data:
    def __init__(self):
        self._dia = gmtime()[2]
        self._mes = gmtime()[1]
        self._ano = gmtime()[0]

    @property
    def dia(self):
        return self._dia

    @property
    def mes(self):
        return self._mes

    @property
    def ano(self):
        return self._ano

    def get_data(self):
        return f"{self.dia}/{self.mes}/{self.ano}"


class Historico:

    def __init__(self):
        self._data_abertura = Data()
        self._transacoes = []

    def imprime(self):
        print(f'Data de Abertura: {self._data_abertura.get_data()}')
        print('Transações: ')
        for transacao in self._transacoes:
            print(f'- {transacao}')

    @property
    def transacoes(self):
        return self._transacoes


class Conta(abc.ABC):
    __slots__ = ['_titular', '_saldo', '_limite', '_numero', '_tipo', '_data_abertura', '_historico', 'id']
    identificador = 1

    def __init__(self, titular, numero, saldo, limite):
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self._numero = numero
        self._tipo = ''
        self._data_abertura = Data()
        self._historico = Historico()
        self.id = Conta.identificador
        Conta.identificador += 1

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        # Nesse caso, um setter para saldo não seria muito adequado porque devo
        # "obrigar" o usuário a utilizar apenas os métodos deposita() e saca().
        if saldo < 0:
            print('Saldo não deve ser negativo.')
        else:
            self._saldo = saldo

    @property
    def limite(self):
        return self._limite

    @property
    def numero(self):
        return self._numero

    @property
    def titular(self):
        return self._titular

    def deposita(self, valor):
        if valor > 0:
            self._saldo += valor
            self._historico.transacoes.append(f'Depósito de R${valor}')
            return True
        return False

    def saca(self, valor):
        if valor > 0:
            if self._saldo >= valor:
                self._saldo -= valor
                self._historico.transacoes.append(f'Saque de R${valor}')
                return True
            else:
                return False
        return False

    def transfere_para(self, conta_destino, valor):
        if self.saca(valor):
            conta_destino.deposita(valor)
            self._historico.transacoes.append(f'Transferência de R${valor} para conta {conta_destino.numero}')
            return True
        return False

    def extrato(self):
        print(f'Nome: {self.titular.nome}')
        print(f'Sobrenome: {self.titular.sobrenome}')
        print(f'CPF: {self.titular.cpf}')
        print(f'Número da Conta: {self._numero}')
        print(f'Saldo: {self._saldo}')
        self._historico.transacoes.append(f'Tirou extrato. Saldo de R${self._saldo}')

    @abc.abstractmethod
    def atualiza(self, taxa):
        pass

    def __str__(self):
        return f"Dados da conta:\nTipo: {self._tipo} \nNúmero: {self._numero} \nTitular: {self._titular.nome} {self._titular.sobrenome} \nSaldo: {self._saldo} \nLimite: {self._limite}"


class ContaPoupanca(Conta):
    def __init__(self, titular, numero, saldo, limite):
        super().__init__(titular, numero, saldo, limite)
        self._tipo = 'Poupança'
    
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3
        return self._saldo


class SeguroDeVida():
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05

class ContaCorrente(Conta):
    def __init__(self, titular, numero, saldo, limite):
        super().__init__(titular, numero, saldo, limite)
        self._tipo = 'Corrente'
    
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2
        return self._saldo

    def deposita(self, valor):
        if valor > 0:
            self._saldo += valor
            if self._saldo >= 0.10:
                self._saldo -= 0.10
            self._historico.transacoes.append(f'Depósito de R${valor}')
            return True
        return False

    def get_valor_imposto(self):
        return self._saldo * 0.01

class ContaInvestimento(Conta):
    def __init__(self, titular, numero, saldo, limite):
        super().__init__(titular, numero, saldo, limite)
        self._tipo = 'Investimento'

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5

    def get_valor_imposto(self):
        return self._saldo * 0.03




