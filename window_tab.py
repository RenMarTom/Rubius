from PyQt6.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QMainWindow, \
    QWidget, QLabel, QLineEdit, QTextEdit, QTabWidget
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Запись секретного приложения")

        self.mainL = QVBoxLayout()
        self.main = QWidget()

        self.tab1L = QVBoxLayout()
        self.tab1 = QWidget()
        self.tab2L = QVBoxLayout()
        self.tab2 = QWidget()
        self.tabbar = QTabWidget()

        self.file_namelab = QLabel("Название файла")
        self.file_name = QLineEdit()

        self.secretlab = QLabel("Секретная часть названия файла")
        self.secret_file_name = QLineEdit()
        self.secret_file_name.setEchoMode(QLineEdit.EchoMode.Password)

        self.file_namelab.setStyleSheet("QLabel{color:#0099FF}")
        self.secretlab.setStyleSheet("QLabel{color:#0099FF}")
        self.file_name.setStyleSheet("QLineEdit{background-color:#000000; color:#FF0000}")
        self.secret_file_name.setStyleSheet("QLineEdit{background-color:#000000; color:#FF0000}")

        self.text = QTextEdit()

        self.buttonL = QHBoxLayout()
        self.button_save = QPushButton(text="Сохранить")
        self.button_load = QPushButton(text="Загрузить")
        self.button_clear = QPushButton(text='Очистить')

        self.button_clear.setStyleSheet("QPushButton{background-color: #FFF5EE; color:#000}")

        self.button_save.clicked.connect(self.save_file)
        self.button_load.clicked.connect(self.load_file)
        self.button_clear.clicked.connect(self.clear)

        self.buttonL.addWidget(self.button_load)
        self.buttonL.addWidget(self.button_save)
        self.buttonL.addWidget(self.button_clear)

        self.tab1L.addWidget(self.file_namelab)
        self.tab1L.addWidget(self.file_name)
        self.tab1L.addWidget(self.secretlab)
        self.tab1L.addWidget(self.secret_file_name)
        self.tab1L.addLayout(self.buttonL)
        self.tab1.setLayout(self.tab1L)

        self.tab2L.addWidget(self.text)
        self.tab2.setLayout(self.tab2L)

        self.tabbar.addTab(self.tab1, "Настройки")
        self.tabbar.addTab(self.tab2, "Текст")

        self.mainL.addWidget(self.tabbar)
        self.main.setLayout(self.mainL)
        self.setCentralWidget(self.main)

    def save_file(self):
        f = open(self.file_name.text() + self.secret_file_name.text() + ".txt", "w")
        f.write(self.text.toPlainText())
        f.close()
        self.file_name.clear()
        self.secret_file_name.clear()
        self.text.clear()

    def load_file(self):
        f = open(self.file_name.text() + self.secret_file_name.text() + ".txt", "r")
        t = f.read()
        self.text.setPlainText(t)

    def clear(self):
        self.file_name.clear()
        self.secret_file_name.clear()
        self.text.clear()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
