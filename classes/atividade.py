from classes import dias


class Atividade:
    def __init__(self, nome, horarioInicial, horarioFinal, days):
        self.nome = nome
        self.horarioInicial = horarioInicial
        self.horarioFinal = horarioFinal
        self.dias = days

    def __repr__(self):
        return repr(("nome: " + self.nome + " horario incial: " + str(self.horarioInicial)))

    def print(self):
        print("my name is " + self.nome)
