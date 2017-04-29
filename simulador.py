    #!/usr/bin/env python
# encoding: utf-8
import fila
import lista
import eventos
import aleatorio

class Simulador:
    def insereEvento(self, event):
        self.event_list.insert_event(event)

    # Construtor
    def __init__(self, media_cheg_A, dist_perfuracao_A, numero_maquinas_perfuracao_A, dist_polimento_A,
                numero_maquinas_polimento_A, media_cheg_B, dist_perfuracao_B, numero_maquinas_perfuracao_B,
                dist_polimento_B, numero_maquinas_polimento_B, dist_envernizamento, numero_maquinas_envernizamento,
                repeticao_i, tempo_simulacao=0, n_clientes=None):

        self.tempo_simulacao = tempo_simulacao
        self.n_clientes = n_clientes

        # Médias das distribuições de chegadas e de atendimento no serviço
        self.media_cheg_A = media_cheg_A
        self.dist_perfuracao_A = dist_perfuracao_A
        self.numero_maquinas_perfuracao_A = numero_maquinas_perfuracao_A
        self.dist_polimento_A = dist_polimento_A
        self.numero_maquinas_polimento_A = numero_maquinas_polimento_A

        self.media_cheg_B = media_cheg_B
        self.dist_perfuracao_B = dist_perfuracao_B
        self.numero_maquinas_perfuracao_B = numero_maquinas_perfuracao_B
        self.dist_polimento_B = dist_polimento_B
        self.numero_maquinas_polimento_B = numero_maquinas_polimento_B

        self.dist_envernizamento = dist_envernizamento
        self.numero_maquinas_envernizamento = numero_maquinas_envernizamento

        self.a_perfuracao_relat = None
        self.a_polimento_relat = None
        self.b_perfuracao_relat = None
        self.b_polimento_relat = None
        self.envernizamento_relat = None

        # Relógio de simulação - variável que contém o valor do tempo em cada instante
        self.instant = 0  # valor inicial a zero

        #Numero da corrida - vai influenciar nos numeros aleatorios
        self.repeticao_i = repeticao_i

    def setup(self):
        # Serviço - pode haver mais do que um num simulador
        # Queues for objects of type A.
        #Queues for both objects

        aleatorio.Random.reset_stream_count()

        self.envernizamento_queue = fila.Fila(self, 2, self.dist_envernizamento, None, self.numero_maquinas_envernizamento, 100000+1000000*self.repeticao_i)

        self.a_polimento_queue = fila.Fila(self, 1, self.dist_polimento_A, self.envernizamento_queue, self.numero_maquinas_polimento_A, 200000+1000000*self.repeticao_i)
        self.b_polimento_queue = fila.Fila(self, 2, self.dist_polimento_B, self.envernizamento_queue, self.numero_maquinas_polimento_B, 300000+1000000*self.repeticao_i)

        self.b_perfuracao_queue = fila.Fila(self, 1 , self.dist_perfuracao_B, self.b_polimento_queue, self.numero_maquinas_perfuracao_B, 400000+1000000*self.repeticao_i)
        self.a_perfuracao_queue = fila.Fila(self, 1, self.dist_perfuracao_A, self.a_polimento_queue, self.numero_maquinas_perfuracao_A, 500000+1000000*self.repeticao_i)

        # Lista de eventos - onde ficam registados todos os eventos que vão ocorrer na simulação
        # Cada simulador só tem uma
        self.event_list = lista.Lista(self)

        # Agendamento da primeira chegada
        # Se não for feito, o simulador não tem eventos para simular
        r1 = aleatorio.Random(600000+1000000*self.repeticao_i)
        r2 = aleatorio.Random(700000+1000000*self.repeticao_i)
        self.insereEvento(eventos.Chegada(self.instant, self, 'A', r1))
        self.insereEvento(eventos.Chegada(self.instant, self, 'B', r2))

    def executa(self):
        self.setup()
        """Método executivo do simulador"""
        # Simulador limitado pelo numero de clientes
        if self.n_clientes != None:
            # Enquanto não atender todos os clientes
            while (self.envernizamento_queue.atendidos < self.n_clientes):
                #print (self.event_list)  # Mostra lista de eventos - desnecessário; é apenas informativo
                event = self.event_list.remove_event()  # Retira primeiro evento (é o mais iminente) da lista de eventos
                self.instant = event.instant  # Actualiza relógio de simula��o
                self.act_stats()  # Actualiza valores estat�sticos
                event.executa()  # Executa evento
            self.relat()  # Apresenta resultados de simulação finais
        # Simulador limitado pelo tempo
        else:
            while (self.instant < self.tempo_simulacao):
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
        self.a_perfuracao_relat = self.a_perfuracao_queue.relat("Perfuracao A")
        self.a_polimento_relat = self.a_polimento_queue.relat("Polimento A")
        self.b_perfuracao_relat = self.b_perfuracao_queue.relat("Perfuracao B")
        self.b_polimento_relat = self.b_polimento_queue.relat("Polimento B")
        self.envernizamento_relat = self.envernizamento_queue.relat("Envernizamento")
