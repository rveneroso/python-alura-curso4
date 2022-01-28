class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

#
# A classe Hipster é aquilo que em Python é chamado MIXIN
#
class Hipster:
    def __str__(self):
        #
        # A classe Hipster assume que quem herdar dela terá um atributo 'nome'. A linha abaixo faz uso dessa
        # suposição.
        #
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura,Caelum):
    pass

class Senior(Alura, Caelum, Hipster):
    pass

jose = Junior('José Matoma')
jose.mostrar_tarefas()


luan = Pleno('Luan Terior')
luan.busca_cursos_do_mes()
luan.mostrar_tarefas()

ruan = Senior('Ruan Darilho')
print(ruan)