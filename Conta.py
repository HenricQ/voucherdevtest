class Conta:
    def __init__(self, nome, cpf, numero, saldo):
        self.nome = nome
        self.__cpf = cpf
        self.__numero = numero
        self.__saldo = saldo

    def depositar(self, dep):
        print(f"R${dep:.2f} depositado a conta")
        self.__saldo += dep

    def sacar(self, saq):
        if self.__saldo < 0:
            print("Sem saldo disponível")
        else:
            print(f"R${saq:.2f} sacados da conta")
            self.__saldo -= saq

    def imprimirSaldo(self):
        print(f"Nome : {self.nome}")      
        print(f"CPF : {self.__cpf}")
        print(f"Número : {self.__numero}")
        print(f"Saldo : R${self.__saldo:.2f}")