import inputWindow
import outputWindow
import simulador
from PyQt4 import QtGui
import sys

default_params = True

class InputWindow(QtGui.QMainWindow, inputWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(InputWindow, self).__init__(parent)
        self.setupUi(self)
        self.botaoSimular.clicked.connect(self.goToOutputWindow)
        self.relatorio = OutputWindow()

    def goToOutputWindow(self):
        self.close()

        if default_params:
            media_cheg_A = 5
            dist_perfuracao_A = (2, 0.7)
            numero_maquinas_perfuracao_A = 1
            dist_polimento_A = (4, 1.2)
            numero_maquinas_polimento_A = 1

            media_cheg_B = 1.33
            dist_perfuracao_B = (0.75, 0.3)
            numero_maquinas_perfuracao_B = 1
            dist_polimento_B = (3, 1)
            numero_maquinas_polimento_B = 2

            dist_envernizamento = (1.4, 0.3)
            numero_maquinas_envernizamento = 2

            n_clientes = 100
            tempo_simulacao = None
        else:
            media_cheg_A = float(self.mediaChegadaA.text())
            dist_perfuracao_A = (float(self.mediaPerfuracaoA.text()), float(self.desvioPerfuracaoA.text()))
            numero_maquinas_perfuracao_A = int(self.nMaquinasPerfuracaoA.text())
            dist_polimento_A = (float(self.mediaPolimentoA.text()), float(self.desvioPolimentoA.text()))
            numero_maquinas_polimento_A = int(self.nMaquinasPolimentoA.text())

            media_cheg_B = float(self.mediaChegadaB.text())
            dist_perfuracao_B = (float(self.mediaPerfuracaoB.text()), float(self.desvioPerfuracaoB.text()))
            numero_maquinas_perfuracao_B = int(self.nMaquinasPerfuracaoB.text())
            dist_polimento_B = (float(self.mediaPolimentoB.text()), float(self.desvioPolimentoB.text()))
            numero_maquinas_polimento_B = int(self.nMaquinasPolimentoB.text())

            dist_envernizamento = (float(self.mediaEnvernizamento.text()), float(self.desvioEnvernizamento.text()))
            numero_maquinas_envernizamento = int(self.nMaquinasEnvernizamento.text())

            n_clientes = int(self.nClientes.text())
            tempo_simulacao = int(self.tempoSimulacao.text())

        n_repeticoes = int(self.nRepeticoes.text())

        sum_media_espera_a_perfuracao = 0
        sum_utilizacao_a_perfuracao = 0
        sum_media_espera_a_polimento = 0
        sum_utilizacao_a_polimento = 0
        sum_media_espera_b_perfuracao = 0
        sum_utilizacao_b_perfuracao = 0
        sum_media_espera_b_polimento = 0
        sum_utilizacao_b_polimento = 0
        sum_media_espera_envernizamento = 0
        sum_utilizacao_envernizamento = 0
        sum_clientes_atendidos = 0

        for i in range(n_repeticoes):
            S = simulador.Simulador(media_cheg_A, dist_perfuracao_A, numero_maquinas_perfuracao_A,
            dist_polimento_A, numero_maquinas_polimento_A, media_cheg_B, dist_perfuracao_B,
            numero_maquinas_perfuracao_B, dist_perfuracao_B, numero_maquinas_polimento_B,
            dist_polimento_B, numero_maquinas_polimento_B, i, tempo_simulacao, n_clientes)

            S.executa()

            sum_media_espera_a_perfuracao += S.a_perfuracao_relat["mediaEspera"]
            sum_utilizacao_a_perfuracao += S.a_perfuracao_relat["utilizacao"]
            sum_media_espera_a_polimento += S.a_polimento_relat["mediaEspera"]
            sum_utilizacao_a_polimento += S.a_polimento_relat["utilizacao"]

            sum_media_espera_b_perfuracao += S.b_perfuracao_relat["mediaEspera"]
            sum_utilizacao_b_perfuracao += S.b_perfuracao_relat["utilizacao"]
            sum_media_espera_b_polimento += S.b_polimento_relat["mediaEspera"]
            sum_utilizacao_b_polimento += S.b_polimento_relat["utilizacao"]

            sum_media_espera_envernizamento += S.envernizamento_relat["mediaEspera"]
            sum_utilizacao_envernizamento += S.envernizamento_relat["utilizacao"]

            sum_clientes_atendidos += S.envernizamento_relat["nClientesAtendidos"]

        media_espera_a_perfuracao += sum_media_espera_a_perfuracao / n_repeticoes
        media_utilizacao_a_perfuracao += sum_utilizacao_a_perfuracao / n_repeticoes
        media_espera_a_polimento += sum_media_espera_a_polimento / n_repeticoes
        media_utilizacao_a_polimento += sum_utilizacao_a_polimento / n_repeticoes

        media_espera_b_perfuracao = sum_media_espera_b_perfuracao / n_repeticoes
        media_utilizacao_b_perfuracao = sum_utilizacao_b_perfuracao / n_repeticoes
        media_espera_b_polimento = sum_media_espera_b_polimento / n_repeticoes
        media_utilizacao_b_polimento = sum_utilizacao_b_polimento / n_repeticoes

        media_utilizacao_envernizamento = sum_utilizacao_envernizamento / n_repeticoes
        media_espera_envernizamento = sum_media_espera_envernizamento / n_repeticoes

        media_clientes_atendidos = sum_clientes_atendidos / n_repeticoes

        self.relatorio.mEsperaPerfuracaoA.setText(str(media_espera_a_perfuracao))
        self.relatorio.utilPerfuracaoA.setText(str(media_utilizacao_a_perfuracao))
        self.relatorio.mEsperaPolimentoA.setText(str(media_espera_a_polimento))
        self.relatorio.utilPolimentoA.setText(str(media_utilizacao_a_polimento))
        self.relatorio.mEsperaPerfuracaoB.setText(str(media_espera_b_perfuracao))
        self.relatorio.utilPerfuracaoB.setText(str(media_utilizacao_b_perfuracao))
        self.relatorio.mEsperaPolimentoB.setText(str(media_espera_b_polimento))
        self.relatorio.utilPolimentoB.setText(str(media_utilizacao_b_polimento))
        self.relatorio.mEsperaEnvernizamento.setText(str(media_espera_envernizamento))
        self.relatorio.utilEnvernizamento.setText(str(media_utilizacao_envernizamento))
        self.relatorio.clientesAtendidos.setText(str(media_clientes_atendidos))
        #MEDIA DISTO TAMBEM SO SE FIZERMOS PARA O NUMERO DE CLIENTES

        self.relatorio.tempoSimulacao.setText(str(S.instant))
        self.relatorio.show()

class OutputWindow(QtGui.QMainWindow, outputWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(OutputWindow, self).__init__(parent)
        self.setupUi(self)


def main():
    app = QtGui.QApplication(sys.argv)
    descricaoSimulacao = InputWindow()
    descricaoSimulacao.show()
    app.exec_()


if __name__ == '__main__':
    main()
