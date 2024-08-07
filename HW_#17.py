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
        self.check4.clicked.connect(self.fourth)

        self.check_boxL.addWidget(self.check1)
        self.check_boxL.addWidget(self.check2)
        self.check_boxL.addWidget(self.check3)
        self.check_boxL.addWidget(self.check4)
        self.check_box.setLayout(self.check_boxL)

        self.boxL.addWidget(self.radio_buttons)
        self.boxL.addWidget(self.check_box)

        self.radio_buttons.setLayout(self.radio_buttonsL)

        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(10)
        self.progress_bar.setValue(self.value)


        self.MainL.addLayout(self.boxL)
        self.MainL.addWidget(self.progress_bar)

        self.Main.setLayout(self.MainL)
        self.setCentralWidget(self.Main)

    def red(self):
        self.Main.setStyleSheet("QWidget{background-color: #ff5555}")

    def green(self):
        self.Main.setStyleSheet("QWidget{background-color: #55ff55}")

    def blue(self):
        self.Main.setStyleSheet("QWidget{background-color: #5555ff}")

    def first(self):
        if self.check1.isChecked():
            self.value += 1
        else:
            self.value -= 1
        self.progress_bar.setValue(self.value)

    def second(self):
        if self.check2.isChecked():
            self.value += 2
        else:
            self.value -= 2
        self.progress_bar.setValue(self.value)

    def third(self):
        if self.check3.isChecked():
            self.value += 3
        else:
            self.value -= 3
        self.progress_bar.setValue(self.value)

    def fourth(self):
        if self.check4.isChecked():
            self.value += 4
        else:
            self.value -= 4
        self.progress_bar.setValue(self.value)



if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
