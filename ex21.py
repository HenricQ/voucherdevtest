from random import choice

def escolheAluno(qtd):
    al = []
    for i in range(qtd):
        al.append(input("Digite o nome do aluno: "))
    print(f"O aluno escolhido foi: {choice(al)}")


escolheAluno(6)