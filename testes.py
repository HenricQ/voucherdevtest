# from Filme import Romance
# import Pessoa
import Funcionário
import Compra

compra1 = Compra.AVista(56, 120)
# compra1.calcularValorAVista()

compra2 = Compra.Parcelada(57, 120, 3)
compra2.calcularValorParcelado()

gernt = Funcionário.Gerente("Flesh", "gerente",5000)
vendedor = Funcionário.Vendedor('Almir',"Et.com", 2000, 120, 150)
vendedor.verMeta()
gernt.novaTentativaSenha()
gernt.alterarSalario()
# aluno1 = Pessoa.Aluno("Sala 144","Joazinho",16,8,4,7.5,5)
# aluno1.calcularMedia()

# r1 = Romance("Casais", 160, "Colorado")
# r1.play()
# r1.plot()