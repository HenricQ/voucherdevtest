class Compra:
    def __init__(self, número, valor, valorTotal=0):
        self._numero = número
        self._valor = valor 
        self._valorTotal = valorTotal

    def calcularValorTotal(self):
        self._valorTotal = self._valor * 1.05 * 1.17 
        print(f"O valor total do produto é de R${self._valorTotal:.2f}")



class AVista(Compra):
    def __init__(self, número, valor, valorTotal=0, desconto=0.9):
        super().__init__(número, valor, valorTotal)
        self._desconto = desconto

    def calcularValorAVista(self):
        super().calcularValorTotal()
        self._valorTotal *= self._desconto
        print(f"O valor final a vista é de R${self._valorTotal:.2f}")


class Parcelada(Compra):
    def __init__(self, número, valor, qtdParcelas, valorTotal=0, jurosSobParc = 0.05):
        super().__init__(número, valor, valorTotal)
        self._qtdParc = qtdParcelas
        self._juros = jurosSobParc


    def calcularValorParcelado(self):
        super().calcularValorTotal()
        self._valorTotal *= (1 + (self._qtdParc - 1) * self._juros)
        print(f"O valor final parcelado em {self._qtdParc} vezes é de R${self._valorTotal:.2f}")