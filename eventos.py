#!/usr/bin/env python
# encoding: utf-8
import cliente
import aleatorio

class Evento:
	# """Classe de onde vão ser derivados todos os eventos.
	# Contem apenas os atributos e métodos comuns a todos os eventos.
	# Não haverá instâncias desta classe num simulador."""

	#construtor
	def __init__(self,i,sim):
		self.instant = i		#Instante de ocorrencia do evento
		self.simulator = sim	#Simulador onde ocorre o evento


	def __lt__(self, other):
		# """Método de comparação entre dois eventos.
		# Determina se o evento corrente ocorre primeiro, ou não, do que o evento e1
		# Se sim, devolve true; se não, devolve false
		# Usado para ordenar por ordem crescente de instantes de ocorrência a lista de eventos do simulador"""
		return self.instant < other.instant

class Chegada(Evento):
	# """Classe que representa a chegada de um cliente. Deriva de Evento."""
	#Construtor
	def __init__(self,i,sim,tipo, random_generator):
		Evento.__init__(self,i,sim)
		self.tipo = tipo
		self.random_generator = random_generator

	def __str__(self):
		# """Método que descreve o evento.
		# Para ser usado na listagem da lista de eventos."""
		return "Chegada\t["+str(self.instant)+"]"

	def executa(self):
		# """Método que executa as accoes correspondentes a chegada de um cliente"""
		#Coloca cliente no serviço - na fila ou a ser atendido, conforme o caso
		if self.tipo == 'A':
			self.simulator.a_perfuracao_queue.insereClient(cliente.Client("A"))
			self.simulator.insereEvento(Chegada(self.simulator.instant+self.random_generator.exponencial(self.simulator.media_cheg_A),self.simulator, self.tipo, self.random_generator))
		elif self.tipo == 'B':
			self.simulator.b_perfuracao_queue.insereClient(cliente.Client("B"))
			self.simulator.insereEvento(Chegada(self.simulator.instant+self.random_generator.exponencial(self.simulator.media_cheg_B),self.simulator, self.tipo, self.random_generator))
			#Agenda nova chegada para daqui a aleatorio.exponencial(self.simulator.media_cheg) instantes


class Saida(Evento):
	def __init__(self,i,sim,fila):
		Evento.__init__(self,i,sim)
		self.fila = fila

	def __str__(self):
		# """Método que descreve o evento.
		# Para ser usado na listagem da lista de eventos."""
		return "Saida\t["+str(self.instant)+"]"

	def executa(self):
		cliente = self.fila.removeClient()
		if self.fila.prox_fila != None:
			self.fila.prox_fila.insereClient(cliente)
		else:
			pass
