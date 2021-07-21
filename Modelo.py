class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, novo_ano):
        self._ano = novo_ano

    @property
    def likes(self):
        return self._likes

    def like(self):
        self._likes += 1


class Filme(Programa):

    def __init__(self, nome, ano, duração):
        super().__init__(nome, ano)
        self._duração = duração

    @property
    def duração(self):
        return self._duração

    @duração.setter
    def duração(self, nova_duração):
        self._duração = nova_duração

    def __str__(self):
        return f"O filme {self._nome} estreou em {self._ano} e tem {self._duração} minutos de duração."


class Série(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas

    @property
    def temporadas(self):
        return self._temporadas

    @temporadas.setter
    def temporadas(self, novas_temporadas):
        self._temporadas = novas_temporadas

    def __str__(self):
        return f"A série {self._nome} estreou em {self._ano} e possui {self._temporadas} temporadas."


class Playlist():

    def __init__(self, nome, programas):
        self._nome = nome.title()
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)


Vingadores = Filme("Vingadores", 2012, 144)
Atlanta = Série("Atlanta", 2016, 2)
filmes_e_séries = [Vingadores, Atlanta]
fim_de_semana = Playlist("fim de semana", filmes_e_séries)
print(f"\nA playlist {fim_de_semana._nome} possui {len(fim_de_semana)} shows")
for show in fim_de_semana:
    print(f"\n{show}")
