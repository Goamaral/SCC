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
        # Médias das distribuições de chegadas e de atendimento no serviço
        self.media_cheg_A = 5
        self.dist_perfuracao_A = (2, 0.7)
        self.dist_polimento_A = (4, 1.2)

        self.media_cheg_B = 1.33
        self.dist_perfuracao_B = (0.75, 0.3)
        self.dist_polimento_B = (3, 1)

        self.dist_envernizamento = (1.4, 0.3)
        # Numero de clientes que vão ser atendidos
        self.n_clientes = 100

        # Relógio de simulação - variável que contém o valor do tempo em cada instante
        self.instant = 0  # valor inicial a zero

        # Serviço - pode haver mais do que um num simulador
        # Queues for objects of type A.
        #Queues for both objects
        self.envernizamento_queue = fila.Fila(self, 2, self.dist_envernizamento, None)

        self.a_polimento_queue = fila.Fila(self, 1, self.dist_polimento_A, self.envernizamento_queue)
        self.b_polimento_queue = fila.Fila(self, 2, self.dist_polimento_B, self.envernizamento_queue)

        self.b_perfuracao_queue = fila.Fila(self, 1 , self.dist_perfuracao_B, self.b_polimento_queue)
        self.a_perfuracao_queue = fila.Fila(self, 1, self.dist_perfuracao_A, self.a_polimento_queue)

        # Lista de eventos - onde ficam registados todos os eventos que vão ocorrer na simulação
        # Cada simulador só tem uma
        self.event_list = lista.Lista(self)

        # Agendamento da primeira chegada
        # Se não for feito, o simulador não tem eventos para simular
        self.insereEvento(eventos.Chegada(self.instant, self, 'A'))
        self.insereEvento(eventos.Chegada(self.instant, self, 'B'))

    def executa(self):
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
        self.envernizamento_queue.act_stats()

    def relat(self):
        """Método que apresenta os resultados de simula��o finais"""
        print ("\n\n------------FINAL RESULTS---------------\n")
        self.a_perfuracao_queue.relat("Perfuracao A")
        print()
        self.a_polimento_queue.relat("Polimento A")
        print()
        self.b_perfuracao_queue.relat("Perfuracao B")
        print()
        self.b_polimento_queue.relat("Polimento B")
        print()
        self.envernizamento_queue.relat("Envernizamento")


# programa principal

# Cria um simulador e
s = Simulador()
# põe-o em marcha
s.executa()
