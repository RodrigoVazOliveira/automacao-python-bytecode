from bytebank import Funcionario

rodrigo = Funcionario(nome="Rodrigo Vaz", salario=2500, data_nascimento=1998)
print(rodrigo)
print("idade do é: {}".format(rodrigo.idade()))