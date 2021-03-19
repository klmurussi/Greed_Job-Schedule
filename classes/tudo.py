from classes import atividade


class Tudo:
    def __init__(self):
        self.atividades = []

    def add(self, atividade):
        self.atividades.append(atividade)

    def print(self):
        for n in self.atividades:
            print(n.nome, "horario inicial:", int(n.horarioInicial),
                  "horario final:", int(n.horarioFinal))
