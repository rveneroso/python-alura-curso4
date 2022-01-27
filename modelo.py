class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas

profecia = Filme('a profecia', 1977, 120)
print(f'O filme {profecia.nome} foi lançado em {profecia.ano} e tem a duração de {profecia.duracao} minutos')

bbt = Serie('the big bang theory',2007, 2019)
print(f'A série {bbt.nome} foi lançada em {bbt.ano} e durou {bbt.temporadas} temporadas')