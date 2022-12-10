#!/usr/bin/python3
# -*- coding: UTF-8 -*-
""" Simple 4/5 rings resistance calculator """
import sys

from PyQt6.QtGui import QFont, QIcon, QFontDatabase, QPainter, QPen, QPixmap, QColor
from PyQt6.QtCore import QSize, Qt, QTimer
from PyQt6.QtWidgets import (QMessageBox, QWidget, QVBoxLayout,
                             QHBoxLayout, QGraphicsDropShadowEffect,
                             QGroupBox, QButtonGroup, QLabel,
                             QRadioButton, QFrame, QComboBox,
                             QApplication, QSplashScreen)

APP_NAME = "Cavalrez"
VERSION = "v1.02"
APP_TITLE = f"{APP_NAME} {VERSION}"
APP_ICON = "./images/logo.png"
FONT = QFont("Lato", 11)
CLOSE_WIN = Qt.WindowType.WindowCloseButtonHint
MIN_WIN = Qt.WindowType.WindowMinimizeButtonHint
MAX_WIN = Qt.WindowType.WindowMaximizeButtonHint
YES_BTN = QMessageBox.StandardButton.Yes
NO_BTN = QMessageBox.StandardButton.No
AN4_SIZE = QSize(596, 212)
AN5_SIZE = QSize(716, 212)
COLOR_LIST = ["Noir", "Marron", "Rouge", "Orange", "Jaune",
              "Vert", "Bleu", "Violet", "Gris", "Blanc"]
MULT_LIST = ["Noir", "Marron", "Rouge", "Orange", "Jaune", "Vert",
             "Bleu", "Violet", "Gris", "Blanc", "Or", "Argent"]
COLOR_VALUES = {"Noir": 0, "Marron": 1, "Rouge": 2, "Orange": 3, "Jaune": 4,
                "Vert": 5, "Bleu": 6, "Violet": 7, "Gris": 8, "Blanc": 9}
MULT_VALUES = {"Noir": 10e-1, "Marron": 10e0, "Rouge": 10e1, "Orange": 10e2,
               "Jaune": 10e3, "Vert": 10e4, "Bleu": 10e5, "Violet": 10e6,
               "Gris": 10e7, "Blanc": 10e8, "Or": 10e-2, "Argent": 10e-3}
COLORS_HEX = {"Noir": "#000000", "Marron": "#9c6500", "Rouge": "#ff0000",
              "Orange": "#ffa500", "Jaune": "#ffff00", "Vert": "#00b600",
              "Bleu": "#0000ff", "Violet": "#8a008a", "Gris": "#808080",
              "Blanc": "#ffffff", "Or": "#ffd700", "Argent": "#c0c0c0"}
TOL_LIST = ["Marron", "Rouge", "Vert", "Bleu",
            "Violet", "Gris", "Or", "Argent"]
TOL_VALUES = {"Marron": 1, "Rouge": 2, "Vert": 0.5, "Bleu": 0.25,
              "Violet": 0.1, "Gris": 0.05, "Or": 5, "Argent": 10}


