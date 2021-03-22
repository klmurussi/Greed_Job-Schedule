# Algoritmo do programa

1. Inicialmente é utilizado uma loop que recebe as entradas do usuário, e essas entradas são armazenadas. 
  ```python3
  while True:
    print("\nDigite o nome da atividade: ")
    nome = input()

    while True:
        print("\nDigite o horário que começa '" + nome + "':")
        horarioInicial = input()
        if int(horarioInicial) >= 0 and int(horarioInicial) <= 23:
            break
    .
    .
    .
  ```
  Cada atividade é armazenada em um objeto do tipo Atividade
  ```python3
  class Atividade:
    def __init__(self, nome, horarioInicial, horarioFinal):
        self.nome = nome
        self.horarioInicial = horarioInicial
        self.horarioFinal = horarioFinal
  ```
  E todos as atividades são armazenadas em um objeto de tipo Tudo, e cada atividade é discrimida pelo dia da semana
  ```python3
  class Tudo:
    def __init__(self):
        self.atividades = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}

    def add(self, atividade, dia):
        self.atividades[dia].append(atividade)
  ```
2. Apṍs isso, para todos dias das semana, a lista que contém as atividades que os funcionários terão que fazer são ordenadas a partir do horário inicial
  ```python3
  sortedAtividades = []
  for i in atividades.atividades:
      sortedAtividades.append(
          sorted(atividades.atividades[i], key=lambda x: x.horarioInicial))
  ```
3. Após isso, para cada dia da semana é utilizado o algoritmo ganancioso "interval partioning" para utilizar o mínimo de fucionários possíveis para realizar as atividades previamente inseridas, além disso, são registradas as atividades de cada funcionário
  ```python3
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
  ```
4. Por último é impresso no terminal o dia, o minímo de funcionários para aquele dia, e as atividades que cada funcionário deve realizar
  ```python3
  print(daySelector.selectDia(count))
    print("Minímo de funcionários: " + str(qtd_funcionarios))
    for i in atividadesDia:
        print("funcionario " + str(i) + "  Atividades:")
        for j in atividadesDia[i]:
            print(j)
  ```


