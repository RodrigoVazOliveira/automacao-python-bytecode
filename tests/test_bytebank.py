from bytebank import Funcionario

class TestClass:

    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000'
        esperado = 22
        funcionario_test = Funcionario("Usuario teste", entrada, 2000)
        resultado = funcionario_test.idade()

        assert  resultado == esperado