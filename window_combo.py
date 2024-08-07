from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, \
    QDialog, QLabel, QComboBox
import sys


class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Word choice')
        self.digL = QVBoxLayout()
        self.combo = QComboBox()
        self.combo.addItems(["рама", "бензин", "лошадь", "Путин", "пылесос"])

        self.buttonsL = QHBoxLayout()
        self.button_accept = QPushButton("Accept")
        self.button_reject = QPushButton("Reject")

        self.button_accept.clicked.connect(self.acceptDef)
        self.button_reject.clicked.connect(self.rejectDef)

        self.buttonsL.addWidget(self.button_accept)
        self.buttonsL.addWidget(self.button_reject)

        self.digL.addWidget(self.combo)
        self.digL.addLayout(self.buttonsL)

        self.setLayout(self.digL)

    def acceptDef(self):
        self.accept()

    def rejectDef(self):
        self.reject()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Words game')

        self.main = QWidget()
        self.mainL = QVBoxLayout()

        self.lab = QLabel("Choose word")

        self.button = QPushButton("Word choice")
        self.button.clicked.connect(self.startDig)

        self.mainL.addWidget(self.lab)
        self.mainL.addWidget(self.button)

        self.main.setLayout(self.mainL)
        self.setCentralWidget(self.main)

    def startDig(self):
        dlg = Dialog()

        if dlg.exec():
            self.lab.setText(dlg.combo.currentText())


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
