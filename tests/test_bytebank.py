import pytest
from pytest import mark
from src.bytebank import Funcionario


class TestClass:

    @mark.idade
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000'
        esperado = 22
        funcionario_test = Funcionario("Usuario teste", entrada, 2000)
        resultado = funcionario_test.idade()

        assert  resultado == esperado

    @mark.sobrenome
    def test_uando_sobrenome_recebe_Rodrigo_Vaz_deve_retornar_Vaz(self):
        entrada = ' Rodrigo Vaz '
        esperado = 'Vaz'
        funcionario_test = Funcionario(entrada, '17/11/1980', 2000)
        resultado = funcionario_test.sobrenome()

        assert esperado.__eq__(resultado)

    @mark.calcular_bonus
    def test_calcular_bonus_com_valor_maior_que_dez_mil_deve_retornar_valor_zero(self):
        with pytest.raises(Exception):
            entrada = 10100

            funcionario_test = Funcionario('Usuario test', '11/11/1987', entrada)
            resultado = funcionario_test.calcular_bonus()
            assert resultado

    @mark.calcular_bonus
    def test_calcular_bonus_com_valor_menor_que_dez_mil_deve_retornar_valor_zero(self):
        entrada = 9000
        esperado = 900
        funcionario_test = Funcionario('Usuario test', '11/11/1987', entrada)
        resultado = funcionario_test.calcular_bonus()

        assert esperado == resultado

    @mark.decrescimo_salario
    def test_quando_decrescimo_salario_recebe_cem_mil_deve_retonar_noventa_mil(self):
        entrada = 100000
        esperado = 90000
        funcionario_test = Funcionario("Test Bragança", '11/11/1598', entrada)
        funcionario_test.decrescimo_salario()
        resultado = funcionario_test.salario

        assert esperado == resultado

    def test_retorno_do_objeto_funcionario(self):
        esperado = 'Funcionario(Rodrigo Vaz, 12/11/1998, 20000)'
        funcionario_test = Funcionario('Rodrigo Vaz', '12/11/1998', 20000)
        resultado = funcionario_test.__str__()

        assert esperado == resultado