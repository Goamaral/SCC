# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inputWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(655, 426)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.List = QtGui.QVBoxLayout()
        self.List.setObjectName(_fromUtf8("List"))
        self.listItem_3 = QtGui.QWidget(self.centralwidget)
        self.listItem_3.setMinimumSize(QtCore.QSize(0, 0))
        self.listItem_3.setMaximumSize(QtCore.QSize(10000, 100))
        self.listItem_3.setObjectName(_fromUtf8("listItem_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.listItem_3)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.nameLabel_3 = QtGui.QLabel(self.listItem_3)
        self.nameLabel_3.setMinimumSize(QtCore.QSize(125, 0))
        self.nameLabel_3.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel_3.setFont(font)
        self.nameLabel_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.nameLabel_3.setObjectName(_fromUtf8("nameLabel_3"))
        self.horizontalLayout_5.addWidget(self.nameLabel_3)
        self.nameLabel_27 = QtGui.QLabel(self.listItem_3)
        self.nameLabel_27.setMinimumSize(QtCore.QSize(100, 0))
        self.nameLabel_27.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.nameLabel_27.setFont(font)
        self.nameLabel_27.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel_27.setObjectName(_fromUtf8("nameLabel_27"))
        self.horizontalLayout_5.addWidget(self.nameLabel_27)
        self.mediaChegadaA = QtGui.QLineEdit(self.listItem_3)
        self.mediaChegadaA.setMinimumSize(QtCore.QSize(50, 25))
        self.mediaChegadaA.setMaximumSize(QtCore.QSize(50, 25))
        self.mediaChegadaA.setText(_fromUtf8(""))
        self.mediaChegadaA.setObjectName(_fromUtf8("mediaChegadaA"))
        self.horizontalLayout_5.addWidget(self.mediaChegadaA)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.List.addWidget(self.listItem_3)
        self.listItem_6 = QtGui.QWidget(self.centralwidget)
        self.listItem_6.setMinimumSize(QtCore.QSize(0, 0))
        self.listItem_6.setMaximumSize(QtCore.QSize(10000, 100))
        self.listItem_6.setObjectName(_fromUtf8("listItem_6"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.listItem_6)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.nameLabel_7 = QtGui.QLabel(self.listItem_6)
        self.nameLabel_7.setMinimumSize(QtCore.QSize(125, 0))
        self.nameLabel_7.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel_7.setFont(font)
        self.nameLabel_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.nameLabel_7.setObjectName(_fromUtf8("nameLabel_7"))
        self.horizontalLayout_7.addWidget(self.nameLabel_7)
        self.nameLabel_8 = QtGui.QLabel(self.listItem_6)
        self.nameLabel_8.setMinimumSize(QtCore.QSize(100, 0))
        self.nameLabel_8.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.nameLabel_8.setFont(font)
        self.nameLabel_8.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel_8.setObjectName(_fromUtf8("nameLabel_8"))
        self.horizontalLayout_7.addWidget(self.nameLabel_8)
        self.mediaPerfuracaoA = QtGui.QLineEdit(self.listItem_6)
        self.mediaPerfuracaoA.setMinimumSize(QtCore.QSize(50, 25))
        self.mediaPerfuracaoA.setMaximumSize(QtCore.QSize(50, 25))
        self.mediaPerfuracaoA.setText(_fromUtf8(""))
        self.mediaPerfuracaoA.setObjectName(_fromUtf8("mediaPerfuracaoA"))
        self.horizontalLayout_7.addWidget(self.mediaPerfuracaoA)
        self.nameLabel_9 = QtGui.QLabel(self.listItem_6)
        self.nameLabel_9.setMinimumSize(QtCore.QSize(100, 0))
        self.nameLabel_9.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.nameLabel_9.setFont(font)
        self.nameLabel_9.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel_9.setObjectName(_fromUtf8("nameLabel_9"))
        self.horizontalLayout_7.addWidget(self.nameLabel_9)
        self.desvioPerfuracaoA = QtGui.QLineEdit(self.listItem_6)
        self.desvioPerfuracaoA.setMinimumSize(QtCore.QSize(50, 25))
        self.desvioPerfuracaoA.setMaximumSize(QtCore.QSize(50, 25))
        self.desvioPerfuracaoA.setText(_fromUtf8(""))
        self.desvioPerfuracaoA.setObjectName(_fromUtf8("desvioPerfuracaoA"))
        self.horizontalLayout_7.addWidget(self.desvioPerfuracaoA)
        self.nameLabel_10 = QtGui.QLabel(self.listItem_6)
        self.nameLabel_10.setMinimumSize(QtCore.QSize(100, 0))
        self.nameLabel_10.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.nameLabel_10.setFont(font)
        self.nameLabel_10.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel_10.setObjectName(_fromUtf8("nameLabel_10"))
        self.horizontalLayout_7.addWidget(self.nameLabel_10)
        self.nMaquinasPerfuracaoA = QtGui.QLineEdit(self.listItem_6)
        self.nMaquinasPerfuracaoA.setMinimumSize(QtCore.QSize(50, 25))
        self.nMaquinasPerfuracaoA.setMaximumSize(QtCore.QSize(50, 25))
        self.nMaquinasPerfuracaoA.setText(_fromUtf8(""))
        self.nMaquinasPerfuracaoA.setObjectName(_fromUtf8("nMaquinasPerfuracaoA"))
        self.horizontalLayout_7.addWidget(self.nMaquinasPerfuracaoA)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.List.addWidget(self.listItem_6)
        self.listItem_7 = QtGui.QWidget(self.centralwidget)
        self.listItem_7.setMinimumSize(QtCore.QSize(0, 0))
        self.listItem_7.setMaximumSize(QtCore.QSize(10000, 100))
        self.listItem_7.setObjectName(_fromUtf8("listItem_7"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.listItem_7)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.nameLabel_11 = QtGui.QLabel(self.listItem_7)
        self.nameLabel_11.setMinimumSize(QtCore.QSize(125, 0))
        self.nameLabel_11.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel_11.setFont(font)
        self.nameLabel_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.nameLabel_11.setObjectName(_fromUtf8("nameLabel_11"))
        self.horizontalLayout_8.addWidget(self.nameLabel_11)
        self.nameLabel_12 = QtGui.QLabel(self.listItem_7)
        self.nameLabel_12.setMinimumSize(QtCore.QSize(100, 0))
        self.nameLabel_12.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.nameLabel_12.setFont(font)
        self.nameLabel_12.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel_12.setObjectName(_fromUtf8("nameLabel_12"))
        self.horizontalLayout_8.addWidget(self.nameLabel_12)
        self.mediaPolimentoA = QtGui.QLineEdit(self.listItem_7)
        self.mediaPolimentoA.setMinimumSize(QtCore.QSize(50, 25))
        self.mediaPolimentoA.setMaximumSize(QtCore.QSize(50, 25))
        self.mediaPolimentoA.setText(_fromUtf8(""))
        self.mediaPolimentoA.setObjectName(_fromUtf8("mediaPolimentoA"))
        self.horizontalLayout_8.addWidget(self.mediaPolimentoA)
        self.nameLabel_13 = QtGui.QLabel(self.listItem_7)
        self.nameLabel_13.setMinimumSize(QtCore.QSize(100, 0))
        self.nameLabel_13.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.nameLabel_13.setFont(font)
        self.nameLabel_13.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel_13.setObjectName(_fromUtf8("nameLabel_13"))
        self.horizontalLayout_8.addWidget(self.nameLabel_13)
        self.desvioPolimentoA = QtGui.QLineEdit(self.listItem_7)
        self.desvioPolimentoA.setMinimumSize(QtCore.QSize(50, 25))
        self.desvioPolimentoA.setMaximumSize(QtCore.QSize(50, 25))
        self.desvioPolimentoA.setText(_fromUtf8(""))
        self.desvioPolimentoA.setObjectName(_fromUtf8("desvioPolimentoA"))
        self.horizontalLayout_8.addWidget(self.desvioPolimentoA)
        self.nameLabel_14 = QtGui.QLabel(self.listItem_7)
        self.nameLabel_14.setMinimumSize(QtCore.QSize(100, 0))
        self.nameLabel_14.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.nameLabel_14.setFont(font)
        self.nameLabel_14.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel_14.setObjectName(_fromUtf8("nameLabel_14"))
        self.horizontalLayout_8.addWidget(self.nameLabel_14)
        self.nMaquinasPolimentoA = QtGui.QLineEdit(self.listItem_7)
        self.nMaquinasPolimentoA.setMinimumSize(QtCore.QSize(50, 25))
        self.nMaquinasPolimentoA.setMaximumSize(QtCore.QSize(50, 25))
        self.nMaquinasPolimentoA.setText(_fromUtf8(""))
        self.nMaquinasPolimentoA.setObjectName(_fromUtf8("nMaquinasPolimentoA"))
        self.horizontalLayout_8.addWidget(self.nMaquinasPolimentoA)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.List.addWidget(self.listItem_7)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setMinimumSize(QtCore.QSize(5, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.List.addWidget(self.line_2)
        self.listItem_4 = QtGui.QWidget(self.centralwidget)
        self.listItem_4.setMinimumSize(QtCore.QSize(0, 0))
        self.listItem_4.setMaximumSize(QtCore.QSize(10000, 100))
        self.listItem_4.setObjectName(_fromUtf8("listItem_4"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.listItem_4)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.nameLabel_4 = QtGui.QLabel(self.listItem_4)
        self.nameLabel_4.setMinimumSize(QtCore.QSize(125, 0))
        self.nameLabel_4.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel_4.setFont(font)
        self.nameLabel_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.nameLabel_4.setObjectName(_fromUtf8("nameLabel_4"))
        self.horizontalLayout_6.addWidget(self.nameLabel_4)
        self.nameLabel_31 = QtGui.QLabel(self.listItem_4)
        self.nameLabel_31.setMinimumSize(QtCore.QSize(100, 0))
        self.nameLabel_31.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.nameLabel_31.setFont(font)
        self.nameLabel_31.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel_31.setObjectName(_fromUtf8("nameLabel_31"))
        self.horizontalLayout_6.addWidget(self.nameLabel_31)
        self.mediaChegadaB = QtGui.QLineEdit(self.listItem_4)
        self.mediaChegadaB.setMinimumSize(QtCore.QSize(50, 25))
        self.mediaChegadaB.setMaximumSize(QtCore.QSize(50, 25))
        self.mediaChegadaB.setText(_fromUtf8(""))
        self.mediaChegadaB.setObjectName(_fromUtf8("mediaChegadaB"))
        self.horizontalLayout_6.addWidget(self.mediaChegadaB)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.List.addWidget(self.listItem_4)
        self.listItem_9 = QtGui.QWidget(self.centralwidget)
        self.listItem_9.setMinimumSize(QtCore.QSize(0, 0))
        self.listItem_9.setMaximumSize(QtCore.QSize(10000, 100))
        self.listItem_9.setObjectName(_fromUtf8("listItem_9"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.listItem_9)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.nameLabel_36 = QtGui.QLabel(self.listItem_9)
        self.nameLabel_36.setMinimumSize(QtCore.QSize(125, 0))
        self.nameLabel_36.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel_36.setFont(font)
        self.nameLabel_36.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.nameLabel_36.setObjectName(_fromUtf8("nameLabel_36"))
        self.horizontalLayout_13.addWidget(self.nameLabel_36)
        self.nameLabel_37 = QtGui.QLabel(self.listItem_9)
        self.nameLabel_37.setMinimumSize(QtCore.QSize(100, 0))
        self.nameLabel_37.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.nameLabel_37.setFont(font)
        self.nameLabel_37.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel_37.setObjectName(_fromUtf8("nameLabel_37"))
        self.horizontalLayout_13.addWidget(self.nameLabel_37)
        self.mediaPerfuracaoB = QtGui.QLineEdit(self.listItem_9)
        self.mediaPerfuracaoB.setMinimumSize(QtCore.QSize(50, 25))
        self.mediaPerfuracaoB.setMaximumSize(QtCore.QSize(50, 25))
        self.mediaPerfuracaoB.setText(_fromUtf8(""))
        self.mediaPerfuracaoB.setObjectName(_fromUtf8("mediaPerfuracaoB"))
        self.horizontalLayout_13.addWidget(self.mediaPerfuracaoB)
        self.nameLabel_38 = QtGui.QLabel(self.listItem_9)
        self.nameLabel_38.setMinimumSize(QtCore.QSize(100, 0))
        self.nameLabel_38.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.nameLabel_38.setFont(font)
        self.nameLabel_38.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel_38.setObjectName(_fromUtf8("nameLabel_38"))
        self.horizontalLayout_13.addWidget(self.nameLabel_38)
        self.desvioPerfuracaoB = QtGui.QLineEdit(self.listItem_9)
        self.desvioPerfuracaoB.setMinimumSize(QtCore.QSize(50, 25))
        self.desvioPerfuracaoB.setMaximumSize(QtCore.QSize(50, 25))
        self.desvioPerfuracaoB.setText(_fromUtf8(""))
        self.desvioPerfuracaoB.setObjectName(_fromUtf8("desvioPerfuracaoB"))
        self.horizontalLayout_13.addWidget(self.desvioPerfuracaoB)
        self.nameLabel_39 = QtGui.QLabel(self.listItem_9)
        self.nameLabel_39.setMinimumSize(QtCore.QSize(100, 0))
        self.nameLabel_39.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.nameLabel_39.setFont(font)
        self.nameLabel_39.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel_39.setObjectName(_fromUtf8("nameLabel_39"))
        self.horizontalLayout_13.addWidget(self.nameLabel_39)
        self.nMaquinasPerfuracaoB = QtGui.QLineEdit(self.listItem_9)
        self.nMaquinasPerfuracaoB.setMinimumSize(QtCore.QSize(50, 25))
        self.nMaquinasPerfuracaoB.setMaximumSize(QtCore.QSize(50, 25))
        self.nMaquinasPerfuracaoB.setText(_fromUtf8(""))
        self.nMaquinasPerfuracaoB.setObjectName(_fromUtf8("nMaquinasPerfuracaoB"))
        self.horizontalLayout_13.addWidget(self.nMaquinasPerfuracaoB)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem4)
        self.List.addWidget(self.listItem_9)
        self.listItem_8 = QtGui.QWidget(self.centralwidget)
        self.listItem_8.setMinimumSize(QtCore.QSize(0, 0))
        self.listItem_8.setMaximumSize(QtCore.QSize(10000, 100))
        self.listItem_8.setObjectName(_fromUtf8("listItem_8"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.listItem_8)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.nameLabel_19 = QtGui.QLabel(self.listItem_8)
        self.nameLabel_19.setMinimumSize(QtCore.QSize(125, 0))
        self.nameLabel_19.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel_19.setFont(font)
        self.nameLabel_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.nameLabel_19.setObjectName(_fromUtf8("nameLabel_19"))
        self.horizontalLayout_10.addWidget(self.nameLabel_19)
        self.nameLabel_20 = QtGui.QLabel(self.listItem_8)
        self.nameLabel_20.setMinimumSize(QtCore.QSize(100, 0))
        self.nameLabel_20.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.nameLabel_20.setFont(font)
        self.nameLabel_20.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel_20.setObjectName(_fromUtf8("nameLabel_20"))
        self.horizontalLayout_10.addWidget(self.nameLabel_20)
        self.mediaPolimentoB = QtGui.QLineEdit(self.listItem_8)
        self.mediaPolimentoB.setMinimumSize(QtCore.QSize(50, 25))
        self.mediaPolimentoB.setMaximumSize(QtCore.QSize(50, 25))
        self.mediaPolimentoB.setText(_fromUtf8(""))
        self.mediaPolimentoB.setObjectName(_fromUtf8("mediaPolimentoB"))
        self.horizontalLayout_10.addWidget(self.mediaPolimentoB)
        self.nameLabel_21 = QtGui.QLabel(self.listItem_8)
        self.nameLabel_21.setMinimumSize(QtCore.QSize(100, 0))
        self.nameLabel_21.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.nameLabel_21.setFont(font)
        self.nameLabel_21.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel_21.setObjectName(_fromUtf8("nameLabel_21"))
        self.horizontalLayout_10.addWidget(self.nameLabel_21)
        self.desvioPolimentoB = QtGui.QLineEdit(self.listItem_8)
        self.desvioPolimentoB.setMinimumSize(QtCore.QSize(50, 25))
        self.desvioPolimentoB.setMaximumSize(QtCore.QSize(50, 25))
        self.desvioPolimentoB.setText(_fromUtf8(""))
        self.desvioPolimentoB.setObjectName(_fromUtf8("desvioPolimentoB"))
        self.horizontalLayout_10.addWidget(self.desvioPolimentoB)
        self.nameLabel_22 = QtGui.QLabel(self.listItem_8)
        self.nameLabel_22.setMinimumSize(QtCore.QSize(100, 0))
        self.nameLabel_22.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.nameLabel_22.setFont(font)
        self.nameLabel_22.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel_22.setObjectName(_fromUtf8("nameLabel_22"))
        self.horizontalLayout_10.addWidget(self.nameLabel_22)
        self.nMaquinasPolimentoB = QtGui.QLineEdit(self.listItem_8)
        self.nMaquinasPolimentoB.setMinimumSize(QtCore.QSize(50, 25))
        self.nMaquinasPolimentoB.setMaximumSize(QtCore.QSize(50, 25))
        self.nMaquinasPolimentoB.setText(_fromUtf8(""))
        self.nMaquinasPolimentoB.setObjectName(_fromUtf8("nMaquinasPolimentoB"))
        self.horizontalLayout_10.addWidget(self.nMaquinasPolimentoB)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.List.addWidget(self.listItem_8)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setMinimumSize(QtCore.QSize(0, 5))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.List.addWidget(self.line)
        self.listItem_11 = QtGui.QWidget(self.centralwidget)
        self.listItem_11.setMinimumSize(QtCore.QSize(0, 0))
        self.listItem_11.setMaximumSize(QtCore.QSize(10000, 100))
        self.listItem_11.setObjectName(_fromUtf8("listItem_11"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.listItem_11)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.nameLabel_23 = QtGui.QLabel(self.listItem_11)
        self.nameLabel_23.setMinimumSize(QtCore.QSize(125, 0))
        self.nameLabel_23.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel_23.setFont(font)
        self.nameLabel_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.nameLabel_23.setObjectName(_fromUtf8("nameLabel_23"))
        self.horizontalLayout_12.addWidget(self.nameLabel_23)
        self.nameLabel_24 = QtGui.QLabel(self.listItem_11)
        self.nameLabel_24.setMinimumSize(QtCore.QSize(100, 0))
        self.nameLabel_24.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.nameLabel_24.setFont(font)
        self.nameLabel_24.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel_24.setObjectName(_fromUtf8("nameLabel_24"))
        self.horizontalLayout_12.addWidget(self.nameLabel_24)
        self.mediaEnvernizamento = QtGui.QLineEdit(self.listItem_11)
        self.mediaEnvernizamento.setMinimumSize(QtCore.QSize(50, 25))
        self.mediaEnvernizamento.setMaximumSize(QtCore.QSize(50, 25))
        self.mediaEnvernizamento.setText(_fromUtf8(""))
        self.mediaEnvernizamento.setObjectName(_fromUtf8("mediaEnvernizamento"))
        self.horizontalLayout_12.addWidget(self.mediaEnvernizamento)
        self.nameLabel_25 = QtGui.QLabel(self.listItem_11)
        self.nameLabel_25.setMinimumSize(QtCore.QSize(100, 0))
        self.nameLabel_25.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.nameLabel_25.setFont(font)
        self.nameLabel_25.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel_25.setObjectName(_fromUtf8("nameLabel_25"))
        self.horizontalLayout_12.addWidget(self.nameLabel_25)
        self.desvioEnvernizamento = QtGui.QLineEdit(self.listItem_11)
        self.desvioEnvernizamento.setMinimumSize(QtCore.QSize(50, 25))
        self.desvioEnvernizamento.setMaximumSize(QtCore.QSize(50, 25))
        self.desvioEnvernizamento.setText(_fromUtf8(""))
        self.desvioEnvernizamento.setObjectName(_fromUtf8("desvioEnvernizamento"))
        self.horizontalLayout_12.addWidget(self.desvioEnvernizamento)
        self.nameLabel_26 = QtGui.QLabel(self.listItem_11)
        self.nameLabel_26.setMinimumSize(QtCore.QSize(100, 0))
        self.nameLabel_26.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.nameLabel_26.setFont(font)
        self.nameLabel_26.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel_26.setObjectName(_fromUtf8("nameLabel_26"))
        self.horizontalLayout_12.addWidget(self.nameLabel_26)
        self.nMaquinasEnvernizamento = QtGui.QLineEdit(self.listItem_11)
        self.nMaquinasEnvernizamento.setMinimumSize(QtCore.QSize(50, 25))
        self.nMaquinasEnvernizamento.setMaximumSize(QtCore.QSize(50, 25))
        self.nMaquinasEnvernizamento.setText(_fromUtf8(""))
        self.nMaquinasEnvernizamento.setObjectName(_fromUtf8("nMaquinasEnvernizamento"))
        self.horizontalLayout_12.addWidget(self.nMaquinasEnvernizamento)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem6)
        self.List.addWidget(self.listItem_11)
        self.verticalLayout_4.addLayout(self.List)
        self.footer = QtGui.QWidget(self.centralwidget)
        self.footer.setMaximumSize(QtCore.QSize(100000, 50))
        self.footer.setObjectName(_fromUtf8("footer"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.footer)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.nameLabel_30 = QtGui.QLabel(self.footer)
        self.nameLabel_30.setMinimumSize(QtCore.QSize(70, 0))
        self.nameLabel_30.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel_30.setFont(font)
        self.nameLabel_30.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.nameLabel_30.setObjectName(_fromUtf8("nameLabel_30"))
        self.horizontalLayout.addWidget(self.nameLabel_30)
        self.nClientes = QtGui.QLineEdit(self.footer)
        self.nClientes.setMinimumSize(QtCore.QSize(50, 25))
        self.nClientes.setMaximumSize(QtCore.QSize(50, 25))
        self.nClientes.setText(_fromUtf8(""))
        self.nClientes.setObjectName(_fromUtf8("nClientes"))
        self.horizontalLayout.addWidget(self.nClientes)
        self.nameLabel_29 = QtGui.QLabel(self.footer)
        self.nameLabel_29.setMinimumSize(QtCore.QSize(100, 0))
        self.nameLabel_29.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel_29.setFont(font)
        self.nameLabel_29.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel_29.setObjectName(_fromUtf8("nameLabel_29"))
        self.horizontalLayout.addWidget(self.nameLabel_29)
        self.nRepeticoes = QtGui.QLineEdit(self.footer)
        self.nRepeticoes.setMinimumSize(QtCore.QSize(50, 25))
        self.nRepeticoes.setMaximumSize(QtCore.QSize(50, 25))
        self.nRepeticoes.setText(_fromUtf8(""))
        self.nRepeticoes.setObjectName(_fromUtf8("nRepeticoes"))
        self.horizontalLayout.addWidget(self.nRepeticoes)
        self.nameLabel_28 = QtGui.QLabel(self.footer)
        self.nameLabel_28.setMinimumSize(QtCore.QSize(125, 0))
        self.nameLabel_28.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel_28.setFont(font)
        self.nameLabel_28.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel_28.setObjectName(_fromUtf8("nameLabel_28"))
        self.horizontalLayout.addWidget(self.nameLabel_28)
        self.tempoSimulacao = QtGui.QLineEdit(self.footer)
        self.tempoSimulacao.setMinimumSize(QtCore.QSize(75, 25))
        self.tempoSimulacao.setMaximumSize(QtCore.QSize(75, 25))
        self.tempoSimulacao.setText(_fromUtf8(""))
        self.tempoSimulacao.setObjectName(_fromUtf8("tempoSimulacao"))
        self.horizontalLayout.addWidget(self.tempoSimulacao)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.botaoSimular = QtGui.QPushButton(self.footer)
        self.botaoSimular.setMinimumSize(QtCore.QSize(100, 25))
        self.botaoSimular.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.botaoSimular.setFont(font)
        self.botaoSimular.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.botaoSimular.setAutoFillBackground(False)
        self.botaoSimular.setStyleSheet(_fromUtf8(""))
        self.botaoSimular.setFlat(False)
        self.botaoSimular.setObjectName(_fromUtf8("botaoSimular"))
        self.horizontalLayout.addWidget(self.botaoSimular)
        self.verticalLayout_4.addWidget(self.footer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Descriçao da simulaçao", None))
        self.nameLabel_3.setText(_translate("MainWindow", "Peças grandes (A)", None))
        self.nameLabel_27.setText(_translate("MainWindow", "Media chegada", None))
        self.nameLabel_7.setText(_translate("MainWindow", "Perfuraçao", None))
        self.nameLabel_8.setText(_translate("MainWindow", "Media", None))
        self.nameLabel_9.setText(_translate("MainWindow", "Desvio padrao", None))
        self.nameLabel_10.setText(_translate("MainWindow", "Nº maquinas", None))
        self.nameLabel_11.setText(_translate("MainWindow", "Polimento", None))
        self.nameLabel_12.setText(_translate("MainWindow", "Media", None))
        self.nameLabel_13.setText(_translate("MainWindow", "Desvio padrao", None))
        self.nameLabel_14.setText(_translate("MainWindow", "Nº maquinas", None))
        self.nameLabel_4.setText(_translate("MainWindow", "Peças grandes (B)", None))
        self.nameLabel_31.setText(_translate("MainWindow", "Media chegada", None))
        self.nameLabel_36.setText(_translate("MainWindow", "Perfuraçao", None))
        self.nameLabel_37.setText(_translate("MainWindow", "Media", None))
        self.nameLabel_38.setText(_translate("MainWindow", "Desvio padrao", None))
        self.nameLabel_39.setText(_translate("MainWindow", "Nº maquinas", None))
        self.nameLabel_19.setText(_translate("MainWindow", "Polimento", None))
        self.nameLabel_20.setText(_translate("MainWindow", "Media", None))
        self.nameLabel_21.setText(_translate("MainWindow", "Desvio padrao", None))
        self.nameLabel_22.setText(_translate("MainWindow", "Nº maquinas", None))
        self.nameLabel_23.setText(_translate("MainWindow", "Envernizamento", None))
        self.nameLabel_24.setText(_translate("MainWindow", "Media", None))
        self.nameLabel_25.setText(_translate("MainWindow", "Desvio padrao", None))
        self.nameLabel_26.setText(_translate("MainWindow", "Nº maquinas", None))
        self.nameLabel_30.setText(_translate("MainWindow", "Nº clientes", None))
        self.nameLabel_29.setText(_translate("MainWindow", "Nº Repeticoes", None))
        self.nameLabel_28.setText(_translate("MainWindow", "Tempo simulacao", None))
        self.botaoSimular.setText(_translate("MainWindow", "Simular", None))
