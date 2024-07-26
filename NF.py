class NF:
    def __init__(self, numero,tipo,serie,CNPJ,razaoSocial,data='',valor='',produtos='',ICMS=1,frete=0,IPI=0):
        self.__numero = numero
        self.__tipo = tipo
        self.__serie = serie
        self.__CNPJ = CNPJ
        self.__razaoSocial = razaoSocial
        self.__data = data
        self.__valor = valor
        self.__produtos = produtos
        self.__ICMS = ICMS
        self.__frete = frete
        self.__IPI = IPI



    def obterNumero(self):
        print(f"Pedido número {self.__numero}")
        print(f"Tipo : {self.__tipo}")
        print(f"Série : {self.__serie}")
        
    def obterDataEmissao(self):
        print(f"Data emissão : {self.__data}")
        print(f"Razão Social : {self.__razaoSocial}")


    def alterarRazaoSocial(self):
        nRazaoSoc = input("Insira a nova razão social : ")
        self.__razaoSocial = nRazaoSoc
    
    def calcularValorTotal(self):
        valTot = self.__valor * (1 + self.__ICMS + self.__IPI) + self.__frete
        print(f"Valor Total : R${valTot:.2f}")


    def gerarNotaFiscal(self):
        self.obterNumero()
        print(f"CNPJ : {self.__CNPJ}")
        self.obterDataEmissao()
        print(f"Produtos : {self.__produtos}")
        self.calcularValorTotal()