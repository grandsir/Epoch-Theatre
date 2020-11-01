# Created by GrandSir in 26.07.2020
# This game developed by GrandSir

from PyQt5 import QtCore
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLineEdit, QHBoxLayout, QTabWidget,QWidget, QPushButton, QDesktopWidget,
QCheckBox)
from style import stylesheet
import sys


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0, 1366, 768)
        self.center() # to center window at start
        self.Lines()
        self.checkboxes()
        self.states()
        self.setStyleSheet(stylesheet)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def checkboxes(self):
        self.MessageBox = QCheckBox(self)
        self.MessageBox.setGeometry(50, 80, 400, 150)
        self.MessageBox.setText("Mesaj kutusu")

        self.Choice = QCheckBox(self)
        self.Choice.setGeometry(350, 80, 400, 150)
        self.Choice.setText("Seçim")

        self.CriticalChoice = QCheckBox(self)
        self.CriticalChoice.setGeometry(650, 80, 400, 150)
        self.CriticalChoice.setText("Kritik Seçim")

    def states(self):  
        self.MessageBox.stateChanged.connect(self.uncheck)
        self.Choice.stateChanged.connect(self.uncheck)
        self.CriticalChoice.stateChanged.connect(self.uncheck)


    def uncheck(self, state):
        #uncheck others when a checkbox checked
        if state == QtCore.Qt.Checked:
            if self.sender() == self.MessageBox:
                self.Choice.setChecked(False)
                self.CriticalChoice.setChecked(False)

            elif self.sender() == self.Choice:
                self.MessageBox.setChecked(False)
                self.CriticalChoice.setChecked(False)

            elif self.sender() == self.CriticalChoice:
                self.MessageBox.setChecked(False)
                self.Choice.setChecked(False)



    def Lines(self):
        self.line = QLineEdit(self)
        self.line.setGeometry(200, 200, 200, 50)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())
