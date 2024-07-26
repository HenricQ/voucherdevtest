class Forma:
    def __init__(self, nome) -> None:
        self.nome = nome

    def descricao(self):
        print(f"Forma : {self.nome}")


class Quadrado(Forma):
    def __init__(self, nome, lado=0) -> None:
        super().__init__(nome)
        self.lado = lado

    def descricao(self):
        print(f"Forma : Quadrado, Lado : {self.lado}")


class Circulo(Forma):
    def __init__(self, nome, raio=0) -> None:
        super().__init__(nome)
        self.raio = raio

    def descricao(self):
        print(f"Forma : Circulo, raio : {self.raio}")


quadrado = Quadrado('4', 10)
quadrado.descricao()
circulo = Circulo('3', 5)
circulo.descricao()