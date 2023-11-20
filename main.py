from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QWidget,QMenu   # Импортируем все необходимые библотеки
import sys
import math


num1 = "" # Переменная для записи и вывода на TextBrowser окно
class App(QWidget): # Создаем основной класс нашей программы


    def __init__(self): # Инициализируем функции которые запустятся при старте программы
        self.start() # вызывается функция старт
        self.button() # вызывается функция кнопок
        self.main_menu.setFixedWidth(390) # задаем размер нашего окна
        self.main_menu.setFixedHeight(435) # задаем размер нашего окна

        self.main_menu.menuMenu.triggered.connect(lambda : self.engine()) # отслеживание состояния кнопки инженерного расширения
    def engine(self):

        if self.main_menu.action_3.isChecked(): # Проверка если кнопка инженерного меню нажата то выполняем действия ниже
            self.main_menu.setFixedWidth(650) # Меняем ширину нашего окна
            self.main_menu.setFixedHeight(435)
            self.main_menu.textBrowser.setFixedWidth(600) # Меняем ширину окна с текстом
            self.main_menu.pushButton_18.show()
            self.main_menu.pushButton_19.show()
            self.main_menu.pushButton_20.show()
            self.main_menu.pushButton_21.show()
            self.main_menu.pushButton_22.show()
            self.main_menu.pushButton_23.show()
            self.main_menu.pushButton_24.show()
            self.main_menu.pushButton_25.show()   # Показываем все кнопки инженерного калькулятора
            self.main_menu.pushButton_26.show()
            self.main_menu.pushButton_27.show()
            self.main_menu.pushButton_28.show()
            self.main_menu.pushButton_29.show()

        elif not self.main_menu.action_3.isChecked(): # Проверка если кнопка инженерного меню не нажата то выполняем действия ниже

            self.main_menu.setFixedWidth(390)
            self.main_menu.setFixedHeight(435)
            self.main_menu.textBrowser.setFixedWidth(370)
            self.main_menu.pushButton_18.hide()
            self.main_menu.pushButton_19.hide()
            self.main_menu.pushButton_20.hide()
            self.main_menu.pushButton_21.hide()
            self.main_menu.pushButton_22.hide()
            self.main_menu.pushButton_23.hide()
            self.main_menu.pushButton_24.hide()   # прячем все кнопки
            self.main_menu.pushButton_25.hide()
            self.main_menu.pushButton_26.hide()
            self.main_menu.pushButton_27.hide()
            self.main_menu.pushButton_28.hide()
            self.main_menu.pushButton_29.hide()
    def start(self):

        self.main_menu = uic.loadUi("untitled.ui") # Загружаем файл который мы создали в QTdesigner
        self.main_menu.show() # Запускаем окно

    def info(self,a): # функция для отображения на экране введенных данных
        global num1 # Делаем переменную глобальной что бы мы могли ее изменить
        num1 += a # Изменяем переменную добавляя туда передаваемые данные
        self.main_menu.textBrowser.setText(f"{num1}") # Выводим переменную на экран
    def cos(self): # функция считает косинус
        global num1
        self.main_menu.textBrowser.setText(f"{math.cos(int(num1))}") # Выводит ответ на экран
        num1 = str(math.cos(int(num1)))
    def sin(self): # считаем синус
        global num1
        self.main_menu.textBrowser.setText(f"{math.sin(int(num1))}") # Выводит ответ на экран
        num1 = str(math.sin(int(num1)))
    def cor(self): # Считаем корень
        global num1
        self.main_menu.textBrowser.setText(f"{math.sqrt(int(num1))}")# Выводит ответ на экран
        num1 = str(math.sqrt(int(num1)))
    def step2(self): # возводим число во 2 степень
        global num1
        self.main_menu.textBrowser.setText(f"{int(num1) ** 2}")# Выводит ответ на экран
        num1 = str(int(num1) ** 2)
    def step3(self):# возводим число во 3 степень
        global num1
        self.main_menu.textBrowser.setText(f"{int(num1) ** 3}")# Выводит ответ на экран
        num1 = str(int(num1)**3)
    def tan(self): # Считаем тангенс
        global num1
        self.main_menu.textBrowser.setText(f"{math.tan(int(num1))}")# Выводит ответ на экран
        num1 = str(math.tan(int(num1)))
    def cat(self): # считаем катангенс
        global num1
        self.main_menu.textBrowser.setText(f"{math.cos(int(num1))/ math.sin(int(num1))}")# Выводит ответ на экран
        num1 = str(math.cos(int(num1))/ math.sin(int(num1)))
    def log(self): # считаем логорифм
        global num1
        self.main_menu.textBrowser.setText(f"{math.log(int(num1))}")# Выводит ответ на экран
        num1 = str(math.log(int(num1)))
    def fact(self): # высчитываем факториал
        global num1
        self.main_menu.textBrowser.setText(f"{math.factorial(int(num1))}")# Выводит ответ на экран
        num1 = str(math.factorial(int(num1)))

    def ontvet(self): # При нажатии кнопки = вызывается эта функция
        global num1
        if "%" in num1: # если в веденных значениях есть символ процента
            num1 = str((int(num1[:num1.find("%")]) * float(num1[num1.find("%") + 1:])) / 100) # Выводит ответ на экран
            self.main_menu.textBrowser.setText(num1) # Выводит ответ на экран

        else: # иначе все действия простые и мы просто их выводим
            num1 = str(eval(num1))
            self.main_menu.textBrowser.setText(f"{eval(num1)}") # Выводит ответ на экран

    def clear(self): # очистить экран
        global num1
        self.main_menu.textBrowser.clear() # вызываем ффункцию очистки
        num1 = ""
    def button(self): # инициализируем кнопки
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
        self.main_menu.pushButton_17.clicked.connect(lambda: self.clear())
        self.main_menu.pushButton_18.clicked.connect(lambda: self.sin())
        self.main_menu.pushButton_19.clicked.connect(lambda: self.tan())
        self.main_menu.pushButton_20.clicked.connect(lambda: self.cor())
        self.main_menu.pushButton_21.clicked.connect(lambda: self.info("%"))
        self.main_menu.pushButton_22.clicked.connect(lambda: self.cos())
        self.main_menu.pushButton_23.clicked.connect(lambda: self.cat())
        self.main_menu.pushButton_24.clicked.connect(lambda: self.step3())
        self.main_menu.pushButton_25.clicked.connect(lambda: self.info("3.14"))
        self.main_menu.pushButton_26.clicked.connect(lambda: self.info("+"))
        self.main_menu.pushButton_27.clicked.connect(lambda: self.step2())
        self.main_menu.pushButton_28.clicked.connect(lambda: self.log())
        self.main_menu.pushButton_29.clicked.connect(lambda: self.fact())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()

