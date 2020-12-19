from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import random
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QTimer
from sources.algorithms import *
import sys

SORTING_FUNCTIONS = {
    'пузырьком': bubble_sort,
    'перемешиванием': shake_sort,
    'расческой': comb_sort,
    'вставками': insert_sort,
    'сортировка Шелла': shell_sort,
    'деревом': binary_insertion_sort,
    'выбором': selection_sort,
    'пирамидальная': heap_sort,
    'быстрая': quick_sort,
    'слиянием': merge_sort,
    'подсчетом': counting_sort,
    'гномья': gnome_sort
}

PLAYING = 2
PAUSE = 3
END = 4
WAIT = 5
ERROR = 6

DELAY = 70
MIN_BAR_WIDTH = 2


class LoggedList(list):
    def __init__(self, *args, **kwargs):
        super(LoggedList, self).__init__(*args, **kwargs)
        self.get_item_count = 0

    def __getitem__(self, item):
        self.get_item_count += 1
        return super(LoggedList, self).__getitem__(item)

    def get_accesses(self):
        return self.get_item_count


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
        self.spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.spacerItem)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Minimum)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setSizePolicy(sizePolicy)
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
        # self.label_2 = QtWidgets.QLabel(self.centralwidget)
        # self.label_2.setObjectName("label_2")
        # self.horizontalLayout_2.addWidget(self.label_2)
        # self.comparsions_count = QtWidgets.QLineEdit(self.centralwidget)
        # self.comparsions_count.setAlignment(
        #     QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        # self.comparsions_count.setReadOnly(True)
        # self.comparsions_count.setObjectName("comparsions_count")
        # self.horizontalLayout_2.addWidget(self.comparsions_count)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName('horizontalLayout_5')

        self.canvas_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas_label.sizePolicy().hasHeightForWidth())
        self.canvas_label.setSizePolicy(sizePolicy)
        self.canvas_label.setObjectName("canvas_label")

        self.horizontalLayout_5.addWidget(self.canvas_label)

        self.slider_delay = QtWidgets.QSlider(self.centralwidget)
        self.slider_delay.setMaximum(100)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Expanding)
        self.slider_delay.setSizePolicy(sizePolicy)

        self.slider_delay.setOrientation(QtCore.Qt.Vertical)
        self.slider_delay.setObjectName("slider_delay")

        self.horizontalLayout_5.addWidget(self.slider_delay)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setObjectName("btn_reset")
        self.horizontalLayout_3.addWidget(self.btn_reset)
        self.enter_bars_count = QtWidgets.QLineEdit(self.centralwidget)
        self.enter_bars_count.setMinimumSize(QtCore.QSize(60, 0))
        self.enter_bars_count.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.enter_bars_count.setObjectName("enter_bars_count")
        self.horizontalLayout_3.addWidget(self.enter_bars_count)
        self.selecter_sorting_algorithm = QtWidgets.QComboBox(self.centralwidget)
        self.selecter_sorting_algorithm.setObjectName("selecter_sorting_algorithm")
        self.horizontalLayout_3.addWidget(self.selecter_sorting_algorithm)
        self.slider_steps = QtWidgets.QSlider(self.centralwidget)
        self.slider_steps.setMaximum(100)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Preferred)
        self.slider_steps.setSizePolicy(sizePolicy)

        self.slider_steps.setOrientation(QtCore.Qt.Horizontal)
        self.slider_steps.setObjectName("slider_steps")
        self.horizontalLayout_3.addWidget(self.slider_steps)
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
        # self.label_2.setText(_translate("MainWindow", "Сравнений:"))
        self.canvas_label.setText(_translate("MainWindow", ""))
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

        self.selecter_sorting_algorithm.addItems(SORTING_FUNCTIONS)

        self.btn_play_pause.clicked.connect(self.btn_play_pause_clicked)
        self.btn_reset.clicked.connect(self.btn_reset_clicked)
        self.action_2.triggered.connect(self.initialize_array)
        self.action_exit.triggered.connect(sys.exit)


        self.selecter_sorting_algorithm.currentIndexChanged.connect(self.change_sorting_algorithm)

        self.array_size = 20
        self.enter_bars_count.setText('20')
        self.enter_bars_count.textChanged.connect(self.change_array_size)

        self.delay = DELAY

        self.timer = QTimer(self)
        self.timer.start(self.delay)
        self.timer.timeout.connect(self.timer_tick)

        self.enter_bars_count.setMaximumWidth(70)

        self.slider_steps.setMinimum(0)
        self.slider_steps.valueChanged.connect(self.paint)

        self.slider_delay.setMaximum(100)
        self.slider_delay.setMinimum(0)
        self.slider_delay.setValue(50)
        self.slider_delay.setInvertedAppearance(True)
        self.slider_delay.valueChanged.connect(self.delay_slider_changed)

        self.state = WAIT

        self.history_of_sorting = []

        self.array = None
        self.change_array_size()
        self.initialize_array()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        self.draw_bars(qp)

        qp.end()

    def paint(self):
        self.repaint()

    def btn_play_pause_clicked(self):
        if self.btn_play_pause.text() == 'Старт':
            if self.slider_steps.value() == self.slider_steps.maximum():
                self.slider_steps.setValue(self.slider_steps.minimum())
            self.btn_play_pause.setText('Пауза')
            self.selecter_sorting_algorithm.setDisabled(True)
            self.enter_bars_count.setDisabled(True)
            self.state = PLAYING
        else:
            self.btn_play_pause.setText('Старт')
            self.selecter_sorting_algorithm.setDisabled(False)
            self.enter_bars_count.setDisabled(False)
            self.state = PAUSE

    def btn_reset_clicked(self):
        self.state = WAIT
        self.change_sorting_algorithm()
        self.slider_steps.setValue(0)
        self.enable_interface()
        self.btn_play_pause.setText('Старт')

    def change_array_size(self):
        self.array_size = str(self.enter_bars_count.text())
        if self.array_size.isdigit():
            self.array_size = int(self.array_size)
            if 1 < self.array_size:
                if self.array_size > self.get_bars_max_count():
                    self.enter_bars_count.setText(str(self.get_bars_max_count()))
                self.state = WAIT
                self.btn_play_pause.setDisabled(False)
                self.enter_bars_count.setStyleSheet('background-color: white;')

                self.initialize_array()
                self.change_sorting_algorithm()
                width = self.canvas_label.width()
                ost = width % len(self.array)
                self.resize(self.width() - ost, self.height())
                return
        self.state = ERROR
        self.btn_play_pause.setDisabled(True)
        self.enter_bars_count.setStyleSheet('background-color: #ff5858;'
                                            'color: white;')

    def initialize_array(self):
        """Создает массив из заданного пользователем количества элементов"""
        self.array = list(range(1, self.array_size + 1))
        random.shuffle(self.array)

        self.change_sorting_algorithm()
        self.paint()

    def get_bars_max_count(self):
        """Возвращает максимальное количество столбиков на экране"""
        return (self.width() - 20) // MIN_BAR_WIDTH

    def draw_bars(self, qp):
        step = self.slider_steps.value()
        s_x, s_y = self.btn_reset.x(), self.btn_reset.y() + 10
        width, height = self.canvas_label.width(), self.canvas_label.height()
        if self.history_of_sorting:
            array, first_red, second_red, first_blue, second_blue, \
                accesses = self.history_of_sorting[step]
            self.access_to_list_count.setText(str(accesses))
        else:
            array = self.array
            first_red, second_red, first_blue, second_blue = -1, -1, -1, -1
        bar_width = width // len(array)

        for i in range(len(array)):
            color = QColor(144, 144, 144)

            if i in [first_red, second_red]:
                color = QColor(255, 0, 0)
            elif i in [first_blue, second_blue]:
                color = QColor(0, 0, 255)

            qp.setBrush(color)
            qp.drawRect(s_x + i * bar_width, s_y, bar_width,
                        int(-array[i] * (self.canvas_label.height() / self.array_size)))

    def timer_tick(self):
        """Сработка таймера"""
        if self.state == PLAYING:
            self.slider_steps.setValue(self.slider_steps.value() + 1)
            if self.slider_steps.value() == self.slider_steps.maximum():
                self.end_of_sorting()

    def sorting_history(self, array, first_red, second_red, first_blue, second_blue):
        """Добавляет в список текущее состояние сортируемого массива и подсвечиваемые элементы"""
        self.history_of_sorting.append((array[:], first_red, second_red, first_blue, second_blue,
                                        array.get_accesses()))

    def change_sorting_algorithm(self):
        try:
            self.current_sorting_algorithm = SORTING_FUNCTIONS[
                self.selecter_sorting_algorithm.currentText()]
            self.history_of_sorting.clear()
            self.history_of_sorting.append((self.array, -1, -1, -1, -1, 0))
            self.current_sorting_algorithm(LoggedList(self.array[:]), self.sorting_history, 0,
                                           len(self.array) - 1)
            self.slider_steps.setMaximum(len(self.history_of_sorting) - 1)
            self.history_of_sorting.append((list(range(1, len(self.array))), -1, -1, -1, -1))
            self.slider_steps.setValue(0)

        except Exception as e:
            print(e)

    def end_of_sorting(self):
        self.state = WAIT
        self.btn_play_pause.setText('Старт')
        self.enable_interface()

    def enable_interface(self):
        """Включает интерфейс"""
        self.enter_bars_count.setDisabled(False)
        self.selecter_sorting_algorithm.setDisabled(False)

    def disable_interface(self):
        """Отключает интерфейс"""
        self.enter_bars_count.setDisabled(True)
        self.selecter_sorting_algorithm.setDisabled(True)

    def delay_slider_changed(self):
        self.delay = self.slider_delay.value()
        self.timer.start(self.delay)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
