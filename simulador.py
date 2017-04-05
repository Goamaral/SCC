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
        self.media_cheg = 1
        self.media_serv = 1.5
        # Numero de clientes que vão ser atendidos
        self.n_clientes = 100

        # Relógio de simulação - variável que contém o valor do tempo em cada instante
        self.instant = 0  # valor inicial a zero

        # Serviço - pode haver mais do que um num simulador
        self.client_queue = fila.Fila(self)
        # Lista de eventos - onde ficam registados todos os eventos que vão ocorrer na simulação
        # Cada simulador só tem uma
        self.event_list = lista.Lista(self)

        # Agendamento da primeira chegada
        # Se não for feito, o simulador não tem eventos para simular
        self.insereEvento(eventos.Chegada(self.instant, self))

    def executa(self):
        """Método executivo do simulador"""
        # Enquanto não atender todos os clientes
        while (self.client_queue.atendidos < self.n_clientes):
            print (self.event_list)  # Mostra lista de eventos - desnecessário; é apenas informativo
            event = self.event_list.remove_event()  # Retira primeiro evento (é o mais iminente) da lista de eventos
            self.instant = event.instant  # Actualiza relógio de simula��o
            self.act_stats()  # Actualiza valores estat�sticos
            event.executa(self.client_queue)  # Executa evento
        self.relat()  # Apresenta resultados de simulação finais

    def act_stats(self):
        """Método que actualiza os valores estat�sticos do simulador"""
        self.client_queue.act_stats()

    def relat(self):
        """Método que apresenta os resultados de simula��o finais"""
        print ("\n\n------------FINAL RESULTS---------------\n\n")
        self.client_queue.relat()


# programa principal

# Cria um simulador e
s = Simulador()
# põe-o em marcha
s.executa()
