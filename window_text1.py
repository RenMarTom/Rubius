from PyQt6.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QMainWindow, QWidget, QLabel, QLineEdit, QTextEdit
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Запись секретного приложения")

        self.mainL = QVBoxLayout()
        self.main = QWidget()

        self.file_namelab = QLabel("Название файла")
        self.file_name = QLineEdit()

        self.secretlab = QLabel("Секретная часть названия файла")
        self.secret_file_name = QLineEdit()

        self.text = QTextEdit()

        self.buttonL = QHBoxLayout()
        self.button_save = QPushButton(text = "Сохранить")
        self.button_load = QPushButton(text = "Загрузить")

        self.buttonL.addWidget(self.button_load)
        self.buttonL.addWidget(self.button_save)

        self.mainL.addWidget(self.file_namelab)
        self.mainL.addWidget(self.file_name)
        self.mainL.addWidget(self.secretlab)
        self.mainL.addWidget(self.secret_file_name)
        self.mainL.addWidget(self.text)
        self.mainL.addLayout(self.buttonL)


        self.main.setLayout(self.mainL)
        self.setCentralWidget(self.main)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
