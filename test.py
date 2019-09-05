# coding=utf-8
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import *
from imageButton import ImageButton

class Ui_MainWindow(QMainWindow):
    
    def setupUi(self):
        self.resize(300, 200)
        self.setStyleSheet("background-color: #424242;")
        self.pixmap = QPixmap("./pixmap.png")
        self.pixmap_hover = QPixmap("pixmap_hover.png")
        self.pixmap_pressed = QPixmap("pixmap_pressed.png")
        self.text="My Text"
        self.btn= ImageButton(self.pixmap,self.pixmap_hover,self.pixmap_pressed,self)
        self.btn.setText(self.text)
        self.btn.clicked.connect(self.myclick)
        self.btn.setSize(10, 10, 150, 30)

    def myclick(self):
        print("clicked")
    
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    mainwindow1 = Ui_MainWindow()
    mainwindow1.setupUi()
    mainwindow1.show()
    sys.exit(app.exec_())
    