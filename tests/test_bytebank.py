from bytebank import Funcionario

class TestClass:

    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000'
        esperado = 22
        funcionario_test = Funcionario("Usuario teste", entrada, 2000)
        resultado = funcionario_test.idade()

        assert  resultado == esperado

    def test_uando_sobrenome_recebe_Rodrigo_Vaz_deve_retornar_Vaz(self):
        entrada = ' Rodrigo Vaz '
        esperado = 'Vaz'
        funcionario_test = Funcionario(entrada, '17/11/1980', 2000)
        resultado = funcionario_test.sobrenome()

        assert esperado.__eq__(resultado)

