from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, \
    QCheckBox, QRadioButton, QProgressBar
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Выбор элементов')

        self.MainL = QVBoxLayout()
        self.Main = QWidget()

        self.boxL = QHBoxLayout()

        self.radio_buttons = QGroupBox()
        self.radio_buttonsL = QVBoxLayout()

        self.radio1 = QRadioButton('1')
        self.radio2 = QRadioButton('2')
        self.radio3 = QRadioButton('3')
        self.radio4 = QRadioButton('4')

        self.radio_buttonsL.addWidget(self.radio1)
        self.radio_buttonsL.addWidget(self.radio2)
        self.radio_buttonsL.addWidget(self.radio3)
        self.radio_buttonsL.addWidget(self.radio4)

        self.radio_buttons.setLayout(self.radio_buttonsL)

        self.check_box = QGroupBox()
        self.check_boxL = QVBoxLayout()

        self.check1 = QCheckBox('Первый')
        self.check2 = QCheckBox('Второй')
        self.check3 = QCheckBox('Третий')
        self.check4 = QCheckBox('Четвёртый')

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
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(52)

        self.MainL.addLayout(self.boxL)
        self.MainL.addWidget(self.progress_bar)

        self.Main.setLayout(self.MainL)
        self.setCentralWidget(self.Main)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
