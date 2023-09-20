#!/usr/local/bin/python3
import typing
import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
    QTabWidget, 
    
)
from PyQt5.QtGui import QPalette, QColor




class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(QSize(300, 600))
        widget_0 = QWidget()
        widget_1 = QWidget()
        widget_2 = QWidget()
        widget_3 = QWidget()

        
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.setMovable(True)
        tabs.addTab(widget_2, 'Patrick')
        tabs.addTab(widget_1, 'blue')
        tabs.addTab(widget_3, 'green')
    
        # button1 = QPushButton(widget_0)
        # button1.setText("Button1")
        # button1.move(64,32)
        # button1.clicked.connect(self.button1_clicked)
        button_0 = self.button_mk(widget_1, grish='grish')
        button_1 = self.button_mk(widget_2, grish='patrick')
        button_2 = self.button_mk(widget_3, grish='Pedro')
    

        self.setCentralWidget(tabs)

    def button_clicked(self, btn_messege):
        print(str(btn_messege))

    def button_mk(self, group, **btn: dict):
        button = QPushButton(group)
        for key in btn.keys():
            button.setText(f'{btn[key]}')
            button.move(64, 32)
            button.clicked.connect(lambda: self.button_clicked(btn_messege=btn[key]))
    


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
