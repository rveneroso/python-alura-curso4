class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome.title()

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

profecia = Filme('a profecia', 1977, 120)
profecia.dar_like()
profecia.dar_like()
print(f'O filme {profecia.nome} foi lançado em {profecia.ano}, tem a duração de {profecia.duracao} minutos e já recebeu {profecia.likes} likes')

bbt = Serie('the big bang theory',2007, 2019)
bbt.dar_like()
print(f'A série {bbt.nome} foi lançada em {bbt.ano}, tem a duração de {bbt.temporadas} temporadas e já recebeu {bbt.likes} likes')