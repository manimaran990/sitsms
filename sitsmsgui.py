#!/usr/bin/python

import sitsms
import sys
from PyQt4 import QtGui, QtCore

class Sitsms(QtGui.QWidget):

    def __init__(self):
        super(Sitsms, self).__init__()

        self.initUI()

    def initUI(self):

        number = QtGui.QLabel("Number ")
        message = QtGui.QLabel("Message ")

        self.numberEdit = QtGui.QLineEdit()
        self.messageEdit = QtGui.QTextEdit()

        sendbtn = QtGui.QPushButton("send")
        quitbtn = QtGui.QPushButton("Exit")

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(number,1,0)
        grid.addWidget(self.numberEdit,1,1)

        grid.addWidget(message,2,0)
        grid.addWidget(self.messageEdit,2,1,3,1)

        sendbtn.clicked.connect(self.buttonClicked)
        grid.addWidget(sendbtn,5,0)

        quitbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        quitbtn.resize(50,50)
        grid.addWidget(quitbtn,5,1)

        self.setLayout(grid)

        self.setGeometry(300,300,350,300)
        self.setWindowTitle('SitSms')
        self.show()

    def buttonClicked(self):
        num = self.numberEdit.text()
        message = self.messageEdit.toPlainText()
        sitsms.loginsite()
        sitsms.sendsms(num,message)
        QtGui.QMessageBox.information(self,'info','Message delivered to '+num,1)

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Sitsms()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
