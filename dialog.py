# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Thu Nov  1 11:23:01 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(377, 246)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.input_francs = QtGui.QLineEdit(Dialog)
        self.input_francs.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.input_francs.setObjectName("input_francs")
        self.horizontalLayout.addWidget(self.input_francs)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.input_euros = QtGui.QLineEdit(Dialog)
        self.input_euros.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.input_euros.setObjectName("input_euros")
        self.horizontalLayout_2.addWidget(self.input_euros)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_convert = QtGui.QPushButton(Dialog)
        self.button_convert.setObjectName("button_convert")
        self.horizontalLayout_3.addWidget(self.button_convert)
        self.button_quit = QtGui.QPushButton(Dialog)
        self.button_quit.setObjectName("button_quit")
        self.horizontalLayout_3.addWidget(self.button_quit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Convertisseur", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Francs", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Euros", None, QtGui.QApplication.UnicodeUTF8))
        self.button_convert.setText(QtGui.QApplication.translate("Dialog", "Convertir", None, QtGui.QApplication.UnicodeUTF8))
        self.button_quit.setText(QtGui.QApplication.translate("Dialog", "Quitter", None, QtGui.QApplication.UnicodeUTF8))

