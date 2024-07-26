class NovaPessoa:
    def __init__(self, nome, telefone, email, endereço):
        self._nome = nome
        self._telefone = telefone
        self._email = email
        self._endereco = endereço

    def negociar(self):
        print(f"{self._email}: {self._nome} deseja fazer uma negociação, contate o tel. {self._telefone}")


class PessoaFisica(NovaPessoa):
    def __init__(self, nome, telefone, email, endereço, cPF):
        super().__init__(nome, telefone, email, endereço)
        self._cpf = cPF

    def negociar(self):
        return super().negociar()       
    

class PessoaJuridica(NovaPessoa):
    def __init__(self, nome, telefone, email, endereço, cNPJ):
        super().__init__(nome, telefone, email, endereço)
        self._cNPJ = cNPJ

    def negociar(self):
        return super().negociar()       
    