from classes import atividade, tudo, dias
from pythonds import PriorityQueue
from tools import daySelector

atividades = tudo.Tudo()

while True:
    print("\nDigite o nome da atividade: ")
    nome = input()

    while True:
        print("\nDigite o horário que começa '" + nome + "':")
        horarioInicial = input()
        if int(horarioInicial) >= 0 and int(horarioInicial) <= 23:
            break

    while True:
        print("\nDigite o horário que terminar '" + nome + "':")
        horarioFinal = input()
        if int(horarioFinal) >= 0 and int(horarioFinal) <= 23:
            if int(horarioFinal) > int(horarioInicial):
                break

    days = dias.Dias()
    print("\nDias da semana que tem que ser feito:\n")
    print("1) Domingo\n2) Segunda\n3) Terça\n4) Quarta\n5) Quinta\n6) Sexta\n7) Sábado\n")
    diasString = input()
    #print (diass)
    for dia in diasString:
        if dia != ' ':
            days.add(daySelector.readDia(dia))

    schedule = atividade.Atividade(
        nome, int(horarioInicial), int(horarioFinal))

    for i in days.dias:
        atividades.add(schedule, i)

    while True:
        print("\nDeseja cadastrar outra atividade? S/N")
        resposta = input()
        if resposta == 'n' or resposta == 'N' or resposta == 'S' or resposta == 's':
            break
    if resposta == 'N' or resposta == 'n':
        break


# print(atividades.atividades)
# print("-------------------------------------")
sortedAtividades = []
for i in atividades.atividades:
    sortedAtividades.append(
        sorted(atividades.atividades[i], key=lambda x: x.horarioInicial))
# print(sortedAtividades)

""" for i in sortedAtividades:
    count += 1
    print(daySelector.selectDia(count))
    for j in i:
        print(j) """
count = 0
for j in sortedAtividades:
    funcionarios = PriorityQueue()
    qtd_funcionarios = 0
    atividadesDia = {}
    count += 1
    for i in j:
        if not funcionarios.isEmpty():
            disponivel = funcionarios.delMin()
            #print (disponivel)

        else:
            disponivel = None

        if disponivel is not None:
            if i.horarioInicial >= disponivel[0]:
                funcionarios.add(
                    (i.horarioFinal, (i.horarioFinal, disponivel[1])))
                atividadesDia[disponivel[1]].append(i)

            else:

                funcionarios.add((disponivel[0], disponivel))
                qtd_funcionarios += 1
                atividadesDia[qtd_funcionarios] = []
                funcionarios.add(
                    (i.horarioFinal, (i.horarioFinal, qtd_funcionarios)))
                atividadesDia[qtd_funcionarios].append(i)

        else:
            qtd_funcionarios += 1
            atividadesDia[qtd_funcionarios] = []
            funcionarios.add(
                (i.horarioFinal, (i.horarioFinal, qtd_funcionarios)))
            atividadesDia[qtd_funcionarios].append(i)
    print(daySelector.selectDia(count))
    print("Minímo de funcionários: " + str(qtd_funcionarios))
    for i in atividadesDia:
        print("funcionario " + str(i) + "  Atividades:")
        for j in atividadesDia[i]:
            print(j)
    print('------------------------------------------------------------------------------------------------------------------')
