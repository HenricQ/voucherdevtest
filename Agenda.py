class Agenda:
    def __init__(self, dia, mes, ano, anotação):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
        self.__anotacao = anotação

    def validarData(self):
        dia = int(input("Digite o dia: "))
        mes = int(input("Digite o mês: "))
        ano = int(input("Digite o ano: "))

        print(f"{dia}/{mes}/{ano}")

    def anotarTarefa(self, novaTarefa):
        print(F'"{novaTarefa}" adicionado a agenda')
        self.__anotacao = novaTarefa

    def mostarAnotacao(self):
        print(f"Data: {self.dia}/{self.__mes}/{self.__ano}")
        print(f"Anotação: {self.__anotacao}")