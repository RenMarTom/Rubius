from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,\
    QPushButton, QLabel, QDialog, QComboBox
import sys


class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Выбор слова")
        self.digL = QVBoxLayout()
        self.combo = QComboBox()
        self.combo.addItems(["Путин", "Бензин", "Лошадь", "Гора", "Турция", "Пылесос"])
        self.buttonL = QHBoxLayout()
        self.button_accept = QPushButton("Принять")
        self.button_reject = QPushButton("Отмена")

        self.button_accept.clicked.connect(self.acceptDef)
        self.button_reject.clicked.connect(self.rejectDef)

        self.buttonL.addWidget(self.button_accept)
        self.buttonL.addWidget(self.button_reject)

        self.digL.addWidget(self.combo)
        self.digL.addLayout(self.buttonL)

        self.setLayout(self.digL)

    def acceptDef(self):
        self.accept()

    def rejectDef(self):
        self.reject()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Игра в слова")

        self.main = QWidget()
        self.mainL = QVBoxLayout()

        self.label = QLabel("Выберите слово")

        self.button = QPushButton("Выбор слова")
        self.button.clicked.connect(self.startDig)

        self.mainL.addWidget(self.label)
        self.mainL.addWidget(self.button)

        self.main.setLayout(self.mainL)
        self.setCentralWidget(self.main)

    def startDig(self):
        dlg = Dialog()

        if dlg.exec():
            self.label.setText(dlg.combo.currentText())

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
