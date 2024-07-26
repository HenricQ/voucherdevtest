import string

class Senha:
    def __init__(self, senha):
        self.senha = senha

    
    def verificarSenha(self):
        senhaValida = 0
        min = False
        mai = False
        num = False
        car8 = False
        if len(self.senha) >= 8:
            car8 = True

        for i in self.senha:
            if i in string.digits:
                num = True
            if i in string.ascii_lowercase:
                min = True
            if i in string.ascii_uppercase:
                mai = True
        
        geral = num == mai == min == car8

        if geral:
            print("SENHA VALIDA")

        else:
            self.senha = input("SENHA INVALIDA!! Digite uma nova senha: ")
            self.verificarSenha()

        # if len(self.senha) >= 8:
        #     senhaValida += 1
        
        # elif string.ascii_uppercase in self.senha:
        #     senhaValida += 1

        # elif string.ascii_lowercase in self.senha:
        #     senhaValida += 1

        # elif string.digits in self.senha:
        #     senhaValida += 1

senha = Senha('12A')
senha.verificarSenha()