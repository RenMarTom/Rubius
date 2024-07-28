from PyQt6.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QMainWindow, QWidget, QLabel
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Первое приложение PyQT")

        self.mainL = QHBoxLayout()
        self.main = QWidget()

        self.button1 = QPushButton(text="1")
        self.button2 = QPushButton(text="2")
        self.button3 = QPushButton(text="3")

        self.button1.setCheckable(True)
        self.button2.setCheckable(True)
        self.button3.setCheckable(True)

        self.button1.clicked.connect(self.click_but_fun1)
        self.button2.clicked.connect(self.click_but_fun2)
        self.button3.clicked.connect(self.click_but_fun3)

        self.lab1 = QLabel("1")
        self.lab2 = QLabel("2")
        self.lab3 = QLabel("3")

        self.L1 = QVBoxLayout()
        self.L2 = QVBoxLayout()
        self.L3 = QVBoxLayout()

        self.L1.addWidget(self.lab1)
        self.L1.addWidget(self.button1)

        self.L2.addWidget(self.lab2)
        self.L2.addWidget(self.button2)

        self.L3.addWidget(self.lab3)
        self.L3.addWidget(self.button3)

        self.mainL.addLayout(self.L1)
        self.mainL.addLayout(self.L2)
        self.mainL.addLayout(self.L3)

        self.button1.setFixedHeight(20)
        self.button1.setFixedWidth(80)
        self.button2.setFixedHeight(20)
        self.button2.setFixedWidth(80)
        self.button3.setFixedHeight(20)
        self.button3.setFixedWidth(80)

        self.main.setLayout(self.mainL)
        self.main.setFixedHeight(100)

        self.setCentralWidget(self.main)

    def click_but_fun1(self):
        if self.button1.isChecked():
            self.button1.setFixedHeight(50)
            self.button1.setFixedWidth(60)

        else:
            self.button1.setFixedHeight(20)
            self.button1.setFixedWidth(80)

    def click_but_fun2(self):
        if self.button2.isChecked():
            self.button2.setFixedHeight(50)
            self.button2.setFixedWidth(60)
        else:
            self.button2.setFixedHeight(20)
            self.button2.setFixedWidth(80)

    def click_but_fun3(self):
        if self.button3.isChecked():
            self.button3.setFixedHeight(50)
            self.button3.setFixedWidth(60)
        else:
            self.button3.setFixedHeight(20)
            self.button3.setFixedWidth(80)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
