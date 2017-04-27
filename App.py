import inputWindow
import outputWindow
import simulador
from PyQt4 import QtGui
import sys

class InputWindow(QtGui.QMainWindow, inputWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(InputWindow, self).__init__(parent)
        self.setupUi(self)
        self.botaoSimular.clicked.connect(self.goToOutputWindow)
        self.relatorio = OutputWindow()

    def goToOutputWindow(self):
        self.close()

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
            S = simulador.Simulador(float(self.mediaChegadaA.text()), (float(self.mediaPerfuracaoA.text()),
            float(self.desvioPerfuracaoA.text())), int(self.nMaquinasPerfuracaoA.text()),
            (float(self.mediaPolimentoA.text()), float(self.desvioPolimentoA.text())),
            int(self.nMaquinasPolimentoA.text()), float(self.mediaChegadaB.text()),
            (float(self.mediaPerfuracaoB.text()), float(self.desvioPerfuracaoB.text())),
            int(self.nMaquinasPerfuracaoB.text()), (float(self.mediaPolimentoB.text()),
            float(self.desvioPolimentoB.text())), int(self.nMaquinasPolimentoB.text()),
            (float(self.mediaEnvernizamento.text()), float(self.desvioEnvernizamento.text())),
            int(self.nMaquinasEnvernizamento.text()), i, tempo_simulação=int(self.tempoSimulacao.text()),
            n_clientes=int(self.nClientes.text()))

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
