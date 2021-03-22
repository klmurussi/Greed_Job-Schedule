# Questão 7

A estratégia gananciosa escolhida para solucionar o problema é:

1. Inicialmente ordene inversamente as atividades por f. Isso se deve ao fato de que independente da ordem de p, todas as atividades passarão pelo super computador, porém quanto mais cedo uma tarefa é inserida no PC's, mais tempo ela ficará lá, logo, para otimizar o tempo, as atividades que precisam de maior tempo nos PC's devem ser as primeiras.
2. Insira as atividades no super-computador a partir da ordenação.

Exemplo de pseudo-código baseado em python:
  ```python3
  atividadesOrdenadas = sorted(atividades, key=lambda x: x.f, reverse=True)
  for i in atividadesOrdenadas:
    i.insertInSuper();
    i.insertInPC();
  ```