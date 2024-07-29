from PyQt6.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QMainWindow, QWidget, QLabel
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пятое приложение PyQT")

        self.mainL = QHBoxLayout()
        self.main = QWidget()

        self.button1 = QPushButton(text="green")
        self.button2 = QPushButton(text="red")
        self.button3 = QPushButton(text="blue")

        # self.button1.setCheckable(True)
        # self.button2.setCheckable(True)
        # self.button3.setCheckable(True)
        #
        # self.button1.clicked.connect(self.click_but_fun1)
        # self.button2.clicked.connect(self.click_but_fun2)
        # self.button3.clicked.connect(self.click_but_fun3)

        self.lab1 = QLabel("black")
        self.lab2 = QLabel("yellow")
        self.lab3 = QLabel("white")

        self.L1 = QVBoxLayout()
        self.L2 = QVBoxLayout()
        self.L3 = QVBoxLayout()

        self.button1.setStyleSheet("QPushButton{background-color:#0000ff;color:#ff99cc;width:100px;height:50px;"
                                   "font-size:20px;border:1px solid white}"
                                   "QPushButton::pressed{background-color:#ffffff; border-color:#000000}")
        self.button2.setStyleSheet("QPushButton{background-color:#cc99ff;color:#3300ff;width:100px;height:50px;"
                                   "font-size:40px;border:8px solid yellow}"
                                   "QPushButton::pressed{background-color:#ffffff; border-color:#000000}")
        self.button3.setStyleSheet("QPushButton{background-color:#ccff00;color:#66ff66;width:100px;height:50px;"
                                   "font-size:30px;border:4px solid lightgreen}"
                                   "QPushButton::pressed{background-color:#ffffff; border-color:#000000}")

        self.lab1.setStyleSheet("QLabel{background-color:#336600;color:#ffff99;width:100px;height:50px;"
                                "font-size:35px;border:7px solid red}"
                                "QLabel::hover{background-color:#ffffff; border-color:#000000}")
        self.lab2.setStyleSheet("QLabel{background-color:#11aabb;color:#cc0000;width:100px;height:50px;"
                                "font-size:45px;border:13px solid blue}"
                                "QLabel::hover{background-color:#ffffff; border-color:#000000}")
        self.lab3.setStyleSheet("QLabel{background-color:#555555;color:#3399ff;width:100px;height:50px;"
                                "font-size:25px;border:6px solid magenta}"
                                "QLabel::hover{background-color:#ffffff; border-color:#000000}")

        self.L1.addWidget(self.lab1)
        self.L1.addWidget(self.button1)

        self.L2.addWidget(self.lab2)
        self.L2.addWidget(self.button2)

        self.L3.addWidget(self.lab3)
        self.L3.addWidget(self.button3)

        self.mainL.addLayout(self.L1)
        self.mainL.addLayout(self.L2)
        self.mainL.addLayout(self.L3)

        # self.button1.setFixedHeight(20)
        # self.button1.setFixedWidth(80)
        # self.button2.setFixedHeight(20)
        # self.button2.setFixedWidth(80)
        # self.button3.setFixedHeight(20)
        # self.button3.setFixedWidth(80)

        self.main.setLayout(self.mainL)
        # self.main.setFixedHeight(100)

        self.setCentralWidget(self.main)

    # def click_but_fun1(self):
    #     if self.button1.isChecked():
    #         self.button1.setFixedHeight(50)
    #         self.button1.setFixedWidth(60)
    #
    #     else:
    #         self.button1.setFixedHeight(20)
    #         self.button1.setFixedWidth(80)
    #
    # def click_but_fun2(self):
    #     if self.button2.isChecked():
    #         self.button2.setFixedHeight(50)
    #         self.button2.setFixedWidth(60)
    #     else:
    #         self.button2.setFixedHeight(20)
    #         self.button2.setFixedWidth(80)
    #
    # def click_but_fun3(self):
    #     if self.button3.isChecked():
    #         self.button3.setFixedHeight(50)
    #         self.button3.setFixedWidth(60)
    #     else:
    #         self.button3.setFixedHeight(20)
    #         self.button3.setFixedWidth(80)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
