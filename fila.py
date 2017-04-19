#!/usr/bin/env python
# encoding: utf-8
import eventos
import aleatorio


class Fila:
    # """Classe que representa um serviço com uma fila de espera associada"""

    # Construtor
    def __init__(self, sim, n_servicos, dist, prox_fila):
        self.fila = []  # Fila de espera do serviço
        self.servico = [] #Lista de Tuplos (cliente, tempo_de_saida) no serviço
        self.n_servicos = n_servicos
        self.simulator = sim  # Referência para o simulador a que pertence o servi�o
        self.estado = 0  # Variável que regista o estado do serviço: 0 - livre; 1 - ocupado
        self.temp_last = sim.instant  # Tempo que passou desde o último evento. Neste caso 0, porque a simulação ainda não começou.
        self.atendidos = 0  # Número de clientes atendidos até ao momento
        self.soma_temp_esp = 0
        self.soma_temp_serv = 0
        self.prox_fila = prox_fila
        self.dist = dist

    def insereClient(self, client):
        # """Método que insere cliente (client) no serviço"""
        if len(self.servico) < self.n_servicos:  # Se serviço livre,
            tempo_de_saida = self.simulator.instant + aleatorio.normal(self.dist)
            self.servico.append((client, tempo_de_saida))
            sorted(self.servico, key=lambda servico: servico[1], reverse=True)
            self.simulator.insereEvento(
                eventos.Saida(tempo_de_saida, self.simulator, self))
        else:
            self.fila.append(client)  # Se serviço ocupado, o cliente vai para a fila de espera

    def removeClient(self):
        # """Método que remove cliente do serviço"""
        self.atendidos = self.atendidos + 1  # Regista que acabou de atender + 1 cliente
        cliente = self.servico.pop()
        if len(self.fila) > 0:
            self.insereClient(self.fila.pop(0))
        return cliente

    def act_stats(self):
        # """Método que calcula valores para estatísticas, em cada passo da simulação ou evento"""
        # Calcula tempo que passou desde o último evento
        temp_desd_ult = self.simulator.instant - self.temp_last
        # Actualiza variável para o próximo passo/evento
        self.temp_last = self.simulator.instant
        # Contabiliza tempo de espera na fila
        # para todos os clientes que estiveram na fila durante o intervalo
        self.soma_temp_esp = self.soma_temp_esp + (len(self.fila) * temp_desd_ult)
        # Contabiliza tempo de atendimento
        estado = len(self.servico) / self.n_servicos
        self.soma_temp_serv = self.soma_temp_serv + (estado * temp_desd_ult)

    def relat(self, nome):
        # """Método que calcula valores finais estatísticos"""
        # Tempo médio de espera na fila
        temp_med_fila = self.soma_temp_esp / (self.atendidos + len(self.fila))
        # Comprimento médio da fila de espera
        # self.simulator.instant neste momento � o valor do tempo de simulação,
        # uma vez que a simulação come�ou em 0 e este método só é chamdao no fim da simulação
        comp_med_fila = self.soma_temp_esp / self.simulator.instant
        # Tempo m�dio de atendimento no serviço
        utilizacao_serv = self.soma_temp_serv / self.simulator.instant

        # Apresenta resultados
        print("Relatorio: %s"%(nome,))
        print("Tempo medio de espera", temp_med_fila)
        print("Comp. medio da fila", comp_med_fila)
        print("Utilizacao do servico", utilizacao_serv)
        print("Tempo de simulacao", self.simulator.instant)
        print("Numero de clientes atendidos", self.atendidos)
        print("Numero de clientes na fila", len(self.fila))
