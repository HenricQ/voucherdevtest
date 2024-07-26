class Funcionario: 
    def __init__(self, nome, matricula, salario):
        self.__nome = nome
        self._matricula = matricula
        self._salario = salario
        self._pontosMensais = []

    def baterPonto(self):
        print("Ponto de hoje está batido")
        self._pontosMensais.append(1)


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario, vendasNoMes=0, metaDeVendas=0):
        super().__init__(nome, matricula, salario) 
        self._vendas = vendasNoMes
        self._meta = metaDeVendas

    def alterarVendas(self):
        nQtd = float(input("Quantas vendas foram feitas neste mês: "))
        self._vendas = nQtd

    def verMeta(self):
        diff = self._meta - self._vendas
        if diff > 0:
            print(f"Faltam {diff} vendas para bater a meta")
        else:
            print(f"A meta foi superada em {diff * -1} vendas")

class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario, senhaT = ''):
        super().__init__(nome, matricula, salario)
        self._senha = '230307'
        self._tentativaSenha = senhaT

    def novaTentativaSenha(self):
        self._tentativaSenha = input("Digite uma nova tentativa de senha: ")
        if self._senha == self._tentativaSenha:
            print("Senha correta")
        else:
            print("Senha incorreta!")

    def alterarSalario(self):
        if self._senha == self._tentativaSenha:
            self._salario = input("Digite o novo salário do funcionário: ")
        else:
            print("A senha inserida não está correta")
        # meu plano era fazer o gerente alterar o salario de outro funcionário, mas não consegui
