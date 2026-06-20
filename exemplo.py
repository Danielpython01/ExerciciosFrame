"""
Arquivo para criação de objetos times (esporte)
que podem ser de vários tipos, como futebol, vôlei,
basquete etc.
"""

from os import system as lt
lt("cls")

class Clube:
    """
    Classe que herda dados de clubes de esporte de vários estilos.
    """
    # Atributos - características do objeto
    def __init__(self, nome: str, fundacao: int, cor_uniforme: str, mascote: str, modalidade: str):
        self.nome = nome
        self.fundacao = fundacao
        self.cor_uniforme = cor_uniforme
        self.mascote = mascote
        self.modalidade = modalidade
        self.campeonatos = 6
        self.jogos = 0
        self.vitorias = 0
        self.derrotas = 0

    # Métodos - ações do objeto
    def ganhar(self):
        self.vitorias += 1

    def jogar(self):
        self.jogos += 1

    def perder(self):
        self.derrotas += 1

    def trocar_uniforme(self):
        pass


time1 = Clube("São Paulo", 1930, "Branco", "Santo Paulo", "Futebol")
time2 = Clube("Capivariano", 1918, "Vermelho", "Leão", "Futebol")
time3 = Clube("Palmeiras", 1800, "Verde", "Porco", "Balé")
time4 = Clube("Flamengo", 1895, "Vermelho", "Urubu", "Futebol")
time5 = Clube("Fúria", 2017, "Preto", "Pantera", "CS2")

time1.jogar()
time2.jogar()
time1.perder()
time2.ganhar()

print(f"O time {time1.nome} tem {time1.vitorias} vitórias \
e {time1.derrotas} derrotas.")
print(f"O time {time2.nome} tem {time2.vitorias} vitórias \
e {time2.derrotas} derrotas.")

print()

