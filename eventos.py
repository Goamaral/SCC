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
		# Usado para ordenar por ordem crescente de instantes de ocorr�ncia a lista de eventos do simulador"""
		return self.instant < other.instant




class Chegada(Evento):
	# """Classe que representa a chegada de um cliente. Deriva de Evento."""
	#Construtor
	def __init__(self,i,sim):
		Evento.__init__(self,i,sim)

	def __str__(self):
		# """Método que descreve o evento.
		# Para ser usado na listagem da lista de eventos."""
		return "Chegada\t["+str(self.instant)+"]"

	def executa(self, fila):
		# """Método que executa as accoes correspondentes a chegada de um cliente"""
		#Coloca cliente no serviço - na fila ou a ser atendido, conforme o caso
		fila.insereClient(cliente.Client()) 
		#Agenda nova chegada para daqui a aleatorio.exponencial(self.simulator.media_cheg) instantes
		self.simulator.insereEvento(Chegada(self.simulator.instant+aleatorio.exponencial(self.simulator.media_cheg),self.simulator))


class Saida(Evento):
	# """Classe que representa a saída de um cliente. Deriva de Evento."""
	#Construtor
	def __init__(self,i,sim):
		Evento.__init__(self,i,sim)

	def __str__(self):
		# """Método que descreve o evento.
		# Para ser usado na listagem da lista de eventos."""
		return "Saida\t\t["+str(self.instant)+"]"

	
	def executa(self, fila):
		# """Método que executa as acoes correspondentes à saída de um cliente"""
		fila.removeClient() #Retira cliente do serviço