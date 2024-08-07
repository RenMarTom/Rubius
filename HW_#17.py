from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, \
    QCheckBox, QRadioButton, QProgressBar
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.value = 0

        self.setWindowTitle('Выбор элементов')

        self.MainL = QVBoxLayout()
        self.Main = QWidget()

        self.boxL = QHBoxLayout()

        self.radio_buttons = QGroupBox()
        self.radio_buttonsL = QVBoxLayout()

        self.radio1 = QRadioButton('Red')
        self.radio2 = QRadioButton('Green')
        self.radio3 = QRadioButton('Blue')

        self.radio1.clicked.connect(self.red)
        self.radio2.clicked.connect(self.green)
        self.radio3.clicked.connect(self.blue)

        self.radio_buttonsL.addWidget(self.radio1)
        self.radio_buttonsL.addWidget(self.radio2)
        self.radio_buttonsL.addWidget(self.radio3)

        self.radio_buttons.setLayout(self.radio_buttonsL)

        self.check_box = QGroupBox()
        self.check_boxL = QVBoxLayout()

        self.check1 = QCheckBox('+1')
        self.check2 = QCheckBox('+2')
        self.check3 = QCheckBox('+3')
        self.check4 = QCheckBox('+4')

        self.check1.clicked.connect(self.first)
        self.check2.clicked.connect(self.second)
        self.check3.clicked.connect(self.third)
        self.check4.clicked.connect(self.fourth
