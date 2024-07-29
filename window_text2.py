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

        self.button_save.clicked.connect(self.save_file)
        # self.button_load.clicked.connect(self.load_file)

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

    def save_file(self):
        f = open(self.file_name.text()+self.secret_file_name.text()+".txt", "w")
        f.write(self.text.toPlainText())
        f.close()
        self.file_name.clear()
        self.secret_file_name.clear()
        self.text.clear()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
