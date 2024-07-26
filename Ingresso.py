class Ingresso:
    def __init__(self, preço:float, setor):
        self._preco = preço
        self._setor = setor

    def alterarPreco(self):
        nPreco = float(input("Insira o novo preço do ingresso: "))
        self._preco = nPreco

    def mostrarSetor(self):
        print(f"Este ingresso é do setor {self._setor} e custa {self._preco}")


class IngressoVIP(Ingresso):
    def __init__(self, preço: float, setor, camarote:bool=False,
                  openBar:bool=False, openFood:bool=False, estacionamento:bool=False):
        super().__init__(preço, setor)
        self._camarote = camarote
        self._openBar = openBar
        self._openFood = openFood
        self._estacionamento = estacionamento 

    def pegarBebida(self):
        if self._openBar:
            print("Você pode pegar uma bebida de sua escolha")
        else:
            print("Você não tem acesso ao Open Bar!")

    def acessarCamarote(self):
        if self._camarote:
            print("Você pode acessar o camarote, fique a vontade")
        else:
            print("Você não possui acesso ao camarote!")