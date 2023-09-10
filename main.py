from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QWidget
import sys
import math
import  re

num1 = ""
class App(QWidget):


    def __init__(self):
        self.start()
        self.button()

    def start(self):
        self.main_menu = uic.loadUi("untitled.ui")
        self.main_menu.show()

    def info(self,a):
        global num1
        num1 += a
        self.main_menu.textBrowser.setText(f"{num1}")
    def ontvet(self):
        global num1

        if re.search(r"cos",num1)[0]== "cos":
            num1 = str(math.cos(int(re.search(r"\d+",num1)[0])))

        elif re.search(r"sin",num1)[0] == "sin":
            num1 = str(math.sin(int(re.search(r"\d+",num1)[0])))

        else:
            num1 = str(eval(num1))

        self.main_menu.textBrowser.setText(f"{eval(num1)}")
    def button(self):
        self.main_menu.pushButton.clicked.connect(lambda: self.info('1'))
        self.main_menu.pushButton_2.clicked.connect(lambda: self.info('4'))
        self.main_menu.pushButton_3.clicked.connect(lambda: self.info('7'))
        self.main_menu.pushButton_4.clicked.connect(lambda: self.info('8'))
        self.main_menu.pushButton_5.clicked.connect(lambda: self.info('5'))
        self.main_menu.pushButton_6.clicked.connect(lambda: self.info('2'))
        self.main_menu.pushButton_7.clicked.connect(lambda: self.info('9'))
        self.main_menu.pushButton_8.clicked.connect(lambda: self.info('6'))
        self.main_menu.pushButton_9.clicked.connect(lambda: self.info('3'))
        self.main_menu.pushButton_10.clicked.connect(lambda: self.ontvet())
        self.main_menu.pushButton_11.clicked.connect(lambda: self.info("."))
        self.main_menu.pushButton_12.clicked.connect(lambda: self.info('0'))
        self.main_menu.pushButton_13.clicked.connect(lambda: self.info("/"))
        self.main_menu.pushButton_14.clicked.connect(lambda: self.info("*"))
        self.main_menu.pushButton_15.clicked.connect(lambda: self.info("-"))
        self.main_menu.pushButton_16.clicked.connect(lambda: self.info("+"))
        self.main_menu.pushButton_17.clicked.connect(lambda: self.info("**"))
        self.main_menu.pushButton_18.clicked.connect(lambda: self.info("cor"))
        self.main_menu.pushButton_19.clicked.connect(lambda: self.info("cos"))
        self.main_menu.pushButton_20.clicked.connect(lambda: self.info("sin"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()