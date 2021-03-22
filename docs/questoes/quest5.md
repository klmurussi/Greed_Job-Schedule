# Questão 5

Pense nas casas como n pontos em uma linha na ordem da esquerda para direita, Hi é o número da posição em milhas da casa até a linha.
	```
	H = [H1, H2, H3, H4, ..., Hn]
	```
E a base das estações é um outro ponto k na mesma linha. Pj é um número da posição em milhas das bases de estação até a linha
	```
	P = [P1, P2, P3, P4, ... , Pn]
	```
A solução é possível se cada ponto Hi está a 4 milhas de um ponto Pj. A estratégia ganaciosa é colocar P1 exatamente 4 milhas a direita de H1, remover todas as casa cobertas por P1, dentro de 4 milhas de P1, e então recursivamente resolver o sub-problema que contém o resto das casas.
	```python3
	def bases (H, P):
		if H is None:
			return P
		else: 
			Pj is exctly four miles to the right of H1
			P.append(Pj)
			for i in H:
				if i < Pj + 4 miles:
					remove i from H
			return bases (H, P)
	```