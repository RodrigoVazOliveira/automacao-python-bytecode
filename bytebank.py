from datetime import date


class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nascimento_quebrado = self._data_nascimento.split('/')
        ano_nascimento = data_nascimento_quebrado[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            valor = 0
        return valor

    def sobrenome(self):
        nome_completo = self.nome.strip()
        nome_quebrado = nome_completo.split()

        return nome_quebrado[-1]

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'

    def decrescimo_salario(self):
        if self._validar_decrescimo():
            decrescimo = self._salario * 0.1
            self._salario -= decrescimo

    def _validar_decrescimo(self):
        return self._salario >= 100000 and self._verificar_se_sobrenome_e_da_diretoria()

    def _verificar_se_sobrenome_e_da_diretoria(self):
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return self.sobrenome() in sobrenomes