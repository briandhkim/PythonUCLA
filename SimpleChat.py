# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 10:20:24 2017

@author: Brian
"""

import socket
from PyQt4.QtGui import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QLineEdit, QPushButton, QHBoxLayout
from PyQt4 import QtCore
from PyQt4.QtCore import QTimer

def Connector():
    def beClient():
        s = socket.socket()
        s.connect(('127.0.0.1', 5000))
        typ = "client"
        return s, typ
               
    def beServer():
        ss = socket.socket()
        
        ss.bind(('127.0.0.1', 5000))
        ss.listen(1)
        s, addr = ss.accept()
        typ = "server"
        return s, typ
                
    try:
        return beClient()
    except:
        return beServer()
        



class MyWidget(QWidget):
    soc, typ = Connector()
    print type(soc)    
    soc.settimeout(0.25)
    
    
    def __init__(self):
        super(MyWidget,self).__init__()
        
        self.setWindowTitle("Chat App")
        self.setGeometry(100,100,400,300)
        
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.layout2 = QHBoxLayout(self)
        self.button = QPushButton("Push Me")
        
        self.widget2 = QWidget()
        self.widget2.setLayout(self.layout2)

        self.textEdit = QTextEdit()
        self.textEdit.setText("Connected as: <" + self.typ + ">")
        
        self.textLine = QLineEdit()
        self.textLine.setText("enter message...")
        
        self.layout.addWidget(self.textEdit)
        
        self.layout2.addWidget(self.textLine)        
        self.layout2.addWidget(self.button)
        
        self.layout.addWidget(self.widget2)
        
        if self.soc is not None:
            self.setWindowTitle("Chat App - Connected <" + self.typ + ">")
            
        self.button.clicked.connect(self.buttonClick)
        self.textLine.returnPressed.connect(self.buttonClick)
        
        self.qt = QTimer(self)
        self.qt.timeout.connect(self.timer)
        self.qt.start(2000)
        
        self.show()
        
        
    def buttonClick(self):
        sender = self.textLine.text()
        self.soc.send(sender)
        self.textEdit.setText("Sent: " + sender)
        self.textLine.setText("")
        
    def timer(self):

        try:
            txt = self.soc.recv(1024)
            if txt == "":
                self.qt.stop()
                txt = "<Connection Terminated>"
            self.textEdit.setText("Received: " + txt)
        except:
            pass

        

def main():
    app = QApplication([])  
    q = MyWidget()
    app.exec_()
    

if __name__ == "__main__":
    main()
