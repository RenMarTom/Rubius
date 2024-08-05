from PyQt6.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QMainWindow, \
    QWidget, QLabel, QLineEdit, QTextEdit, QTabWidget, QScrollArea, QGridLayout, QTableWidget, \
    QTableWidgetItem

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Запись секретного приложения")

        self.mainL = QVBoxLayout()
        self.main = QWidget()

        self.tab1L = QGridLayout()
        self.tab1 = QWidget()
        self.tab2L = QVBoxLayout()
        self.tab2 = QWidget()

        self.table = QTableWidget()
        self.table.setRowCount(3)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['мама', 'мыла', 'раму'])
        self.table.setVerticalHeaderLabels(['папа', 'не мыл', 'раму'])
        items_for_table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.set_data(items_for_table)

        self.tab_bar = QTabWidget()

        self.file_namelab = QLabel("Название файла")
        self.file_name = QLineEdit()

        self.secretlab = QLabel("Секретная часть навания файла")
        self.secret_file_name = QLineEdit()
        self.secret_file_name.setEchoMode(QLineEdit.EchoMode.Password)

        self.old_textlab = QLabel("Старый текст")
        self.old_text = QLabel()
        self.old_text.setWordWrap(True)
        self.scroll_old_text = QScrollArea()
        self.scroll_old_text.setWidget(self.old_text)
        self.new_textlab = QLabel("Новый текст")

        self.file_namelab.setStyleSheet("QLabel{color:#0099FF}")
        self.secretlab.setStyleSheet("QLabel{color:#0099FF}")
        self.file_name.setStyleSheet("QLineEdit{background-color:#000000; color:#FF0000}")
        self.secret_file_name.setStyleSheet("QLineEdit{background-color:#000000; color:#FF0000}")
        self.scroll_old_text.setStyleSheet("QScrollArea{border: 2px dotted green}")
        self.old_textlab.setStyleSheet("QLabel{background-color: #FF66CC; border-radius: 3px}")
        self.new_textlab.setStyleSheet("QLabel{background-color: #FF66CC; border-radius: 3px}")

        self.text = QTextEdit()
        self.text.setStyleSheet("QTextEdit{border: 2px dotted #00FF66}")

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

        self.tab1L.addWidget(self.file_namelab, 0, 0)
        self.tab1L.addWidget(self.file_name, 0, 1)
        self.tab1L.addWidget(self.secretlab, 1, 0)
        self.tab1L.addWidget(self.secret_file_name, 1, 1)
        self.tab1L.addLayout(self.buttonL, 2, 0)
        self.tab1.setLayout(self.tab1L)

        self.tab2L.addWidget(self.old_textlab)
        self.tab2L.addWidget(self.scroll_old_text)
        self.tab2L.addWidget(self.new_textlab)
        self.tab2L.addWidget(self.text)
        self.tab2.setLayout(self.tab2L)


        self.tab_bar.addTab(self.tab1, "Настройки")
        self.tab_bar.addTab(self.tab2, "Текст")
        self.tab_bar.addTab(self.table, 'Таблица')

        self.mainL.addWidget(self.tab_bar)
        self.main.setLayout(self.mainL)
        self.setCentralWidget(self.main)

    def save_file(self):
        f = open(self.file_name.text() + self.secret_file_name.text() + ".txt", "a")
        f.write("\n" + self.text.toPlainText())
        f.close()
        self.file_name.clear()
        self.secret_file_name.clear()
        self.text.clear()

    def load_file(self):
        self.scroll_old_text.setWidgetResizable(True)
        f = open(self.file_name.text() + self.secret_file_name.text() + ".txt", "r")
        t = f.read()
        self.old_text.setText(t)
        f.close()

    def set_data(self, items):
        x = 0
        y = 0
        for row_items in items:
            for col_item in row_items:
                table_item = QTableWidgetItem(str(col_item))
                self.table.setItem(y, x, table_item)
                x += 1
            x = 0
            y += 1

    def clear(self):
        self.file_name.clear()
        self.secret_file_name.clear()
        self.text.clear()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
