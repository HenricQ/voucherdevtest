class Aluno:
    def __init__(self, nome, ra, *args):
        self.__nome = nome
        self.__ra = ra
        self.__notas = args
        self.__mediaGeral = (self.__ra + sum(self.__notas)) / (len(self.__notas) + 1)

    def mostrarNotas(self):
        print(f"O aluno {self.__nome} tem as seguintes notas: ")
        for i in self.__notas:
            print(i, end=', ')
        print(f"média final de {self.__mediaGeral:.1f}")
        if self.__mediaGeral < 5:
            print("\nEste aluno está reprovado")
        elif self.__mediaGeral < 7:
            print("\nEste aluno está de exame")
        else:
            print("\nO ALUNO ESTÁ APROVADO")


aluno1 = Aluno("Henrico",8,6,5,7,9)
aluno1.mostrarNotas()