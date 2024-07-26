class Filme:
    def __init__(self, nome, duração) :
        self._nome = nome
        self._duracao = duração

    def play(self):
        print(f"{self._nome} começou : {self._duracao} minutos restantes")

    
class Romance(Filme):
    def __init__(self, _nome, _duração, _protagonista):
        super().__init__(_nome, _duração)
        self.__protagonista = _protagonista

    def plot(self):
        print(f"Então, {self.__protagonista} beijou sua amada, e os dois viveram felizes para sempre")


class Acao(Filme):
    def __init__(self, _nome, _duração, _objeto):
        super().__init__(_nome, _duração)
        self.__objeto = _objeto

    def explodir(self):
        print(f"{self.__objeto} EXPLODIU 💣💣🧨")