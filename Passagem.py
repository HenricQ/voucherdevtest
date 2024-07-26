class Passagem:
    def __init__(self, preço:float, assento):
        self._preco = preço
        self._assento = assento

    def alterarPreco(self):
        nPreco = float(input("Digite o novo preço da passagem: "))
        self._preco = nPreco

    def escolherAssento(self):
        nAssento = input("Digite qual será o novo assento: ")
        self._assento = nAssento

class PassagemBus(Passagem):
    def __init__(self, preço: float, assento, placa, leito=''):
        super().__init__(preço, assento)
        self._placa = placa
        self._leito = leito
        self._combustivelSuf = False

    def abastercer(self):
        self._combustivelSuf = True
        print("Ônibus com combustível suficiente, pronto para a viagem")

    def iniciarViagem(self):
        if self._combustivelSuf:
            print(f"O ônibus com placa {self._placa} está partindo!")
        else:
            print("Não há combustível suficiente para a viagem")


class PassagemAviao(Passagem):
    def __init__(self, preço: float, assento, portaoDeEmbarque, checkin=False):
        super().__init__(preço, assento)
        self._portao = portaoDeEmbarque
        self._checkin = checkin

    def realizarCheckin(self):
        print("Checkin em andamento...")
        print(f"Você está pronto para viajar, dirija-se ao portão {self._portao}")
        self._checkin = True

    def decolar(self):
        if self._checkin:
            print(f"O Avião está no portão {self._portao}")
            print("Pronto para decolar")
            print("Decolando")
        else:
            print("Realize o checkin primeiro")