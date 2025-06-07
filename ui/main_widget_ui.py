# -*- coding: utf-8 -*-

##########################################################################
# Form generated from reading UI file 'untitled.ui'
##
# Created by: Qt User Interface Compiler version 6.9.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
##########################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    QTime,
)
from PySide6.QtGui import (
    QFont,
)
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QTimeEdit,
    QPushButton,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 800)
        MainWindow.setStyleSheet(
            "\n"
            "       QWidget {\n"
            "           background-color: #000;\n"
            "           color: white;\n"
            "           font-family: Arial;\n"
            "       }\n"
            "       QLabel {\n"
            "           font-size: 12pt;\n"
            "           font-weight: bold;\n"
            "           border-radius: 6px;\n"
            "       }\n"
            "       QPushButton {\n"
            "           background-color: #222;\n"
            "           border: 1px solid #666;\n"
            "           padding: 8px;\n"
            "           font-size: 12pt;\n"
            "           border-radius: 8px;\n"
            "       }\n"
            "       QPushButton:hover {\n"
            "           background-color: #333;\n"
            "       }\n"
            "       QPushButton#btnStop {\n"
            "           background-color: white;\n"
            "           color: black;\n"
            "           font-size: 16pt;\n"
            "           font-weight: bold;\n"
            "           border: none;\n"
            "           border-radius: 20px;\n"
            "       }\n"
            "       QDial {\n"
            "           background-color: #222;\n"
            "       }\n"
            "       QFrame#tempBar {\n"
            "           background-color: orange;\n"
            "           min-height: 10px;\n"
            "           max-height: 10px;\n"
            "  "
            "     }\n"
            "   "
        )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget3 = QWidget(self.centralwidget)
        self.widget3.setObjectName("widget3")
        self.widget3.setGeometry(QRect(253, 120, 151, 40))
        self.widget3.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(0, 0, 0);"
        )
        self.label_10 = QLabel(self.widget3)
        self.label_10.setObjectName("label_10")
        self.label_10.setGeometry(QRect(30, -20, 41, 71))
        self.label_10.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);\n"
            "\n"
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-color: rgba(255, 255, 255, 0);"
        )
        self.temp_2 = QLabel(self.widget3)
        self.temp_2.setObjectName("temp_2")
        self.temp_2.setGeometry(QRect(50, 0, 71, 41))
        self.temp_2.setStyleSheet("border-color: rgba(255, 255, 255, 0);")
        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName("widget2")
        self.widget2.setEnabled(True)
        self.widget2.setGeometry(QRect(0, 120, 251, 40))
        self.widget2.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(0, 0, 0);"
        )
        self.label_1_3 = QLabel(self.widget2)
        self.label_1_3.setObjectName("label_1_3")
        self.label_1_3.setGeometry(QRect(50, -30, 71, 91))
        self.label_1_3.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);\n"
            "\n"
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-color: rgba(255, 255, 255, 0);"
        )
        self.time_2 = QTimeEdit(self.widget2)
        self.time_2.setDisplayFormat("h:mm:ss")
        self.time_2.setObjectName("time_2")
        self.time_2.setGeometry(QRect(80, 0, 121, 41))
        self.time_2.setStyleSheet("border-color: rgba(255, 255, 255, 0);\n" "")
        self.check_wifi = QLabel(self.centralwidget)
        self.check_wifi.setObjectName("check_wifi")
        self.check_wifi.setGeometry(QRect(410, 0, 47, 51))
        self.check_wifi.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);\n"
            "color: rgb(255, 255, 255);\n"
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-color: rgba(255, 255, 255, 0);"
        )
        self.check_blutooth = QLabel(self.centralwidget)
        self.check_blutooth.setObjectName("check_blutooth")
        self.check_blutooth.setGeometry(QRect(440, 0, 47, 51))
        self.check_blutooth.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);\n"
            "color: rgb(255, 255, 255);\n"
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-color: rgba(255, 255, 255, 0);"
        )
        self.labelGrillTemp = QLabel(self.centralwidget)
        self.labelGrillTemp.setObjectName("labelGrillTemp")
        self.labelGrillTemp.setGeometry(QRect(20, 100, 203, 13))
        font = QFont()
        font.setFamilies(["MS Shell Dlg 2"])
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        self.labelGrillTemp.setFont(font)
        self.labelGrillTemp.setStyleSheet(
            'font: 8pt "MS Shell Dlg 2";\n'
            "color: rgb(255, 255, 255);\n"
            "background-color: rgba(255, 255, 255, 0);\n"
            "qproperty-alignment: 'AlignCenter';\n"
            "border-color: rgba(255, 255, 255, 0);\n"
            ""
        )
        self.labelTimer = QLabel(self.centralwidget)
        self.labelTimer.setObjectName("labelTimer")
        self.labelTimer.setEnabled(True)
        self.labelTimer.setGeometry(QRect(250, 100, 203, 13))
        self.labelTimer.setFont(font)
        self.labelTimer.setStyleSheet(
            'font: 8pt "MS Shell Dlg 2";\n'
            "background-color: rgba(255, 255, 255, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "qproperty-alignment: 'AlignCenter';\n"
            "border-color: rgba(255, 255, 255, 0);"
        )
        self.label_1_1 = QLabel(self.centralwidget)
        self.label_1_1.setObjectName("label_1_1")
        self.label_1_1.setGeometry(QRect(410, 120, 71, 41))
        self.label_1_1.setStyleSheet(
            "background-color: rgb(249, 249, 249);\n"
            "color: rgb(0, 0, 0);\n"
            "\n"
            "border-color: rgba(255, 255, 255, 0);\n"
            'font: 10pt "MS Shell Dlg 2";'
        )
        self.widget4 = QWidget(self.centralwidget)
        self.widget4.setObjectName("widget4")
        self.widget4.setGeometry(QRect(0, 240, 161, 82))
        self.widget4.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(0, 0, 0);"
        )
        self.label_11 = QLabel(self.widget4)
        self.label_11.setObjectName("label_11")
        self.label_11.setGeometry(QRect(0, -10, 81, 61))
        self.label_11.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);\n"
            "\n"
            'font: 28pt "MS Shell Dlg 2";\n'
            "border-color: rgba(255, 255, 255, 0);"
        )
        self.temp1 = QLabel(self.widget4)
        self.temp1.setObjectName("temp1")
        self.temp1.setGeometry(QRect(50, 10, 81, 41))
        self.temp1.setStyleSheet(
            "background-color: rgba(248, 248, 248, 0);\n"
            'font: 75 16pt "MS Shell Dlg 2";\n'
            "border-color: rgba(255, 255, 255, 0);\n"
            ""
        )
        self.line = QFrame(self.widget4)
        self.line.setObjectName("line")
        self.line.setGeometry(QRect(10, 50, 118, 3))
        self.line.setStyleSheet("")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_13 = QLabel(self.widget4)
        self.label_13.setObjectName("label_13")
        self.label_13.setGeometry(QRect(50, 40, 81, 41))
        self.label_13.setStyleSheet(
            "background-color: rgba(248, 248, 248, 0);\n"
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-color: rgba(255, 255, 255, 0);\n"
            ""
        )
        self.widget5 = QWidget(self.centralwidget)
        self.widget5.setObjectName("widget5")
        self.widget5.setGeometry(QRect(170, 240, 161, 82))
        self.widget5.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(0, 0, 0);"
        )
        self.temp2 = QLabel(self.widget5)
        self.temp2.setObjectName("temp2")
        self.temp2.setGeometry(QRect(50, 10, 81, 41))
        self.temp2.setStyleSheet(
            "background-color: rgba(248, 248, 248, 0);\n"
            'font: 75 16pt "MS Shell Dlg 2";\n'
            "border-color: rgba(255, 255, 255, 0);\n"
            ""
        )
        self.label_27 = QLabel(self.widget5)
        self.label_27.setObjectName("label_27")
        self.label_27.setGeometry(QRect(0, -10, 81, 61))
        self.label_27.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);\n"
            "\n"
            'font: 28pt "MS Shell Dlg 2";\n'
            "border-color: rgba(255, 255, 255, 0);"
        )
        self.label_17 = QLabel(self.widget5)
        self.label_17.setObjectName("label_17")
        self.label_17.setGeometry(QRect(50, 40, 81, 41))
        self.label_17.setStyleSheet(
            "background-color: rgba(248, 248, 248, 0);\n"
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-color: rgba(255, 255, 255, 0);\n"
            ""
        )
        self.line_2 = QFrame(self.widget5)
        self.line_2.setObjectName("line_2")
        self.line_2.setGeometry(QRect(10, 50, 118, 3))
        self.line_2.setStyleSheet("")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.widget6 = QWidget(self.centralwidget)
        self.widget6.setObjectName("widget6")
        self.widget6.setGeometry(QRect(340, 240, 134, 82))
        self.widget6.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(0, 0, 0);"
        )
        self.temp3 = QLabel(self.widget6)
        self.temp3.setObjectName("temp3")
        self.temp3.setGeometry(QRect(50, 10, 81, 41))
        self.temp3.setStyleSheet(
            "background-color: rgba(248, 248, 248, 0);\n"
            'font: 75 16pt "MS Shell Dlg 2";\n'
            "border-color: rgba(255, 255, 255, 0);\n"
            ""
        )
        self.label_29 = QLabel(self.widget6)
        self.label_29.setObjectName("label_29")
        self.label_29.setGeometry(QRect(0, -10, 81, 61))
        self.label_29.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);\n"
            "\n"
            'font: 28pt "MS Shell Dlg 2";\n'
            "border-color: rgba(255, 255, 255, 0);"
        )
        self.label_22 = QLabel(self.widget6)
        self.label_22.setObjectName("label_22")
        self.label_22.setGeometry(QRect(50, 40, 81, 41))
        self.label_22.setStyleSheet(
            "background-color: rgba(248, 248, 248, 0);\n"
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-color: rgba(255, 255, 255, 0);\n"
            ""
        )
        self.line_3 = QFrame(self.widget6)
        self.line_3.setObjectName("line_3")
        self.line_3.setGeometry(QRect(10, 50, 118, 3))
        self.line_3.setStyleSheet("")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(20, 220, 134, 13))
        self.label.setStyleSheet(
            'font: 8pt "MS Shell Dlg 2";\n'
            "background-color: rgba(255, 255, 255, 0);\n"
            "border-color: rgba(255, 255, 255, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "qproperty-alignment: 'AlignCenter';"
        )
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(340, 220, 134, 13))
        self.label_2.setStyleSheet(
            'font: 8pt "MS Shell Dlg 2";\n'
            "background-color: rgba(255, 255, 255, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "qproperty-alignment: 'AlignCenter';\n"
            "border-color: rgba(255, 255, 255, 0);"
        )
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(190, 220, 134, 13))
        self.label_3.setStyleSheet(
            'font: 8pt "MS Shell Dlg 2";\n'
            "background-color: rgba(255, 255, 255, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "qproperty-alignment: 'AlignCenter';\n"
            "border-color: rgba(255, 255, 255, 0);"
        )
        self.uimode = QPushButton(self.centralwidget)
        self.uimode.setObjectName("uimode")
        self.uimode.setGeometry(QRect(380, 370, 99, 54))
        self.uimode.setStyleSheet(
            'font: 20pt "MS Shell Dlg 2";\n'
            "border-color: rgba(255, 255, 255, 0);\n"
            "background-color: rgba(255, 255, 255, 0);\n"
            "color: rgb(255, 255, 255);"
        )
        self.cfmode = QPushButton(self.centralwidget)
        self.cfmode.setObjectName("cfmode")
        self.cfmode.setGeometry(QRect(10, 380, 99, 37))
        self.cfmode.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-color: rgba(255, 255, 255, 0);\n"
            "background-color: rgba(255, 255, 255, 0);\n"
            "color: rgb(255, 255, 255);"
        )
        self.label1 = QLabel(self.centralwidget)
        self.label1.setObjectName("label1")
        self.label1.setGeometry(QRect(180, 430, 140, 140))

        self.label3 = QLabel(self.centralwidget)
        self.label3.setObjectName("label3")
        self.label3.setGeometry(QRect(300, 560, 60, 60))

        self.label2 = QLabel(self.centralwidget)
        self.label2.setObjectName("label2")
        self.label2.setGeometry(QRect(140, 560, 60, 60))

        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.label_18.setGeometry(QRect(150, 610, 81, 51))
        self.label_18.setStyleSheet(
            "background-color: rgba(248, 248, 248, 0);\n"
            'font: 75 10pt "MS Shell Dlg 2";\n'
            "border-color: rgba(255, 255, 255, 0);\n"
            ""
        )
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.label_16.setGeometry(QRect(120, 590, 51, 81))
        self.label_16.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);\n"
            'font: 16pt "MS Shell Dlg 2";\n'
            "border-color: rgba(255, 255, 255, 0);"
        )
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName("label_20")
        self.label_20.setGeometry(QRect(300, 610, 81, 51))
        self.label_20.setStyleSheet(
            "background-color: rgba(248, 248, 248, 0);\n"
            'font: 75 10pt "MS Shell Dlg 2";\n'
            "border-color: rgba(255, 255, 255, 0);\n"
            ""
        )
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName("label_19")
        self.label_19.setGeometry(QRect(350, 600, 51, 61))
        self.label_19.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);\n"
            'font: 16pt "MS Shell Dlg 2";\n'
            "border-color: rgba(255, 255, 255, 0);"
        )
        self.btnStop = QPushButton(self.centralwidget)
        self.btnStop.setObjectName("btnStop")
        self.btnStop.setGeometry(QRect(30, 700, 416, 51))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.label_10.setText(
            QCoreApplication.translate(
                "MainWindow", "🌡️", None))
        self.temp_2.setText(
            QCoreApplication.translate(
                "MainWindow", " 85°F", None))
        self.label_1_3.setText(
            QCoreApplication.translate(
                "MainWindow", "🕒", None))
        self.time_2.setTime(QTime(0, 0, 0))
        self.check_wifi.setText(
            QCoreApplication.translate(
                "MainWindow", "📡", None))
        self.check_blutooth.setText(
            QCoreApplication.translate(
                "MainWindow", "🅱️", None))
        self.labelGrillTemp.setText(
            QCoreApplication.translate("MainWindow", "Timer", None)
        )
        self.labelTimer.setText(
            QCoreApplication.translate("MainWindow", "GRILL TEMP", None)
        )
        self.label_1_1.setText(
            QCoreApplication.translate("MainWindow", " 0°F \n" " set", None)
        )
        self.label_11.setText(
            QCoreApplication.translate(
                "MainWindow", "🌡️", None))
        self.temp1.setText(
            QCoreApplication.translate(
                "MainWindow", " 85°F", None))
        self.label_13.setText(
            QCoreApplication.translate("MainWindow", " 0°F set", None)
        )
        self.temp2.setText(
            QCoreApplication.translate(
                "MainWindow", " 85°F", None))
        self.label_27.setText(
            QCoreApplication.translate(
                "MainWindow", "🌡️", None))
        self.label_17.setText(
            QCoreApplication.translate("MainWindow", " 0°F set", None)
        )
        self.temp3.setText(
            QCoreApplication.translate(
                "MainWindow", " 85°F", None))
        self.label_29.setText(
            QCoreApplication.translate(
                "MainWindow", "🌡️", None))
        self.label_22.setText(
            QCoreApplication.translate("MainWindow", " 0°F set", None)
        )
        self.label.setText(
            QCoreApplication.translate("MainWindow", "PROBE1 TEMP", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", "PROBE3 TEMP", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", "PROBE2 TEMP", None)
        )
        self.uimode.setText(
            QCoreApplication.translate(
                "MainWindow", "⚙", None))
        self.cfmode.setText(
            QCoreApplication.translate(
                "MainWindow", "°C/°F", None))
        self.label1.setText(
            QCoreApplication.translate(
                "MainWindow", "OFF", None))
        self.label3.setText(
            QCoreApplication.translate(
                "MainWindow", "0%", None))
        self.label2.setText(
            QCoreApplication.translate(
                "MainWindow", "0%", None))
        self.label_18.setText(
            QCoreApplication.translate(
                "MainWindow", "GAS", None))
        self.label_16.setText(
            QCoreApplication.translate(
                "MainWindow", "🔥", None))
        self.label_20.setText(
            QCoreApplication.translate("MainWindow", "ELECTRIC", None)
        )
        self.label_19.setText(
            QCoreApplication.translate(
                "MainWindow", "⚡", None))
        self.btnStop.setText(
            QCoreApplication.translate(
                "MainWindow", "STOP", None))

    # retranslateUi
