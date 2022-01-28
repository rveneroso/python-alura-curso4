class Programa:
    def __init__(self, nome, ano):
        #
        # Em Python, um único underline (_) à frente do nome do atributo indica que o atributo é protected.
        #
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self._likes = 0

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        self._nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self._likes = 0

profecia = Filme('a profecia', 1977, 120)
profecia.dar_like()
profecia.dar_like()
print(f'O filme {profecia.nome} foi lançado em {profecia.ano}, tem a duração de {profecia.duracao} minutos e já recebeu {profecia.likes} likes')

bbt = Serie('the big bang theory',2007, 2019)
bbt.dar_like()
print(f'A série {bbt.nome} foi lançada em {bbt.ano}, tem a duração de {bbt.temporadas} temporadas e já recebeu {bbt.likes} likes')