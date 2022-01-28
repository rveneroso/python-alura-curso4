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

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    #
    # De maneira análoga ao que foi feito com o método __getitem__ para tornar um objeto Playlist iterable, o método __len__ torna as instâncias
    # de Playlist objetos sized. Com isso essas instâncias podem ser passadas diretamente como argumentos da função len().
    #
    def __len__(self):
        return len(self._programas)

    #
    # O método __getitem___ dá a um objeto do tipo Playlist a capacidade de se comportar parcialmente como um objeto list. Diferentemente do que
    # aconteceu quando Playlist estendia diretamente de list, não são todas as funcionalidades de list que estarão presentes em Playlist.
    # Com a implementação do método __getitem__ agora já é possível executar comandos for in e in diretamente em um objeto do tipo Playlist sem
    # a necessidade de outras implementações.
    # Essa técnica é conhecida como 'Duck typing'.
    #
    def __getitem__(self, item):
        return self._programas[item]
#
# Bloco para teste das classes criadas acima.
#
profecia = Filme('a profecia', 1977, 120)
bbt = Serie('the big bang theory',2007, 12)
friends = Serie('Friends',1994,10)
total_recall = Filme('o vingador do futuro', 1990, 113)

profecia.dar_like()
profecia.dar_like()
profecia.dar_like()
profecia.dar_like()
profecia.dar_like()
total_recall.dar_like()
total_recall.dar_like()
total_recall.dar_like()


bbt.dar_like()
bbt.dar_like()
bbt.dar_like()
bbt.dar_like()
bbt.dar_like()
bbt.dar_like()
bbt.dar_like()

friends.dar_like()
friends.dar_like()
friends.dar_like()

filmes_e_series = [profecia, bbt, friends,total_recall]
playlist_fim_de_semana = Playlist('Fim de Semana',filmes_e_series)


#
# Como agora Playlist herda de list, a iteração pode ser feita diretamente sem a necessidade de acesso a nenhum atributo específico da classe
# Playlist. Além disso, o tamanho da lista de programas e séries contidos na instância de Playlist também pode ser obtido diretamente através
# da função len() sem a necessidade de existir um atributo específico para conter essa informação.
#
print(f'A playlist {playlist_fim_de_semana.nome} possui {len(playlist_fim_de_semana)} filmes e/ou séries')

for programa in playlist_fim_de_semana:
    print(programa)

#
# Outro recurso herdado de list é a capacidade de verificar se a playlist contém um determinado filme ou série
#
print(f'O filme {profecia.nome} está na playlist {playlist_fim_de_semana.nome}? {profecia in playlist_fim_de_semana}')