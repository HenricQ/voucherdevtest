class Transporte:
    def __init__(self, capacidade):
        self._capacidade = capacidade


class Aquatico(Transporte):
    def __init__(self, capacidade):
        super().__init__(capacidade)


class Terreste(Transporte):
    def __init__(self, capacidade, numeroDeRodas=4):
        super().__init__(capacidade)
        self._numRodas = numeroDeRodas

class Aereo(Transporte):
    def __init__(self, capacidade, alturaMaxima=0):
        super().__init__(capacidade)
        self._altMax = alturaMaxima

class Automovel(Terreste):
    def __init__(self, capacidade, numeroDeRodas=4, placa='', numeroPortas=2, cor='', potencia=0):
        Terreste().__init__(capacidade, numeroDeRodas, numeroDeRodas)
        self._placa = placa
        self._qtdPorta = numeroPortas
        self._cor = cor
        self._potencia = potencia


class Lancha(Aquatico):
    def __init__(self, capacidade, velocidadeMaxima = 0):
        Aquatico().__init__(capacidade)
        self._topSpeed = velocidadeMaxima


class Navio(Aquatico):
    def __init__(self, capacidade, capacidadePassageiros = 0):
        super().__init__(capacidade)
        self._qtdPass = capacidadePassageiros

class AviaoMonomotor(Aereo):
    def __init__(self, capacidade, alturaMaxima=0, peso=0, potencia=0):
        Aereo().__init__(capacidade, alturaMaxima)
        self._peso = peso
        self._potencia = potencia


class AviaoComercial(Aereo):
    def __init__(self, capacidade, alturaMaxima=0, capacidadePassageiros=0):
        Aereo().__init__(capacidade, alturaMaxima)
        self._qtdPass = capacidadePassageiros


boeing = AviaoComercial(20000, 13000, 50)
whiteMustang = Automovel(1500, 4, 'Hra6985', 2, 'Branco', 513)
lancha = Lancha(3000, 150)