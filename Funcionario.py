class Funcionario:
    def __init__(self, nome, sobrenome, horasTrabalhadas, valorHora):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__hrTrab = horasTrabalhadas
        self.__valHora = valorHora


    def nomeCompleto(self):
        print(f"O nome completo do funcionário é {self.__nome} {self.__sobrenome}")

    def calcularSalario(self):
        salario = self.__hrTrab * self.__valHora
        print(f"O salário de {self.__nome} é de R${salario:.2f}")

    def incrementarHoras(self, horaAdc):
        self.__hrTrab += horaAdc
        print(f"O funcionário trabalhou {self.__hrTrab} horas")