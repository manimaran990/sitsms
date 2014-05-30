#!/usr/bin/python

import sitsms
import sys
from PyQt4 import QtGui, QtCore

class Sitsms(QtGui.QWidget):

    def __init__(self):
        super(Sitsms, self).__init__()

        self.initUI()

    def initUI(self):

        number = QtGui.QLabel("Number ",self)
        number.move(20,20);

        message = QtGui.QLabel("Message ",self)
        message.move(20,60);

        self.numberEdit = QtGui.QLineEdit(self)
        self.numberEdit.resize(190,24);
        self.numberEdit.move(80,20);
        self.messageEdit = QtGui.QTextEdit(self)
        self.messageEdit.resize(220,200)
        self.messageEdit.move(80,60);

        self.sendbtn = QtGui.QPushButton("send",self)
        self.sendbtn.setStyleSheet("QPushButton:pressed { background-color: green }"
                      "QPushButton:released { background-color: gray }" )
        quitbtn = QtGui.QPushButton("Exit",self)

        self.sendbtn.clicked.connect(self.buttonClicked)
        self.sendbtn.move(80,280)

        quitbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        quitbtn.move(200,280)

        self.setGeometry(300,350,320,320)
        self.setFixedSize(320,320)
        self.setWindowTitle('SitSms')
        self.show()


    def buttonClicked(self):
        numlen = len(self.numberEdit.text())
        msglen = len(self.messageEdit.toPlainText())

        if numlen==0:
            QtGui.QMessageBox.information(self,'info',"please fill your number",1)
        elif numlen>10:
            QtGui.QMessageBox.information(self,'info',"number count must be 10 digits",1)
	else:
	    num = self.numberEdit.text()
	    if msglen>145:
	        QtGui.QMessageBox.information(self,'info',"your message is trimmed to 145 chars",1)
	    message = self.messageEdit.toPlainText()[:145]
	    sitsms.loginsite()
	    sitsms.sendsms(num,message)
	    QtGui.QMessageBox.information(self,'info','Message delivered to '+num,1)

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Sitsms()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
