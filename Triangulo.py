class Triangulo:
    def __init__(self):
        self.__lado1 = float(input("Digite o valor do primeiro lado: "))
        self.__lado2 = float(input("Digite o valor do segundo lado: "))
        self.__lado3 = float(input("Digite o valor do terceiro lado: "))

    def calcularPerimetro(self):
        self.per = self.__lado1 + self.__lado2 + self.__lado3
        print(f"O perimetro do triângulo é de {self.per}")

    def getMaiorLado(self):
        maior = max(self.__lado1,self.__lado2,self.__lado3)
        print(f"O maior lado tem valor {maior}")