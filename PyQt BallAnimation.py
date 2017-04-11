# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 18:12:37 2017

@author: Brian
"""

import sys
from PyQt4 import QtGui, QtCore

class Homework(QtGui.QWidget):
    
    xVel = 1
    yVel = 1
    xLoc= 15
    yLoc = 15
    xGeo = 600
    yGeo = 400    
    
    def __init__(self):
        super(Homework, self).__init__()
        
        
        self.initUI()
        
    def initUI(self):      
        
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('HW 4W')
        self.show()

    def paintEvent(self, e):

        hw = QtGui.QPainter()
        hw.begin(self)
        self.drawRectangles(hw) #calls drawrectangels to set the background to white
        self.drawCircle(hw)     #calls drawcircle that creates a circle with radius 15 set to point p
                                #point x and y axis are set to variables so they can later be added by velocity in animate funct.
        QtCore.QTimer.singleShot(30,self.animate(hw))   #timer that animates every 30ms
        hw.end()
        
    def drawRectangles(self, hw):
      
        color = QtGui.QColor(255,255,255)
        color.setNamedColor('#FFFFFF')
        hw.setPen(color)

#        self.xGeo = QtCore.QRect.height(self)
#        self.yGeo = QtCore.QRect.width(self)
        hw.setBrush(QtGui.QColor(255,255 ,255))
        hw.drawRect(0, 0, self.xGeo, self.yGeo)
        
        

    def drawCircle(self, hw):
        
        p = QtCore.QPoint(self.xLoc,self.yLoc)
        color = QtGui.QColor(255,0,0)
        color.setNamedColor('FF0000')
        hw.setPen(color)
        
        hw.setBrush(QtGui.QColor(255,0,0))
        hw.drawEllipse(p,15,15)
             
    def animate(self, hw):
        self.xLoc += self.xVel  #adds velocity to point variables used to create the circle
        self.yLoc += self.yVel
        self.checkCollision(hw)
        self.checkGeometry(hw)
        self.update()
        
    
    def checkCollision(self,hw):
        if self.xLoc > self.xGeo - 15:
            self.xVel *= -1
        if self.yLoc > self.yGeo - 15:
            self.yVel *= -1
        if self.xLoc < 15:
            self.xVel *= -1
        if self.yLoc < 15:
            self.yVel *= -1            
        
    def checkGeometry(self,hw):
        if self.xGeo != 600:
            self.xGeo = QtGui.QWidget.height(self)
           
        if self.yGeo != 400:
            self.yGeo = QtGui.QWidget.width(self)
                       
            
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Homework()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()