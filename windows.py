#!/usr/local/bin/python3
import sys, time
import pyautogui
from structure.database import ImitateDatebase

juice_dbm = ImitateDatebase('juices').read()
persons_dbm = ImitateDatebase('persons').read()

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
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.setMovable(True)

        # Layouts
        layout_1 = QHBoxLayout()
        layout_2 = QHBoxLayout()

        # Tabs
        tab_1 = QWidget()
        tab_1.setLayout(layout_1)
        tab_2 = QWidget()
        tab_2.setLayout(layout_2)
        
        # buttons
        
        self.generate_buttons(persons_dbm, layout=layout_1)
        self.generate_buttons(juice_dbm, layout=layout_2)

        tabs.addTab(tab_1, 'Mardik')
        tabs.addTab(tab_2, 'Hyuter')
    

        self.setCentralWidget(tabs)


    def generate_buttons(self, buttons, layout):
            for button_name, button_text in buttons.items():
                button = QPushButton(button_text, self)
                button.clicked.connect(lambda checked, name=button_name: self.button_clicked(name))
                layout.addWidget(button)
            
    def button_clicked(self, btn_messege):
        messege = str(btn_messege)
        time.sleep(2)
        pyautogui.write(messege)

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
