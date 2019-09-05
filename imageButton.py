from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import *

class ImageButton(QAbstractButton):
    def __init__(self,pixmap, pixmap_hover, pixmap_pressed,parent=None):
        super(ImageButton, self).__init__(parent)
        self.x=0
        self.y=0
        self.w=40
        self.h=30
        self.pixmap = pixmap
        self.pixmap_hover = pixmap_hover
        self.pixmap_pressed = pixmap_pressed
        self.text=QLabel(self)
        self.text.setObjectName("imagebuttontext")
        self.text.setAttribute(Qt.WA_TranslucentBackground)

        self.text.setText("")
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.pressed.connect(self.update)
        self.released.connect(self.update)
        self.setSize(0,0,40,30)

    def setSize(self,x,y,w,h):   
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.setGeometry(x, y, w,h)
        self.text.setGeometry(0, 0,w,h)
    def setBackground(self,pixmap, pixmap_hover, pixmap_pressed):
        self.pixmap = pixmap
        self.pixmap_hover = pixmap_hover
        self.pixmap_pressed = pixmap_pressed
    def paintEvent(self, event):
        pix = self.pixmap_hover if self.underMouse() else self.pixmap
        if self.isDown():
            pix = self.pixmap_pressed
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), pix)


    def setText(self,text,style=None):
        self.text.setText(text)
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        
        if(style == None):
            self.text.setStyleSheet("color: white")
        else:
            self.text.setStyleSheet(style)    
    
    def setIcon(self,icon):
        self.text.setPixmap(icon)

    def sizeHint(self):
        return QSize(self.w, self.h)