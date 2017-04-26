#!/usr/bin/env python
# encoding: utf-8
import fila
import lista
import eventos


class Simulador:
    def insereEvento(self, event):
        self.event_list.insert_event(event)

    # Construtor
    def __init__(self):
        self.n_repeticoes = None
        self.tempo_simulacao = None
        self.n_clientes = None

        # Médias das distribuições de chegadas e de atendimento no serviço
        self.media_cheg_A = None
        self.dist_perfuracao_A = None
        self.numero_maquinas_perfuracao_A = None
        self.dist_polimento_A = None
        self.numero_maquinas_polimento_A = None

        self.media_cheg_B = None
        self.dist_perfuracao_B = None
        self.numero_maquinas_perfuracao_B = None
        self.dist_polimento_B = None
        self.numero_maquinas_polimento_B = None

        self.dist_envernizamento = None
        self.numero_maquinas_envernizamento = None

        self.a_perfuracao_relat = None
        self.a_polimento_relat = None
        self.b_perfuracao_relat = None
        self.b_polimento_relat = None
        self.envernizamento_relat = None

        # Relógio de simulação - variável que contém o valor do tempo em cada instante
        self.instant = 0  # valor inicial a zero

    def setup(self):
        # Serviço - pode haver mais do que um num simulador
        # Queues for objects of type A.
        #Queues for both objects
        self.envernizamento_queue = fila.Fila(self, 2, self.dist_envernizamento, None, self.numero_maquinas_envernizamento)

        self.a_polimento_queue = fila.Fila(self, 1, self.dist_polimento_A, self.envernizamento_queue, self.numero_maquinas_polimento_A)
        self.b_polimento_queue = fila.Fila(self, 2, self.dist_polimento_B, self.envernizamento_queue, self.numero_maquinas_polimento_B)

        self.b_perfuracao_queue = fila.Fila(self, 1 , self.dist_perfuracao_B, self.b_polimento_queue, self.numero_maquinas_perfuracao_B)
        self.a_perfuracao_queue = fila.Fila(self, 1, self.dist_perfuracao_A, self.a_polimento_queue, self.numero_maquinas_perfuracao_A)

        # Lista de eventos - onde ficam registados todos os eventos que vão ocorrer na simulação
        # Cada simulador só tem uma
        self.event_list = lista.Lista(self)

        # Agendamento da primeira chegada
        # Se não for feito, o simulador não tem eventos para simular
        self.insereEvento(eventos.Chegada(self.instant, self, 'A'))
        self.insereEvento(eventos.Chegada(self.instant, self, 'B'))

    def executa(self):
        self.setup()
        """Método executivo do simulador"""
        # Enquanto não atender todos os clientes
        while (self.envernizamento_queue.atendidos < self.n_clientes):
            #print (self.event_list)  # Mostra lista de eventos - desnecessário; é apenas informativo
            event = self.event_list.remove_event()  # Retira primeiro evento (é o mais iminente) da lista de eventos
            self.instant = event.instant  # Actualiza relógio de simula��o
            self.act_stats()  # Actualiza valores estat�sticos
            event.executa()  # Executa evento
        self.relat()  # Apresenta resultados de simulação finais

    def act_stats(self):
        """Método que actualiza os valores estat�sticos do simulador"""
        self.a_perfuracao_queue.act_stats()
        self.a_polimento_queue.act_stats()
        self.b_perfuracao_queue.act_stats()
        self.b_polimento_queue.act_stats()
        self.envernizamento_queue.act_stats()

    def relat(self):
        """Método que apresenta os resultados de simula��o finais"""
        print ("\n\n------------FINAL RESULTS---------------\n")
        self.a_perfuracao_relat = self.a_perfuracao_queue.relat("Perfuracao A")
        print()
        self.a_polimento_relat = self.a_polimento_queue.relat("Polimento A")
        print()
        self.b_perfuracao_relat = self.b_perfuracao_queue.relat("Perfuracao B")
        print()
        self.b_polimento_relat = self.b_polimento_queue.relat("Polimento B")
        print()
        self.envernizamento_relat = self.envernizamento_queue.relat("Envernizamento")
