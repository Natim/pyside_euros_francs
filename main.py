#!/usr/bin/python

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from dialog import Ui_Dialog
 
class MainApplication(QDialog):
    """SetUp the dialog generated with pyside-uic."""
    def __init__(self, parent=None):
        super(MainApplication, self).__init__(parent)
        self.createWidgets()

    def createWidgets(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
 
# Create a Qt application
app = QApplication(sys.argv)
myapp = MainApplication()
myapp.show()
# Enter Qt application main loop
sys.exit(app.exec_())

