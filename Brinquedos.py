class Brinquedos:
    def __init__(self, nome, cor, tamanho, preço):
        self._nome = nome
        self._cor = cor
        self._tamanho = tamanho
        self._preco = preço

    def brincar(self):
        print(f"Estou brincando com {self._nome}")
    

