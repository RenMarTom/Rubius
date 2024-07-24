from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget
from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Первое приложение на Python")

        self.mainL = QVBoxLayout()
        self.main = QWidget()

        self.label1 = QLabel("Внизу меня находится кнопка")
        self.button1 = QPushButton(text="Нажмите меня")

        self.button1.clicked.connect(self.ch_name)

        self.mainL.addWidget(self.label1)
        self.mainL.addWidget(self.button1)

        self.main.setLayout(self.mainL)
        self.main.setFixedHeight(100)

        self.setCentralWidget(self.main)
        self.resize(1000,150)

        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def ch_name(self):
        self.button1.setText("Нажато")




if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
