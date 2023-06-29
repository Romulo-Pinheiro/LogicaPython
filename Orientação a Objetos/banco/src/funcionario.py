import abc

class Funcionario(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_bonificacao(self):
        pass

if __name__ == '__main__':
    f1 = Funcionario()