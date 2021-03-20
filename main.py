from classes import atividade, tudo, dias
from pythonds import PriorityQueue

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
    #print (days.dias)
    print("\nDias da semana que tem que ser feito:\n")
    print("1) Domingo\n2) Segunda\n3) Terça\n4) Quarta\n5) Quinta\n6) Sexta\n7) Sábado\n")
    diass = input()
    #print (diass)
    for dia in diass:
        if dia == '1':
            days.add(1)

        if dia == '2':
            days.add(2)

        if dia == '3':
            days.add(3)

        if dia == '4':
            days.add(4)

        if dia == '5':
            days.add(5)

        if dia == '6':
            days.add(6)

        if dia == '7':
            days.add(7)

    #print (days.dias)

    schedule = atividade.Atividade(
        nome, int(horarioInicial), int(horarioFinal), days)

    atividades.add(schedule)

    while True:
        print("\nDeseja cadastrar outra atividade? S/N")
        resposta = input()
        if resposta == 'n' or resposta == 'N' or resposta == 'S' or resposta == 's':
            break
    if resposta == 'N' or resposta == 'n':
        break


#print(atividades.atividades)
#print("-------------------------------------")
sortedAtividades = sorted(
    atividades.atividades, key=lambda x: x.horarioInicial)
#print(sortedAtividades)


funcionarios = PriorityQueue()
qtd_funcionarios = 0

for i in sortedAtividades:
    if not funcionarios.isEmpty():
        disponivel = funcionarios.delMin()
        #print (disponivel)

    else:
        disponivel = None

    if disponivel is not None:
        if i.horarioInicial >= disponivel[0]:
            funcionarios.add((i.horarioFinal, (i.horarioFinal, disponivel[1])))

        else:
            qtd_funcionarios = qtd_funcionarios + 1
            funcionarios.add((i.horarioFinal, (i.horarioFinal, qtd_funcionarios)))

    else:
            qtd_funcionarios = qtd_funcionarios + 1
            funcionarios.add((i.horarioFinal, (i.horarioFinal, qtd_funcionarios)))

print (qtd_funcionarios)