class Imovel:
    def __init__(self, inscriçãoMunicipal, valorAluguel, iPTU=0):
        self._inscricaoMunicipal = inscriçãoMunicipal
        self._valorAluguel = valorAluguel
        self._iPTU = iPTU
    
    def obterParcelaIPTU(self):
        parcela = self._valorAluguel * (1 + self._iPTU)
        print(f"O valor de cada parcela é de R${parcela:.2f}")
    
    def setValorAluguel(self):
        nAluguel = float(input("Insira o novo valor para aluguel: "))
        self._valorAluguel = nAluguel

class Casa(Imovel):
    def __init__(self, inscriçãoMunicipal, valorAluguel, iPTU=0, endereco=''):
        super().__init__(inscriçãoMunicipal, valorAluguel, iPTU)
        self._endereco = endereco

class Condominio(Imovel):
    def __init__(self, inscriçãoMunicipal, valorAluguel, iPTU=0, qtdQuartos=0):
        super().__init__(inscriçãoMunicipal, valorAluguel, iPTU)
        self._qtdQuartos = qtdQuartos
    
class Apartamento(Imovel):
    def __init__(self, inscriçãoMunicipal, valorAluguel, iPTU=0, andar=0):
        super().__init__(inscriçãoMunicipal, valorAluguel, iPTU)
        self._andar = andar

class Terreno(Imovel):
    def __init__(self, inscriçãoMunicipal, valorAluguel, iPTU=0, area=0):
        super().__init__(inscriçãoMunicipal, valorAluguel, iPTU)
        self._area = area
        
class Chacara(Imovel):
    def __init__(self, inscriçãoMunicipal, valorAluguel, iPTU=0, distanciaDaCidade=0):
        super().__init__(inscriçãoMunicipal, valorAluguel, iPTU)
        self._distCidade = distanciaDaCidade
