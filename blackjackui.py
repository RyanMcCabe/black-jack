
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Wed Jun 25 16:17:14 2014
#      by: PyQt4 UI code generator 4.11
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

class Ui_Blackjack(object):
    def setupUi(self, Blackjack):
        Blackjack.setObjectName(_fromUtf8("Blackjack"))
        Blackjack.resize(934, 673)
        Blackjack.setAutoFillBackground(True)
        Blackjack.setStyleSheet(_fromUtf8("color rgb(85, 255, 0)"))
        self.centralwidget = QtGui.QWidget(Blackjack)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(750, 30, 171, 581))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.labMoney = QtGui.QLabel(self.widget)
        self.labMoney.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labMoney.setAlignment(QtCore.Qt.AlignCenter)
        self.labMoney.setObjectName(_fromUtf8("labMoney"))
        self.verticalLayout_3.addWidget(self.labMoney)
        self.lineBet = QtGui.QLineEdit(self.widget)
        self.lineBet.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineBet.setObjectName(_fromUtf8("lineBet"))
        self.verticalLayout_3.addWidget(self.lineBet)
        self.labWarning = QtGui.QLabel(self.widget)
        self.labWarning.setStyleSheet(_fromUtf8("font: 12pt \"MS Shell Dlg 2\";"))
        self.labWarning.setText(_fromUtf8(""))
        self.labWarning.setAlignment(QtCore.Qt.AlignCenter)
        self.labWarning.setWordWrap(True)
        self.labWarning.setObjectName(_fromUtf8("labWarning"))
        self.verticalLayout_3.addWidget(self.labWarning)
        self.btnBet = QtGui.QPushButton(self.widget)
        self.btnBet.setObjectName(_fromUtf8("btnBet"))
        self.verticalLayout_3.addWidget(self.btnBet)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnDouble = QtGui.QPushButton(self.widget)
        self.btnDouble.setObjectName(_fromUtf8("btnDouble"))
        self.verticalLayout.addWidget(self.btnDouble)
        self.btnHit = QtGui.QPushButton(self.widget)
        self.btnHit.setObjectName(_fromUtf8("btnHit"))
        self.verticalLayout.addWidget(self.btnHit)
        self.btnStay = QtGui.QPushButton(self.widget)
        self.btnStay.setObjectName(_fromUtf8("btnStay"))
        self.verticalLayout.addWidget(self.btnStay)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(10, 30, 731, 581))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.cardWidget_2 = QtGui.QWidget(self.widget_2)
        self.cardWidget_2.setGeometry(QtCore.QRect(0, 390, 721, 129))
        self.cardWidget_2.setAutoFillBackground(True)
        self.cardWidget_2.setObjectName(_fromUtf8("cardWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.cardWidget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pCard_7 = QtGui.QLabel(self.cardWidget_2)
        self.pCard_7.setEnabled(True)
        self.pCard_7.setText(_fromUtf8(""))
        self.pCard_7.setPixmap(QtGui.QPixmap(_fromUtf8("../Dropbox/final/cards/back.png")))
        self.pCard_7.setScaledContents(False)
        self.pCard_7.setAlignment(QtCore.Qt.AlignCenter)
        self.pCard_7.setObjectName(_fromUtf8("pCard_7"))
        self.horizontalLayout_2.addWidget(self.pCard_7)
        self.pCard = QtGui.QLabel(self.cardWidget_2)
        self.pCard.setEnabled(True)
        self.pCard.setText(_fromUtf8(""))
        self.pCard.setPixmap(QtGui.QPixmap(_fromUtf8("../Dropbox/final/cards/back.png")))
        self.pCard.setScaledContents(False)
        self.pCard.setAlignment(QtCore.Qt.AlignCenter)
        self.pCard.setObjectName(_fromUtf8("pCard"))
        self.horizontalLayout_2.addWidget(self.pCard)
        self.pCard_2 = QtGui.QLabel(self.cardWidget_2)
        self.pCard_2.setEnabled(True)
        self.pCard_2.setText(_fromUtf8(""))
        self.pCard_2.setPixmap(QtGui.QPixmap(_fromUtf8("../Dropbox/final/cards/back.png")))
        self.pCard_2.setScaledContents(False)
        self.pCard_2.setAlignment(QtCore.Qt.AlignCenter)
        self.pCard_2.setObjectName(_fromUtf8("pCard_2"))
        self.horizontalLayout_2.addWidget(self.pCard_2)
        self.pCard_3 = QtGui.QLabel(self.cardWidget_2)
        self.pCard_3.setEnabled(True)
        self.pCard_3.setText(_fromUtf8(""))
        self.pCard_3.setPixmap(QtGui.QPixmap(_fromUtf8("../Dropbox/final/cards/back.png")))
        self.pCard_3.setScaledContents(False)
        self.pCard_3.setAlignment(QtCore.Qt.AlignCenter)
        self.pCard_3.setObjectName(_fromUtf8("pCard_3"))
        self.horizontalLayout_2.addWidget(self.pCard_3)
        self.pCard_4 = QtGui.QLabel(self.cardWidget_2)
        self.pCard_4.setEnabled(True)
        self.pCard_4.setText(_fromUtf8(""))
        self.pCard_4.setPixmap(QtGui.QPixmap(_fromUtf8("../Dropbox/final/cards/back.png")))
        self.pCard_4.setScaledContents(False)
        self.pCard_4.setAlignment(QtCore.Qt.AlignCenter)
        self.pCard_4.setObjectName(_fromUtf8("pCard_4"))
        self.horizontalLayout_2.addWidget(self.pCard_4)
        self.pCard_5 = QtGui.QLabel(self.cardWidget_2)
        self.pCard_5.setEnabled(True)
        self.pCard_5.setText(_fromUtf8(""))
        self.pCard_5.setPixmap(QtGui.QPixmap(_fromUtf8("../Dropbox/final/cards/back.png")))
        self.pCard_5.setScaledContents(False)
        self.pCard_5.setAlignment(QtCore.Qt.AlignCenter)
        self.pCard_5.setObjectName(_fromUtf8("pCard_5"))
        self.horizontalLayout_2.addWidget(self.pCard_5)
        self.pCard_6 = QtGui.QLabel(self.cardWidget_2)
        self.pCard_6.setEnabled(True)
        self.pCard_6.setText(_fromUtf8(""))
        self.pCard_6.setPixmap(QtGui.QPixmap(_fromUtf8("../Dropbox/final/cards/back.png")))
        self.pCard_6.setScaledContents(False)
        self.pCard_6.setAlignment(QtCore.Qt.AlignCenter)
        self.pCard_6.setObjectName(_fromUtf8("pCard_6"))
        self.horizontalLayout_2.addWidget(self.pCard_6)
        self.pCard_8 = QtGui.QLabel(self.cardWidget_2)
        self.pCard_8.setEnabled(True)
        self.pCard_8.setText(_fromUtf8(""))
        self.pCard_8.setPixmap(QtGui.QPixmap(_fromUtf8("../Dropbox/final/cards/back.png")))
        self.pCard_8.setScaledContents(False)
        self.pCard_8.setAlignment(QtCore.Qt.AlignCenter)
        self.pCard_8.setObjectName(_fromUtf8("pCard_8"))
        self.horizontalLayout_2.addWidget(self.pCard_8)
        self.pCard_9 = QtGui.QLabel(self.cardWidget_2)
        self.pCard_9.setEnabled(True)
        self.pCard_9.setText(_fromUtf8(""))
        self.pCard_9.setPixmap(QtGui.QPixmap(_fromUtf8("../Dropbox/final/cards/back.png")))
        self.pCard_9.setScaledContents(False)
        self.pCard_9.setAlignment(QtCore.Qt.AlignCenter)
        self.pCard_9.setObjectName(_fromUtf8("pCard_9"))
        self.horizontalLayout_2.addWidget(self.pCard_9)
        self.pCard_10 = QtGui.QLabel(self.cardWidget_2)
        self.pCard_10.setEnabled(True)
        self.pCard_10.setText(_fromUtf8(""))
        self.pCard_10.setPixmap(QtGui.QPixmap(_fromUtf8("../Dropbox/final/cards/back.png")))
        self.pCard_10.setScaledContents(False)
        self.pCard_10.setAlignment(QtCore.Qt.AlignCenter)
        self.pCard_10.setObjectName(_fromUtf8("pCard_10"))
        self.horizontalLayout_2.addWidget(self.pCard_10)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.cardWidget = QtGui.QWidget(self.widget_2)
        self.cardWidget.setGeometry(QtCore.QRect(0, 110, 731, 121))
        self.cardWidget.setAutoFillBackground(True)
        self.cardWidget.setObjectName(_fromUtf8("cardWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.cardWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.dCard = QtGui.QLabel(self.cardWidget)
        self.dCard.setEnabled(True)
        self.dCard.setText(_fromUtf8(""))
        self.dCard.setPixmap(QtGui.QPixmap(_fromUtf8("../Dropbox/final/cards/back.png")))
        self.dCard.setScaledContents(False)
        self.dCard.setAlignment(QtCore.Qt.AlignCenter)
        self.dCard.setObjectName(_fromUtf8("dCard"))
        self.horizontalLayout.addWidget(self.dCard)
        self.dCard_2 = QtGui.QLabel(self.cardWidget)
        self.dCard_2.setEnabled(True)
        self.dCard_2.setText(_fromUtf8(""))
        self.dCard_2.setPixmap(QtGui.QPixmap(_fromUtf8("../Dropbox/final/cards/back.png")))
        self.dCard_2.setScaledContents(False)
        self.dCard_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dCard_2.setObjectName(_fromUtf8("dCard_2"))
        self.horizontalLayout.addWidget(self.dCard_2)
        self.dCard_3 = QtGui.QLabel(self.cardWidget)
        self.dCard_3.setEnabled(True)
        self.dCard_3.setText(_fromUtf8(""))
        self.dCard_3.setPixmap(QtGui.QPixmap(_fromUtf8("../Dropbox/final/cards/back.png")))
        self.dCard_3.setScaledContents(False)
        self.dCard_3.setAlignment(QtCore.Qt.AlignCenter)
        self.dCard_3.setObjectName(_fromUtf8("dCard_3"))
        self.horizontalLayout.addWidget(self.dCard_3)
        self.dCard_4 = QtGui.QLabel(self.cardWidget)
        self.dCard_4.setEnabled(True)
        self.dCard_4.setText(_fromUtf8(""))
        self.dCard_4.setPixmap(QtGui.QPixmap(_fromUtf8("../Dropbox/final/cards/back.png")))
        self.dCard_4.setScaledContents(False)
        self.dCard_4.setAlignment(QtCore.Qt.AlignCenter)
        self.dCard_4.setObjectName(_fromUtf8("dCard_4"))
        self.horizontalLayout.addWidget(self.dCard_4)
        self.dCard_5 = QtGui.QLabel(self.cardWidget)
        self.dCard_5.setEnabled(True)
        self.dCard_5.setText(_fromUtf8(""))
        self.dCard_5.setPixmap(QtGui.QPixmap(_fromUtf8("../Dropbox/final/cards/back.png")))
        self.dCard_5.setScaledContents(False)
        self.dCard_5.setAlignment(QtCore.Qt.AlignCenter)
        self.dCard_5.setObjectName(_fromUtf8("dCard_5"))
        self.horizontalLayout.addWidget(self.dCard_5)
        self.dCard_6 = QtGui.QLabel(self.cardWidget)
        self.dCard_6.setEnabled(True)
        self.dCard_6.setText(_fromUtf8(""))
        self.dCard_6.setPixmap(QtGui.QPixmap(_fromUtf8("../Dropbox/final/cards/back.png")))
        self.dCard_6.setScaledContents(False)
        self.dCard_6.setAlignment(QtCore.Qt.AlignCenter)
        self.dCard_6.setObjectName(_fromUtf8("dCard_6"))
        self.horizontalLayout.addWidget(self.dCard_6)
        self.dCard_7 = QtGui.QLabel(self.cardWidget)
        self.dCard_7.setEnabled(True)
        self.dCard_7.setText(_fromUtf8(""))
        self.dCard_7.setPixmap(QtGui.QPixmap(_fromUtf8("../Dropbox/final/cards/back.png")))
        self.dCard_7.setScaledContents(False)
        self.dCard_7.setAlignment(QtCore.Qt.AlignCenter)
        self.dCard_7.setObjectName(_fromUtf8("dCard_7"))
        self.horizontalLayout.addWidget(self.dCard_7)
        self.dCard_8 = QtGui.QLabel(self.cardWidget)
        self.dCard_8.setEnabled(True)
        self.dCard_8.setText(_fromUtf8(""))
        self.dCard_8.setPixmap(QtGui.QPixmap(_fromUtf8("../Dropbox/final/cards/back.png")))
        self.dCard_8.setScaledContents(False)
        self.dCard_8.setAlignment(QtCore.Qt.AlignCenter)
        self.dCard_8.setObjectName(_fromUtf8("dCard_8"))
        self.horizontalLayout.addWidget(self.dCard_8)
        self.dCard_9 = QtGui.QLabel(self.cardWidget)
        self.dCard_9.setEnabled(True)
        self.dCard_9.setText(_fromUtf8(""))
        self.dCard_9.setPixmap(QtGui.QPixmap(_fromUtf8("../Dropbox/final/cards/back.png")))
        self.dCard_9.setScaledContents(False)
        self.dCard_9.setAlignment(QtCore.Qt.AlignCenter)
        self.dCard_9.setObjectName(_fromUtf8("dCard_9"))
        self.horizontalLayout.addWidget(self.dCard_9)
        self.dCard_10 = QtGui.QLabel(self.cardWidget)
        self.dCard_10.setEnabled(True)
        self.dCard_10.setText(_fromUtf8(""))
        self.dCard_10.setPixmap(QtGui.QPixmap(_fromUtf8("../Dropbox/final/cards/back.png")))
        self.dCard_10.setScaledContents(False)
        self.dCard_10.setAlignment(QtCore.Qt.AlignCenter)
        self.dCard_10.setObjectName(_fromUtf8("dCard_10"))
        self.horizontalLayout.addWidget(self.dCard_10)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.labDealer = QtGui.QLabel(self.widget_2)
        self.labDealer.setGeometry(QtCore.QRect(290, 230, 151, 20))
        self.labDealer.setText(_fromUtf8(""))
        self.labDealer.setAlignment(QtCore.Qt.AlignCenter)
        self.labDealer.setObjectName(_fromUtf8("labDealer"))
        self.labPlayer = QtGui.QLabel(self.widget_2)
        self.labPlayer.setGeometry(QtCore.QRect(290, 520, 141, 20))
        self.labPlayer.setText(_fromUtf8(""))
        self.labPlayer.setAlignment(QtCore.Qt.AlignCenter)
        self.labPlayer.setObjectName(_fromUtf8("labPlayer"))
        Blackjack.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Blackjack)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 934, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Blackjack.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Blackjack)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Blackjack.setStatusBar(self.statusbar)

        self.retranslateUi(Blackjack)
        QtCore.QMetaObject.connectSlotsByName(Blackjack)

    def retranslateUi(self, Blackjack):
        Blackjack.setWindowTitle(_translate("Blackjack", "MainWindow", None))
        self.label_3.setText(_translate("Blackjack", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Money:</span></p></body></html>", None))
        self.labMoney.setText(_translate("Blackjack", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#4b9600;\">500</span></p></body></html>", None))
        self.lineBet.setPlaceholderText(_translate("Blackjack", "Enter Bet", None))
        self.btnBet.setText(_translate("Blackjack", "Enter Bet", None))
        self.btnDouble.setText(_translate("Blackjack", "Double", None))
        self.btnHit.setText(_translate("Blackjack", "Hit", None))
        self.btnStay.setText(_translate("Blackjack", "Stay", None))
