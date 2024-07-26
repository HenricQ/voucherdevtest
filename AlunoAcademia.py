class AlunoAcademia:
    def __init__(self, nome:str='', idade:int=0, peso:float=0, altura:float=0, mensalidade:float=120):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__mensalidade = mensalidade

        if idade < 18:
            self.__mensalidade *= 0.75

    def calcularIMC(self):
        imc = self.__peso / self.__altura**2
        print(f"O IMC do(a) aluno(a) {self.__nome} é {imc:.2f}")

    def obterValorMensalidade(self):
        print(f"Nome : {self.__nome}")
        print(f"Mensalidade : R${self.__mensalidade}")