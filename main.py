from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QTimer
import random
import sys


def bubble_sort(array, sorting_history, *args):
    # Сортировка пузырьком
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            sorting_history(array, j, j + 1, -1, -1)
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    sorting_history(array, -1, -1, -1, -1)
    return array


def shake_sort(array, sorting_history, *args):
    n = len(array)
    left = 0
    right = n - 1
    while left <= right:
        for i in range(left, right):
            sorting_history(array, i, i + 1, -1, -1)
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        right -= 1
        for i in range(right, left, -1):
            sorting_history(array, -1, -1, i, i + 1)
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
        left += 1
    sorting_history(array, -1, -1, -1, -1)
    return array


def comb_sort(array, sorting_history, *args):
    def get_next_gap(previous_gap):
        next_gap = int(previous_gap / 1.247)
        return next_gap if next_gap > 1 else 1

    n = len(array)
    gap = n
    swapped = True

    while gap != 1 or swapped:
        gap = get_next_gap(gap)
        swapped = False

        for i in range(n - gap):
            sorting_history(array, i, i + gap, -1, -1)
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                swapped = True
    sorting_history(array, -1, -1, -1, -1)
    return array


def gnome_sort(array, sorting_history, *args):
    n = len(array)
    i = 0
    while i < n:
        if array[i - 1] <= array[i] or i == 0:
            sorting_history(array, i, i - 1, -1, -1)
            i += 1
        else:
            sorting_history(array, i, i - 1, -1, -1)
            array[i - 1], array[i] = array[i], array[i - 1]
            i -= 1
    sorting_history(array, -1, -1, -1, -1)
    return array


def quick_sort(array, sorting_history, left, right, *args):
    if left >= right:
        sorting_history(array, -1, -1, -1, -1)
        return array
    i = left
    for j in range(left, right):
        sorting_history(array, j, right, i, -1)
        if array[j] < array[right]:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[i], array[right] = array[right], array[i]
    quick_sort(array, sorting_history, i + 1, right)
    quick_sort(array, sorting_history, left, i - 1)


SORTING_FUNCTIONS = {
    'пузырьком': bubble_sort,
    'шейкерная': shake_sort,
    'расческой': comb_sort,
    'гномья': gnome_sort,
    'быстрая': quick_sort,
}

PLAYING = 2
PAUSE = 3
END = 4
WAIT = 5
ERROR = 6

DELAY = 70
MIN_BAR_WIDTH = 2


class LoggedList(list):
    """Класс логированного списка, который запоминает общее
     кол-во обращений к его элементам о индексу"""

    def __init__(self, *args, **kwargs):
        super(LoggedList, self).__init__(*args, **kwargs)
        self.get_item_count = 0

    def __getitem__(self, item):
        self.get_item_count += 1
        return super(LoggedList, self).__getitem__(item)

    def get_accesses(self):
        """Получить количество обращений  к списку"""
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
        """Нажатие кнопки паузы, проигрывания"""
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
        """Нажатие кнопки сброса"""
        self.state = WAIT
        self.change_sorting_algorithm()
        self.slider_steps.setValue(0)
        self.enable_interface()
        self.btn_play_pause.setText('Старт')

    def change_array_size(self):
        """Срабатывает при смене кол-ва элементов"""
        self.array_size = str(self.enter_bars_count.text())
        if self.array_size.isdigit():
            try:
                self.array_size = int(self.array_size)
            except Exception:
                self.array_size = 2
                self.enter_bars_count.setText('2')
            if self.array_size < 2:
                self.array_size = 2
                self.enter_bars_count.setText('2')
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
        """Рисуем столбики"""
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
        bar_width = width // max(len(array), 2)

        for i in range(len(array)):
            color = QColor(144, 144, 144)

            if i in [first_red, second_red]:
                color = QColor(255, 0, 0)
            elif i in [first_blue, second_blue]:
                color = QColor(0, 0, 255)

            qp.setBrush(color)
            qp.drawRect(s_x + i * bar_width, s_y, bar_width,
                        int(-array[i] * (self.canvas_label.height() / max(len(self.array), 2))))

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
        """Срабатывает при смене сортирующего алгоритма"""
        self.current_sorting_algorithm = SORTING_FUNCTIONS[
            self.selecter_sorting_algorithm.currentText()]
        self.history_of_sorting.clear()
        self.history_of_sorting.append((self.array, -1, -1, -1, -1, 0))
        self.current_sorting_algorithm(LoggedList(self.array[:]), self.sorting_history, 0,
                                       len(self.array) - 1)
        self.slider_steps.setMaximum(len(self.history_of_sorting) - 1)
        self.history_of_sorting.append((list(range(1, len(self.array))), -1, -1, -1, -1))
        self.slider_steps.setValue(0)

    def end_of_sorting(self):
        """Конец сортировки"""
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
        """Изменяем задержку при передвижении полунка"""
        self.delay = self.slider_delay.value()
        self.timer.start(self.delay)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
