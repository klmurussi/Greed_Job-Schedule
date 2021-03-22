from classes import atividade


class Tudo:
    def __init__(self):
        self.atividades = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}

    def add(self, atividade, dia):
        self.atividades[dia].append(atividade)

    def print(self):
        for n in self.atividades:
            print(n.nome, "horario inicial:", int(n.horarioInicial),
                  "horario final:", int(n.horarioFinal))
