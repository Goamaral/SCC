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
        S = simulador.Simulador()

        if default_params:
            S.media_cheg_A = 5
            S.dist_perfuracao_A = (2, 0.7)
            S.numero_maquinas_perfuracao_A = 1
            S.dist_polimento_A = (4, 1.2)
            S.numero_maquinas_polimento_A = 1

            S.media_cheg_B = 1.33
            S.dist_perfuracao_B = (0.75, 0.3)
            S.numero_maquinas_perfuracao_B = 1
            S.dist_polimento_B = (3, 1)
            S.numero_maquinas_polimento_B = 2

            S.dist_envernizamento = (1.4, 0.3)
            S.numero_maquinas_envernizamento = 2

            S.n_clientes = 100
            S.tempo_simulacao = None
            S.n_repeticoes = 1
        else:
            S.media_cheg_A = float(self.mediaChegadaA.text())
            S.dist_perfuracao_A = (float(self.mediaPerfuracaoA.text()), float(self.desvioPerfuracaoA.text()))
            S.numero_maquinas_perfuracao_A = float(self.nMaquinasPerfuracaoA.text())
            S.dist_polimento_A = (float(self.mediaPolimentoA.text()), float(self.desvioPolimentoA.text()))
            S.numero_maquinas_polimento_A = float(self.nMaquinasPolimentoA.text())

            S.media_cheg_B = float(self.mediaChegadaB.text())
            S.dist_perfuracao_B = (float(self.mediaPerfuracaoB.text()), float(self.desvioPerfuracaoB.text()))
            S.numero_maquinas_perfuracao_B = float(self.nMaquinasPerfuracaoB.text())
            S.dist_polimento_B = (float(self.mediaPolimentoB.text()), float(self.desvioPolimentoB.text()))
            S.numero_maquinas_polimento_B = float(self.nMaquinasPolimentoB.text())

            S.dist_envernizamento = (float(self.mediaEnvernizamento.text()), float(self.desvioEnvernizamento.text()))
            S.numero_maquinas_envernizamento = float(self.nMaquinasEnvernizamento.text())

            S.n_clientes = float(self.nClientes.text())
            S.tempo_simulacao = float(self.tempoSimulacao.text())
            S.n_repeticoes = float(self.nRepeticoes.text())

        S.executa()

        self.relatorio.mEsperaPerfuracaoA.setText(str(S.a_perfuracao_relat['mediaEspera']))
        self.relatorio.utilPerfuracaoA.setText(str(S.a_perfuracao_relat['utilizacao']))
        self.relatorio.mEsperaPolimentoA.setText(str(S.a_polimento_relat['mediaEspera']))
        self.relatorio.utilPolimentoA.setText(str(S.a_polimento_relat['utilizacao']))
        self.relatorio.mEsperaPerfuracaoB.setText(str(S.b_perfuracao_relat['mediaEspera']))
        self.relatorio.utilPerfuracaoB.setText(str(S.b_perfuracao_relat['utilizacao']))
        self.relatorio.mEsperaPolimentoB.setText(str(S.b_polimento_relat['mediaEspera']))
        self.relatorio.utilPolimentoB.setText(str(S.b_polimento_relat['utilizacao']))
        self.relatorio.mEsperaEnvernizamento.setText(str(S.envernizamento_relat['mediaEspera']))
        self.relatorio.utilEnvernizamento.setText(str(S.envernizamento_relat['utilizacao']))
        self.relatorio.clientesAtendidos.setText(str(S.envernizamento_queue.atendidos))
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
