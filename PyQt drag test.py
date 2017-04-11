# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 18:23:33 2017

@author: Brian
"""

import sys
from PyQt4 import QtGui, QtCore

class Homework(QtGui.QWidget):
    
    sqX = 50
    sqY = 50
    ptX =5
    ptY =5
    posX = 0
    posY = 0    
    colorA = 0
    colorB = 0
    colorC = 0
    color = QtGui.QColor(0,204,0)
    def __init__(self):
        super(Homework, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300,300,600,400)
        self.setWindowTitle('HW 4F')
        self.show()
        
    def paintEvent(self, e):
        hw = QtGui.QPainter()
        hw.begin(self)
        self.drawBackground(hw)
        self.drawSquare(hw)
        hw.end()
                
        
    def drawBackground(self, hw):
        color = QtGui.QColor(255,255,255)
        color.setNamedColor('#FFFFFF')
        hw.setPen(color)
        
        hw.setBrush(QtGui.QColor(255,255,255))
        hw.drawRect(0,0,600,400)
        
    def drawSquare(self,hw):
        
        color = QtGui.QColor(0,204,0)
        color.setNamedColor('#00cc00')
        hw.setPen(color)
        #self.color = QtGui.QColor(0,204,0)
        hw.setBrush(self.color)
        hw.drawRect(self.ptX,self.ptY, self.sqX, self.sqY)
#        hw.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        
    def mousePressEvent(self, e):
        self.posX = e.x()
        self.posY = e.y()
        if e.x() > self.ptX and e.x() < self.ptX +self.sqX:
            if e.y() > self.ptY and e.y() < self.ptY+self.sqY:
                self.posX = e.x()
                self.posY = e.y()
                self.update()
    def mouseMoveEvent(self, e):
        if e.x() > self.ptX and e.x() < self.ptX +self.sqX:
            if e.y() > self.ptY and e.y() < self.ptY+self.sqY:
                if e.x() != self.posX or e.y() != self.posY:
                    self.ptX = e.x() - self.posX
                    self.ptY = e.y() - self.posY
                    self.update()
                
    def mouseDoubleClickEvent(self,e):
        if e.x() >self.ptX and e.x() < self.ptX +self.sqX:
            if e.y() > self.ptY and e.y() < self.ptY+self.sqY:
                #QtGui.QColorDialog.open(self)
                self.color = QtGui.QColorDialog.getColor()
                self.update()
                
def main():
    app = QtGui.QApplication(sys.argv)
    hwk = Homework()
    
    sys.exit(app.exec_())
    
if __name__=='__main__':
    main()