class MainWindow(QWidget):
    """ Main WIndow """

    def __init__(self):
        super().__init__(flags=MIN_WIN | CLOSE_WIN)

        self.setWindowTitle(APP_TITLE)
        # self.setWindowFlags(MIN_WIN | MAX_WIN | CLOSE_WIN)
        self.setWindowIcon(QIcon(APP_ICON))
        self.setFixedSize(AN5_SIZE)
        self.setWindowOpacity(0.0)

        # Variables
        self.opacity = 0.0
        self.result = str()
        black_pix = QPixmap(100, 100)
        black_pix.fill(QColor("#000000"))
        self.black_icon = QIcon(black_pix)
        maroon_pix = QPixmap(100, 100)
        maroon_pix.fill(QColor("#9c6500"))
        self.maroon_icon = QIcon(maroon_pix)
        red_pix = QPixmap(100, 100)
        red_pix.fill(QColor("#ff0000"))
        self.red_icon = QIcon(red_pix)
        orange_pix = QPixmap(100, 100)
        orange_pix.fill(QColor("#ffa500"))
        self.orange_icon = QIcon(orange_pix)
        yellow_pix = QPixmap(100, 100)
        yellow_pix.fill(QColor("#ffff00"))
        self.yellow_icon = QIcon(yellow_pix)
        green_pix = QPixmap(100, 100)
        green_pix.fill(QColor("#00b600"))
        self.green_icon = QIcon(green_pix)
        blue_pix = QPixmap(100, 100)
        blue_pix.fill(QColor("#0000ff"))
        self.blue_icon = QIcon(blue_pix)
        purple_pix = QPixmap(100, 100)
        purple_pix.fill(QColor("#8a008a"))
        self.purple_icon = QIcon(purple_pix)
        gray_pix = QPixmap(100, 100)
        gray_pix.fill(QColor("#808080"))
        self.gray_icon = QIcon(gray_pix)
        white_pix = QPixmap(100, 100)
        white_pix.fill(QColor("#ffffff"))
        self.white_icon = QIcon(white_pix)
        gold_pix = QPixmap(100, 100)
        gold_pix.fill(QColor("#ffd700"))
        self.gold_icon = QIcon(gold_pix)
        silver_pix = QPixmap(100, 100)
        silver_pix.fill(QColor("#c0c0c0"))
        self.silver_icon = QIcon(silver_pix)

        self.main_layout = QVBoxLayout(self)

        self.input_layout = QHBoxLayout()
        self.output_layout = QHBoxLayout()
        self.output_group = QGroupBox()
        self.output_shadow = QGraphicsDropShadowEffect()
        self.output_shadow.setBlurRadius(100)
        self.output_group.setGraphicsEffect(self.output_shadow)
        self.output_group.setLayout(self.output_layout)

        # ############## Input Layout ################
        # Rings
        self.ring_group = QGroupBox()
        self.ring_shadow = QGraphicsDropShadowEffect()
        self.ring_shadow.setBlurRadius(100)
        self.ring_group.setGraphicsEffect(self.ring_shadow)
        self.ring_layout = QVBoxLayout()
        self.ring_btn_grp = QButtonGroup()
        self.ring_label = QLabel("Anneaux")
        self.four_ring_radio = QRadioButton("4")
        self.five_ring_radio = QRadioButton("5")
        self.five_ring_radio.setChecked(True)
        self.ring_btn_grp.addButton(self.four_ring_radio)
        self.ring_btn_grp.addButton(self.five_ring_radio)
        self.ring_layout.addWidget(self.ring_label, 1, Qt.AlignmentFlag.AlignCenter)
        self.ring_layout.addWidget(self.four_ring_radio, 1, Qt.AlignmentFlag.AlignCenter)
        self.ring_layout.addWidget(self.five_ring_radio, 1, Qt.AlignmentFlag.AlignCenter)
        self.ring_group.setLayout(self.ring_layout)
        # noinspection PyUnresolvedReferences
        self.five_ring_radio.clicked.connect(lambda: self.set_rings_number(5))
        # noinspection PyUnresolvedReferences
        self.four_ring_radio.clicked.connect(lambda: self.set_rings_number(4))

        # Colors
        self.color_group = QGroupBox()
        self.color_shadow = QGraphicsDropShadowEffect()
        self.color_shadow.setBlurRadius(100)
        self.color_group.setGraphicsEffect(self.color_shadow)
        self.color_layout = QHBoxLayout()
        self.color_layout.setSpacing(20)
        self.color_group.setLayout(self.color_layout)

        self.color_1_layout = QVBoxLayout()
        self.color_2_layout = QVBoxLayout()
        self.color_3_layout = QVBoxLayout()
        # noinspection PyArgumentList
        self.color_3_frame = QFrame()
        self.mult_layout = QVBoxLayout()
        self.tol_layout = QVBoxLayout()
        self.color_layout.addLayout(self.color_1_layout, 1)
        self.color_layout.addLayout(self.color_2_layout, 1)
        self.color_layout.addWidget(self.color_3_frame, 1, Qt.AlignmentFlag.AlignCenter)
        self.color_layout.addLayout(self.mult_layout, 1)
        self.color_layout.addLayout(self.tol_layout, 1)

        self.color_1_label_up = QLabel("Couleur 1")
        self.color_1_combo = QComboBox()
        self.color_1_combo.setMaxVisibleItems(20)
        self.color_1_combo.addItems([i for i in COLOR_LIST if i != "Noir"])
        self.color_1_combo.setEditable(True)
        self.color_1_combo.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.color_1_combo.lineEdit().setReadOnly(True)
        self.format_combobox(self.color_1_combo)
        self.color_1_combo.setCurrentText("Marron")
        self.color_1_combo.setCurrentIndex(0)
        self.color_1_combo.setFixedWidth(100)
        self.color_1_label_down = QLabel("1")
        self.color_1_layout.addWidget(self.color_1_label_up, 1, Qt.AlignmentFlag.AlignCenter)
        self.color_1_layout.addWidget(self.color_1_combo, 1, Qt.AlignmentFlag.AlignCenter)
        self.color_1_layout.addWidget(self.color_1_label_down, 1, Qt.AlignmentFlag.AlignCenter)

        self.color_2_label_up = QLabel("Couleur 2")
        self.color_2_combo = QComboBox()
        self.color_2_combo.setMaxVisibleItems(20)
        self.color_2_combo.addItems(COLOR_LIST)
        self.color_2_combo.setCurrentIndex(1)
        self.color_2_combo.setEditable(True)
        self.color_2_combo.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.color_2_combo.lineEdit().setReadOnly(True)
        self.format_combobox(self.color_2_combo)
        self.color_2_combo.setCurrentText("Marron")
        self.color_2_combo.setFixedWidth(100)
        self.color_2_label_down = QLabel("1")
        self.color_2_layout.addWidget(self.color_2_label_up, 1, Qt.AlignmentFlag.AlignCenter)
        self.color_2_layout.addWidget(self.color_2_combo, 1, Qt.AlignmentFlag.AlignCenter)
        self.color_2_layout.addWidget(self.color_2_label_down, 1, Qt.AlignmentFlag.AlignCenter)

        self.color_3_label_up = QLabel("Couleur 3")
        self.color_3_combo = QComboBox()
        self.color_3_combo.setMaxVisibleItems(20)
        self.color_3_combo.addItems(COLOR_LIST)
        self.color_3_combo.setCurrentIndex(1)
        self.color_3_combo.setEditable(True)
        self.color_3_combo.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.color_3_combo.lineEdit().setReadOnly(True)
        self.format_combobox(self.color_3_combo)
        self.color_3_combo.setCurrentText("Marron")
        self.color_3_combo.setFixedWidth(100)
        self.color_3_label_down = QLabel("1")
        self.color_3_layout.addWidget(self.color_3_label_up, 1, Qt.AlignmentFlag.AlignCenter)
        self.color_3_layout.addWidget(self.color_3_combo, 1, Qt.AlignmentFlag.AlignCenter)
        self.color_3_layout.addWidget(self.color_3_label_down, 1, Qt.AlignmentFlag.AlignCenter)
        self.color_3_frame.setLayout(self.color_3_layout)
        self.color_3_layout.setContentsMargins(0, 0, 0, 0)
        self.color_3_layout.setSpacing(20)

        self.mult_label_up = QLabel("Multiplicateur")
        self.mult_combo = QComboBox()
        self.mult_combo.setMaxVisibleItems(20)
        self.mult_combo.addItems(MULT_LIST)
        self.mult_combo.setCurrentIndex(0)
        self.mult_combo.setEditable(True)
        self.mult_combo.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mult_combo.lineEdit().setReadOnly(True)
        self.format_combobox(self.mult_combo)
        self.mult_combo.setCurrentText("Noir")
        self.mult_combo.setFixedWidth(100)
        self.mult_label_down = QLabel("1")
        self.mult_layout.addWidget(self.mult_label_up, 1, Qt.AlignmentFlag.AlignCenter)
        self.mult_layout.addWidget(self.mult_combo, 1, Qt.AlignmentFlag.AlignCenter)
        self.mult_layout.addWidget(self.mult_label_down, 1, Qt.AlignmentFlag.AlignCenter)

        self.tol_label_up = QLabel("Tolérence")
        self.tol_combo = QComboBox()
        self.tol_combo.setMaxVisibleItems(20)
        self.tol_combo.addItems(TOL_LIST)
        self.tol_combo.setCurrentIndex(0)
        self.tol_combo.setEditable(True)
        self.tol_combo.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tol_combo.lineEdit().setReadOnly(True)
        self.format_combobox(self.tol_combo)
        self.tol_combo.setCurrentText("Marron")
        self.tol_combo.setFixedWidth(100)
        self.tol_label_down = QLabel("1")
        self.tol_layout.addWidget(self.tol_label_up, 1, Qt.AlignmentFlag.AlignCenter)
        self.tol_layout.addWidget(self.tol_combo, 1, Qt.AlignmentFlag.AlignCenter)
        self.tol_layout.addWidget(self.tol_label_down, 1, Qt.AlignmentFlag.AlignCenter)

        # noinspection PyUnresolvedReferences
        self.color_1_combo.currentTextChanged.connect(lambda e: self.set_rings_color(1, e))
        # noinspection PyUnresolvedReferences
        self.color_2_combo.currentTextChanged.connect(lambda e: self.set_rings_color(2, e))
        # noinspection PyUnresolvedReferences
        self.color_3_combo.currentTextChanged.connect(lambda e: self.set_rings_color(3, e))
        # noinspection PyUnresolvedReferences
        self.mult_combo.currentTextChanged.connect(lambda e: self.set_rings_color(4, e))
        # noinspection PyUnresolvedReferences
        self.tol_combo.currentTextChanged.connect(lambda e: self.set_rings_color(5, e))

        self.input_layout.addWidget(self.ring_group, 1, Qt.AlignmentFlag.AlignJustify)
        self.input_layout.addWidget(self.color_group, 5, Qt.AlignmentFlag.AlignJustify)

        # ############## Output Layout ################
        # noinspection PyArgumentList
        self.res_frame = QFrame()
        self.res_frame.setFixedHeight(30)
        self.res_frame.setContentsMargins(10, 0, 10, 0)
        self.res_frame.setStyleSheet("background: qlineargradient(spread:pad, "
                                     "x1:0, y1:0, x2:1, y2:1, "
                                     "stop:0 rgba(214, 186, 147, 255), "
                                     "stop:1 rgba(182, 154, 115, 255));"
                                     "border: 0px solid black; "
                                     "border-radius: 5px")
        self.res_layout = QHBoxLayout()
        self.res_layout.setContentsMargins(0, 0, 0, 0)
        self.res_layout.setSpacing(15)
        self.res_frame.setLayout(self.res_layout)
        # noinspection PyArgumentList
        self.color_1_res_frame = QFrame()
        self.color_1_res_frame.setFixedSize(10, 30)
        # noinspection PyArgumentList
        self.color_2_res_frame = QFrame()
        self.color_2_res_frame.setFixedSize(10, 30)
        # noinspection PyArgumentList
        self.color_3_res_frame = QFrame()
        self.color_3_res_frame.setFixedSize(10, 30)
        # noinspection PyArgumentList
        self.mult_res_frame = QFrame()
        self.mult_res_frame.setFixedSize(10, 30)
        # noinspection PyArgumentList
        self.tol_res_frame = QFrame()
        self.tol_res_frame.setFixedSize(10, 30)
        self.color_1_res_frame.setStyleSheet(f"background-color: {COLORS_HEX['Marron']}; "
                                             f"border: 0px solid black; border-radius: 0px")
        self.color_2_res_frame.setStyleSheet(f"background-color: {COLORS_HEX['Marron']}; "
                                             f"border: 0px solid black; border-radius: 0px")
        self.color_3_res_frame.setStyleSheet(f"background-color: {COLORS_HEX['Marron']}; "
                                             f"border: 0px solid black; border-radius: 0px")
        self.mult_res_frame.setStyleSheet(f"background-color: {COLORS_HEX['Noir']}; "
                                          f"border: 0px solid black; border-radius: 0px")
        self.tol_res_frame.setStyleSheet(f"background-color: {COLORS_HEX['Marron']}; "
                                         f"border: 0px solid black; border-radius: 0px")
        self.res_layout.addWidget(self.color_1_res_frame, 1, Qt.AlignmentFlag.AlignCenter)
        self.res_layout.addWidget(self.color_2_res_frame, 1, Qt.AlignmentFlag.AlignCenter)
        self.res_layout.addWidget(self.color_3_res_frame, 1, Qt.AlignmentFlag.AlignCenter)
        self.res_layout.addWidget(self.mult_res_frame, 1, Qt.AlignmentFlag.AlignCenter)
        self.res_layout.addWidget(self.tol_res_frame, 1, Qt.AlignmentFlag.AlignCenter)

        self.result_label = QLabel("111 Ω - 1 %")
        label_font = self.result_label.font()
        label_font.setPointSize(25)
        self.result_label.setFont(label_font)

        self.output_layout.addWidget(self.res_frame, 1, Qt.AlignmentFlag.AlignCenter)
        self.output_layout.addWidget(self.result_label, 1, Qt.AlignmentFlag.AlignCenter)

        self.main_layout.addLayout(self.input_layout, 2)
        self.main_layout.addWidget(self.output_group, 1, Qt.AlignmentFlag.AlignBaseline)

        self.setLayout(self.main_layout)

        # Start Opacity Anim Timer
        self.start_anim_timer = QTimer(self)
        self.start_anim_timer.setInterval(5)
        # noinspection PyUnresolvedReferences
        self.start_anim_timer.timeout.connect(self.increase_opacity)

        self.four_ring_radio.setChecked(True)
        self.set_rings_number(4)

    def format_combobox(self, combobox):
        for i in range(0, combobox.count()):
            combobox.setItemData(i, Qt.AlignmentFlag.AlignCenter)
            if combobox.itemText(i) == "Noir":
                combobox.setItemIcon(i, self.black_icon)
            elif combobox.itemText(i) == "Marron":
                combobox.setItemIcon(i, self.maroon_icon)
            elif combobox.itemText(i) == "Rouge":
                combobox.setItemIcon(i, self.red_icon)
            elif combobox.itemText(i) == "Orange":
                combobox.setItemIcon(i, self.orange_icon)
            elif combobox.itemText(i) == "Jaune":
                combobox.setItemIcon(i, self.yellow_icon)
            elif combobox.itemText(i) == "Vert":
                combobox.setItemIcon(i, self.green_icon)
            elif combobox.itemText(i) == "Bleu":
                combobox.setItemIcon(i, self.blue_icon)
            elif combobox.itemText(i) == "Violet":
                combobox.setItemIcon(i, self.purple_icon)
            elif combobox.itemText(i) == "Gris":
                combobox.setItemIcon(i, self.gray_icon)
            elif combobox.itemText(i) == "Blanc":
                combobox.setItemIcon(i, self.white_icon)
            elif combobox.itemText(i) == "Or":
                combobox.setItemIcon(i, self.gold_icon)
            elif combobox.itemText(i) == "Argent":
                combobox.setItemIcon(i, self.silver_icon)

    def paintEvent(self, event):
        """ Draw line """
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.black, 2))
        painter.setOpacity(0.6)
        if self.five_ring_radio.isChecked():
            painter.drawLine(113, 173, 265, 173)
            painter.drawLine(265, 173, 275, 183)
            painter.drawLine(113, 173, 103, 183)
        elif self.four_ring_radio.isChecked():
            painter.drawLine(95, 173, 222, 173)
            painter.drawLine(95, 173, 85, 183)
            painter.drawLine(222, 173, 232, 183)

    def set_rings_color(self, ring_num, color):
        """ Set the color of the given ring index """
        if ring_num == 1:
            self.color_1_res_frame.setStyleSheet(f"background-color: {COLORS_HEX[color]}; "
                                                 f"border: 0px solid black; border-radius: 0px")
            self.color_1_label_down.setText(str(COLOR_VALUES[self.color_1_combo.currentText()]))
        elif ring_num == 2:
            self.color_2_res_frame.setStyleSheet(f"background-color: {COLORS_HEX[color]}; "
                                                 f"border: 0px solid black; border-radius: 0px")
            self.color_2_label_down.setText(str(COLOR_VALUES[self.color_2_combo.currentText()]))
        elif ring_num == 3:
            self.color_3_res_frame.setStyleSheet(f"background-color: {COLORS_HEX[color]}; "
                                                 f"border: 0px solid black; border-radius: 0px")
            self.color_3_label_down.setText(str(COLOR_VALUES[self.color_3_combo.currentText()]))
        elif ring_num == 4:
            self.mult_res_frame.setStyleSheet(f"background-color: {COLORS_HEX[color]}; "
                                              f"border: 0px solid black; border-radius: 0px")
            self.mult_label_down.setText(str(MULT_VALUES[self.mult_combo.currentText()]))
        elif ring_num == 5:
            self.tol_res_frame.setStyleSheet(f"background-color: {COLORS_HEX[color]}; "
                                             f"border: 0px solid black; border-radius: 0px")
            self.tol_label_down.setText(str(TOL_VALUES[self.tol_combo.currentText()]))

        self.display_result()

    def set_rings_number(self, num):
        """ Set the number or rings """
        if num == 4:
            self.color_3_frame.hide()
            self.color_3_res_frame.hide()
            self.setFixedSize(AN4_SIZE)
        elif num == 5:
            self.color_3_frame.show()
            self.color_3_res_frame.show()
            self.setFixedSize(AN5_SIZE)

        self.display_result()

    def display_result(self):
        """
        Méthode appelée pour afficher les résultats en
        fonction des options choisies
        """
        if self.four_ring_radio.isChecked():
            self.result = float(str(COLOR_VALUES[self.color_1_combo.currentText()]) +
                                str(COLOR_VALUES[self.color_2_combo.currentText()])) * \
                          MULT_VALUES[self.mult_combo.currentText()]

        elif self.five_ring_radio.isChecked():
            self.result = float(str(COLOR_VALUES[self.color_1_combo.currentText()]) +
                                str(COLOR_VALUES[self.color_2_combo.currentText()]) +
                                str(COLOR_VALUES[self.color_3_combo.currentText()])) * \
                          MULT_VALUES[self.mult_combo.currentText()]

        if 0 < self.result <= 999:
            unit = " Ω - "
        elif 10e2 <= self.result <= 10e5 - 1:
            unit = " kΩ - "
            self.result = self.result / 10e2
        elif 10e5 <= self.result <= 10e8 - 1:
            unit = " MΩ - "
            self.result = self.result / 10e5
        else:
            unit = " GΩ - "
            self.result = self.result / 10e8

        self.result_label.setText(str(round(self.result, 3)) + unit +
                                  str(TOL_VALUES[self.tol_combo.currentText()]) + " %")

    def increase_opacity(self):
        """ Increase opacity """
        if self.opacity >= 1.00:
            self.opacity = 1.00
            self.start_anim_timer.stop()
        else:
            self.opacity += 0.01

        self.setWindowOpacity(self.opacity)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont("./font/Lato-Regular.ttf")
    app.setFont(FONT)
    splash_screen = QSplashScreen(QPixmap(APP_ICON))
    splash_screen.show()
    window = MainWindow()
    splash_screen.finish(window)
    window.show()
    window.start_anim_timer.start()
    app.exec()
