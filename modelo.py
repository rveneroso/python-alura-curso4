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

    #
    # O método __str__ é o equivalente ao toString() do Java.
    #
    def __str__(self):
         return f'{self._nome} - {self.ano} - {self._likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        #
        # No caso de uma chamada ao construtor da superclasse não há a necessidade de se passar o objeto self; o Python consegue identificar
        # automaticamente qual instância está fazendo a chamada à superclasse.
        #
        super().__init__(nome,ano)
        self.duracao = duracao
        
    #
    # O método __str__ é o equivalente ao toString() do Java.
    #
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} minutos - {self._likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        #
        # No caso de uma chamada ao construtor da superclasse não há a necessidade de se passar o objeto self; o Python consegue identificar
        # automaticamente qual instância está fazendo a chamada à superclasse.
        #
        super().__init__(nome,ano)
        self.temporadas = temporadas

    #
    # O método __str__ é o equivalente ao toString() do Java.
    #
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes}'
#
# Bloco para teste das classes criadas acima.
#
profecia = Filme('a profecia', 1977, 120)
profecia.dar_like()
profecia.dar_like()
#print(f'{profecia.nome} - {profecia.ano} - {profecia.duracao} : {profecia.likes}')

bbt = Serie('the big bang theory',2007, 12)
bbt.dar_like()
#print(f'{bbt.nome} - {bbt.ano} - {bbt.temporadas} : {bbt.likes}')

filmes_e_series = [profecia, bbt]
for programa in filmes_e_series:
    print(programa)