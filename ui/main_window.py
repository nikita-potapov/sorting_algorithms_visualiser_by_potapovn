from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from sources.algorithms import *
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(657, 455)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.access_to_list_count = QtWidgets.QLineEdit(self.centralwidget)
        self.access_to_list_count.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.access_to_list_count.setReadOnly(True)
        self.access_to_list_count.setObjectName("access_to_list_count")
        self.horizontalLayout.addWidget(self.access_to_list_count)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comparsions_count = QtWidgets.QLineEdit(self.centralwidget)
        self.comparsions_count.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.comparsions_count.setReadOnly(True)
        self.comparsions_count.setObjectName("comparsions_count")
        self.horizontalLayout_2.addWidget(self.comparsions_count)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_4.addWidget(self.line)
        self.btn_info_about_algorithm = QtWidgets.QPushButton(self.centralwidget)
        self.btn_info_about_algorithm.setObjectName("btn_info_about_algorithm")
        self.horizontalLayout_4.addWidget(self.btn_info_about_algorithm)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.canvas_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas_label.sizePolicy().hasHeightForWidth())
        self.canvas_label.setSizePolicy(sizePolicy)
        self.canvas_label.setObjectName("canvas_label")
        self.verticalLayout.addWidget(self.canvas_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setObjectName("btn_reset")
        self.horizontalLayout_3.addWidget(self.btn_reset)
        self.enter_bars_count = QtWidgets.QSpinBox(self.centralwidget)
        self.enter_bars_count.setMinimumSize(QtCore.QSize(60, 0))
        self.enter_bars_count.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.enter_bars_count.setObjectName("enter_bars_count")
        self.horizontalLayout_3.addWidget(self.enter_bars_count)
        self.selecter_sorting_algorithm = QtWidgets.QComboBox(self.centralwidget)
        self.selecter_sorting_algorithm.setObjectName("selecter_sorting_algorithm")
        self.horizontalLayout_3.addWidget(self.selecter_sorting_algorithm)
        self.slider_delay = QtWidgets.QSlider(self.centralwidget)
        self.slider_delay.setMaximum(100)
        self.slider_delay.setOrientation(QtCore.Qt.Horizontal)
        self.slider_delay.setObjectName("slider_delay")
        self.horizontalLayout_3.addWidget(self.slider_delay)
        self.btn_play_pause = QtWidgets.QPushButton(self.centralwidget)
        self.btn_play_pause.setObjectName("btn_play_pause")
        self.horizontalLayout_3.addWidget(self.btn_play_pause)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 657, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_shuffle_list = QtWidgets.QAction(MainWindow)
        self.action_shuffle_list.setObjectName("action_shuffle_list")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu.addAction(self.action_exit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Алгоритмы сортировки"))
        self.label.setText(_translate("MainWindow", "Доступов к массиву:"))
        self.label_2.setText(_translate("MainWindow", "Сравнений:"))
        self.btn_info_about_algorithm.setText(_translate("MainWindow", "Справка"))
        self.canvas_label.setText(_translate("MainWindow", "TextLabel"))
        self.btn_reset.setText(_translate("MainWindow", "Сброс"))
        self.btn_play_pause.setText(_translate("MainWindow", "Старт"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.action_exit.setText(_translate("MainWindow", "Выход"))
        self.action_shuffle_list.setText(_translate("MainWindow", "Перемешать массив"))
        self.action_2.setText(_translate("MainWindow", "Перемешать массив"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

    def paint(self):
        self.do_paint = True

        self.number_of_lines = QInputDialog.getInt(self, 'Введите количество цветов',
                                                   'Сколько цветов изволите-с?', 3, 1, 10, 1)[0]
        self.wg = self.width() / 2
        self.hg = max(10, (self.width() - self.btn.height()) / 10)

        if self.width() - self.btn.width() - 10 < self.hg * self.number_of_lines:
            self.resize(self.width(), int(self.hg * self.number_of_lines + self.btn.height() + 20))

        self.repaint()
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint and self.number_of_lines:
            qp = QPainter()

            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        start_point = (int(self.width() / 2 - self.wg / 2), int(self.btn.height() + 10))
        for i in range(self.number_of_lines):
            qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
            qp.drawRect(int(start_point[0]), int(start_point[1]), int(self.wg), int(self.hg))
            start_point = (start_point[0], start_point[1] + int(self.hg))

        self.number_of_lines = None
        self.do_paint = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
