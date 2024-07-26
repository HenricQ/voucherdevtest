class Pessoa:
    def __init__(self, matricula, nome, idade):
        self.__matricula = matricula
        self._nome = nome
        self._idade = idade

class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade:int, *notas):
        super().__init__(matricula, nome, idade)
        self.__notas = notas

    def calcularMedia(self):
        media = sum(self.__notas) / len(self.__notas)
        print(f"A média das notas de {self._nome} é de {media} pontos")


class Professor(Pessoa):
    def __init__(self, matricula, nome, idade, formação, disciplina, carga=0):
        super().__init__(matricula, nome, idade)
        self._formacao = formação
        self._disciplina = disciplina
        self._carga = carga
    
    def lecionar(self):
        print(f"Professor(a) {self._nome} está dando sua aula, e está ensinando {self._disciplina}")

    def carreira(self):
        print(f"{self._nome} é formada em {self._formacao}, e trabalha {self._carga} por semana")
    