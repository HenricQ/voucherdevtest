class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.__nome = nome
        self.__autor = autor
        self.__editora = editora
        self.__paginas = paginas

    def alterarEditora(self, novaEditora):
        self.__editora = novaEditora
        print(f"A nova editora é {self.__editora}, do autor {self.__autor}")

    def listarQtdPaginas(self):
        print(f"O livro {self.__nome} possuí {self.__paginas} paginas")