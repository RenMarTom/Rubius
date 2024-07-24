from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QMainWindow, QWidget;
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

        self.button1.setFixedWidth(100)
        self.button1.setFixedHeight(100)
        self.button2.setFixedWidth(50)
        self.button2.setFixedHeight(200)
        self.button3.setFixedWidth(200)
        self.button3.setFixedHeight(500)

        self.label1 = QLabel("1")
        self.label2 = QLabel("2")
        self.label3 = QLabel("3")


        self.L1 = QVBoxLayout()
        self.L2 = QVBoxLayout()
        self.L3 = QVBoxLayout()

        self.L1.addWidget(self.label1)
        self.L1.addWidget(self.button1)
        self.L2.addWidget(self.label2)
        self.L2.addWidget(self.button2)
        self.L3.addWidget(self.label3)
        self.L3.addWidget(self.button3)

        self.mainL.addLayout(self.L1)
        self.mainL.addLayout(self.L2)
        self.mainL.addLayout(self.L3)


        self.mainL.addWidget(self.button1)
        self.mainL.addWidget(self.button2)

        self.main.setLayout(self.mainL)
        self.main.setFixedHeight(100)

        self.setCentralWidget(self.main)

    def ch_name1(self):
        if self.button1.isChecked():
            self.button1.setText("Нажато")
        else:
            self.button1.setText("Нажми меня")

    def ch_name2(self):
        if self.button2.isChecked():
            self.button2.setText("Тоже нажато")
        else:
            self.button2.setText("Нажми меня")


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

