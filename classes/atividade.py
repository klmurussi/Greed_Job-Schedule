from classes import dias

class Atividade :
	def __init__(self, nome, horarioInicial, horarioFinal, days):	
		self.nome = nome
		self.horarioInicial = horarioInicial
		self.horarioFinal = horarioFinal
		self.dias = days

	def print (self):
		print ("my name is " + self.nome)