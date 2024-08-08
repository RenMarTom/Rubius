from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QHBoxLayout, \
    QVBoxLayout, QComboBox, QLineEdit, QDialog
import random
import sys


class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Saving result")

        self.dlgL = QVBoxLayout()

        self.nameL = QHBoxLayout()
        self.name_lab = QLabel('Enter your name')
        self.name = QLineEdit()

        self.nameL.addWidget(self.name_lab)
        self.nameL.addWidget(self.name)

        self.button_save = QPushButton('Save')

        self.button_save.clicked.connect(self.save_file)

        self.dlgL.addLayout(self.nameL)
        self.dlgL.addWidget(self.button_save)

        self.setLayout(self.dlgL)

    def save_file(self):
        file = open(f'level{window.level1}.txt', "a")
        file.write(f'{self.name.text()} {window.k} {window.number1}' + '\n')
        file.close()
        self.close()
        window.text.clear()
        window.field2.setText('Waiting for the start...')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Numbers game")

        self.main = QWidget()
        self.mainL = QVBoxLayout()

        self.level = QHBoxLayout()

        self.level_lab = QLabel('Choose level')
        self.combo = QComboBox()
        self.combo.addItems(['1', '2', '3'])
        self.button_start = QPushButton('Start')
        self.button_start.setStyleSheet('QPushButton{background-color: #9f9; border-radius: 4px}')

        self.level.addWidget(self.level_lab)
        self.level.addWidget(self.combo)
        self.level.addWidget(self.button_start)

        self.field1L = QHBoxLayout()

        self.lab1 = QLabel('Enter the number')
        self.text = QLineEdit()

        self.field1L.addWidget(self.lab1)
        self.field1L.addWidget(self.text)

        self.field2 = QLineEdit('Waiting for the start...')

        self.lab2 = QLabel('Enter the number')

        self.buttonsL = QHBoxLayout()

        self.button_check = QPushButton('Check')
        self.button_check.setStyleSheet("QPushButton{background-color: #ccf; border-radius: 2.5px}")
        self.button_restart = QPushButton('Restart')
        self.button_restart.setStyleSheet("QPushButton{background-color: #fcc; border-radius: 2.5px}")

        self.button_start.clicked.connect(self.logic_app)
        self.button_check.clicked.connect(self.check_number)
        self.button_restart.clicked.connect(self.logic_app)

        self.buttonsL.addWidget(self.button_check)
        self.buttonsL.addWidget(self.button_restart)

        self.mainL.addLayout(self.level)
        self.mainL.addLayout(self.field1L)
        self.mainL.addWidget(self.field2)
        self.mainL.addLayout(self.buttonsL)

        self.main.setLayout(self.mainL)
        self.setCentralWidget(self.main)

    def logic_app(self):
        self.field2.setStyleSheet("QLineEdit{background-color: none}")
        self.k = 1
        self.level1 = self.combo.currentText()
        self.level1 = int(self.level1)
        self.n = 10 ** self.level1
        self.number1 = random.randint(0, self.n)
        self.field2.setText('The game has started')
        self.text.clear()

    def check_number(self):
        number = int(self.text.text())
        if number > self.number1:
            self.field2.setText('Number is bigger, than original one')
            self.text.clear()
            self.k += 1
        elif number < self.number1:
            self.field2.setText('Number is less than the original one')
            self.text.clear()
            self.k += 1
        else:
            self.field2.setStyleSheet("QLineEdit{background-color: #9f9; border-radius: 4px}")
            self.field2.setText('Congrats!')
            dlg = Dialog()
            dlg.exec()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
