from PyQt6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QMainWindow, QWidget;
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Первое приложение PyQT")

        self.mainL = QVBoxLayout()
        self.main = QWidget()

        self.button1 = QPushButton(text="Нажми меня")
        self.button2 = QPushButton(text="Нажми меня тоже")

        self.button1.setCheckable(True)
        self.button2.setCheckable(True)

        self.button1.clicked.connect(self.ch_name1)
        self.button2.clicked.connect(self.ch_name2)

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
