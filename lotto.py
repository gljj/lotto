from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import random


class LottoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.label1 = QLabel("게임 수: ", self)
        self.label1.resize(100, 25)

        self.combobox1 = QComboBox(self)
        self.combobox1.resize(50, 25)
        self.number_lists = [str(i+1) for i in range(10)]
        self.combobox1.addItems(self.number_lists)

        self.button1 = QPushButton("시작")
        self.button1.resize(50, 25)
        self.button1.clicked.connect(self.play_lotto)

        self.button2 = QPushButton("초기화")
        self.button2.resize(50, 25)

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.label1)
        self.hbox.addWidget(self.combobox1)
        self.hbox.addWidget(self.button1)
        # self.hbox.addWidget(self.button2)

        self.qtable = QTableWidget(self)
        self.qtable.resize(400, 800)
        self.col_name = [str(i+1) for i in range(6)]
        self.qtable.setColumnCount(len(self.col_name))
        self.qtable.setRowCount(len(self.number_lists))

        for i in range(len(self.col_name)):
            self.qtable.setColumnWidth(i, 66)
        for i in range(len(self.number_lists)):
            self.qtable.setRowHeight(i, 70)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.qtable)

        self.mainbox = QVBoxLayout()
        self.mainbox.addLayout(self.hbox)
        self.mainbox.addLayout(self.vbox)

        self.setLayout(self.mainbox)
        self.setGeometry(100, 100, 500, 900)
        self.setWindowTitle("777 Lotto!!")

    def play_lotto(self):
        self.qtable.clearContents()
        tries = int(self.combobox1.currentText())
        for i in range(tries):
            final_numbers = self.get_number()
            final_numbers.sort()
            self.set_number(i, final_numbers)

    def get_number(self):
        numbers = []
        while len(numbers) < 6:
            number = random.randint(1, 45)
            if number not in numbers:
                numbers.append(number)
        return numbers

    def set_number(self, tries, winning_numbers):
        for i, v in enumerate(winning_numbers):
            item = QTableWidgetItem(str(v))
            item.setTextAlignment(Qt.AlignCenter)
            self.qtable.setItem(tries, i, item)
            if int(v) <= 10:
                self.qtable.item(tries, i).setBackground(QColor(255, 255, 204))
            elif int(v) <= 20:
                self.qtable.item(tries, i).setBackground(QColor(204, 229, 255))
            elif int(v) <= 30:
                self.qtable.item(tries, i).setBackground(QColor(255, 204, 204))
            elif int(v) <= 40:
                self.qtable.item(tries, i).setBackground(QColor(224, 224, 224))
            else:
                self.qtable.item(tries, i).setBackground(QColor(204, 255, 204))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LottoWindow()
    win.show()
    app.exec()
