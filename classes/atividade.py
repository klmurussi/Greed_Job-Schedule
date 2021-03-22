from classes import dias


class Atividade:
    def __init__(self, nome, horarioInicial, horarioFinal):
        self.nome = nome
        self.horarioInicial = horarioInicial
        self.horarioFinal = horarioFinal

    def __repr__(self):
        return repr(("nome: " + self.nome + " horario incial: " + str(self.horarioInicial) + " horario final: " + str(self.horarioFinal)))

    def print(self):
        print("my name is " + self.nome)
