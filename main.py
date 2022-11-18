from bytebank import Funcionario

#rodrigo = Funcionario(nome="Rodrigo Vaz", salario=2500, data_nascimento='10/01/2000')
#print(rodrigo)
#print("idade do é: {}".format(rodrigo.idade()))


def teste_idade():
    funcionario_teste = Funcionario('Funcionario teste', '17/11/1992', 1230)
    print("teste = {}".format(funcionario_teste.idade()))

teste_idade()

