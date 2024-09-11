import os
import random as rd
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtCore
from form1 import Ui_Form


class Main:
    def __init__(self):
        self.imported_list = []
        self.list_before = []
        self.list_after = []
        self.lucky_guy = None

    def initialize(self):
        # 初始化运行
        file_name = 'list.txt'

        if not os.path.exists(file_name):
            # 如果文件不存在，创建一个
            with open(file_name, 'w'):
                pass
        else:
            # 如果文件存在，读取每行内容，并存入一个列表中
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    self.imported_list.append(line.strip())

        # 将imported_list的副本给list_before，保证两者内存地址不同
        self.list_before = self.imported_list[:]

        return self.list_before, self.imported_list

    def wow_lucky_guy(self):
        # 抽取函数

        # 如果list.txt为空,填入'抽取列表为空！'
        if not self.imported_list:
            self.imported_list.append('抽取列表为空！')

        # 如果列表为空，重置列表
        if not self.list_before:
            self.list_before = self.imported_list[:]

        # 随机抽取，抽过的从当前列表中去除，并堆入另一列表
        self.lucky_guy = rd.choice(self.list_before)
        self.list_before.remove(self.lucky_guy)
        self.list_after.append(self.lucky_guy)

        return self.lucky_guy

    def history(self):
        # 历史记录
        history_name = 'history.txt'

        # a模式打开history.txt，没有就创建
        with open(history_name, 'a') as file:
            for guy in reversed(self.list_after):
                file.write(guy + '\n')

        # 用记事本打开
        os.startfile(history_name)

    def edit(self):
        # 编辑列表
        list_name = 'list.txt'

        # 检测文件是否存在
        if not os.path.exists(list_name):
            # 如果文件不存在，创建一个
            with open(list_name, 'w'):
                pass

        # 用记事本打开
        os.startfile(list_name)

    def refresh(self):
        # 刷新历史记录和抽取列表
        self.list_after = []
        self.imported_list = []
        list_name = 'list.txt'
        history_name = 'history.txt'

        with open(list_name, 'r', encoding='utf-8') as file:
            for line in file:
                self.imported_list.append(line.strip())

        with open(history_name, 'w', encoding='utf-8'):
            pass

        self.list_before = self.imported_list[:]

        return self.imported_list, self.list_before, self.list_after


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 创建ui类并设置ui
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # 创建main类并初始化
        self.main = Main()
        self.main.initialize()
        # 绑定按钮
        self.ui.pushButton.clicked.connect(self.main.edit)
        self.ui.pushButton_2.clicked.connect(self.main.history)
        self.ui.pushButton_3.clicked.connect(self.packed)
        self.ui.pushButton_4.clicked.connect(self.main.refresh)

    def packed(self):
        # 随机选取，更改label并刷新ui
        self.main.wow_lucky_guy()
        self.ui.name = self.main.lucky_guy
        _translate = QtCore.QCoreApplication.translate
        self.ui.label.setText(_translate(f"{self}",
                                         f"<html><head/><body><p align=\"center\"><span style=\" font-size:72"
                                         f"pt;\">{self.ui.name}<br/></span></p></body></html>"))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
