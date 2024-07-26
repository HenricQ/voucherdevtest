class Carro:
    def __init__(self,modelo:str='', marca:str='',cor:str='',ano:int=2024,valor:float=0,nivel:float=5,consumo:float=0):
        self.__modelo = modelo
        self.__marca = marca
        self.__cor = cor
        self.__ano = ano
        self.__valor = valor 
        self.__nivel = nivel
        self.__consumo = consumo
        self.__ligado = False


    def ligar(self):
        print("Carro ligado")
        self.__ligado = True
        
    def abastecer(self):
        nComb = float(input("Insira a quantidade de combustível a ser adicionada: "))
        self.__nivel += nComb   

    def andar(self):
        dPerc = float(input("Digite a distância percorrida pelo carro: "))
        cGast = float(input("Digite a quantidade de combustível consumido"))
        self.__consumo = dPerc / cGast


        self.__nivel -= cGast

    def verificarNivel(self):
        print(f"Com bases nas ultimas viagens, o consumo do {self.__modelo} é de {self.__consumo}Km/L")

    def calcularImposto(self):
        idade = 2024 - self.__ano
        if idade < 15:
            print(f"Seu carro tem {idade} anos e paga R${self.__valor * 0.025} de IPVA")
