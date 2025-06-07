from PySide6.QtWidgets import QMainWindow, QPushButton
from PySide6.QtCore import Qt, QTimer, QTime
from ui.main_widget_ui import Ui_MainWindow
from utils.settings import Settings
import traceback
import sys
import os
from utils.common import is_rpi
from utils.api import api
from settings import CRASH_FILE


class MainScreen(QMainWindow):
    EXIT_CODE_CRASH = -12345678

    def __init__(self, settings: Settings):
        super().__init__()
        self.settings = settings
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.settings.theme_changed.connect(self.update_theme)
        self.settings.temp_unit_changed.connect(self.update_temp_unit)
        self.ui.uimode.clicked.connect(self.settings.toggle_theme)
        self.ui.cfmode.clicked.connect(self.settings.toggle_temp_unit)
        self.ui.btnStop.clicked.connect(self.settings.button)
        # Initialize theme
        self.update_theme(self.settings.dark_mode)
        self.update_temp_unit(self.settings.celsius)
        self.update_button_event(self.settings.button_status)

        if is_rpi:
            self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
            self.move(0, 0)
        if os.path.exists(CRASH_FILE) and is_rpi:
            os.remove(CRASH_FILE)
        self._inactive_timer = QTimer()
        self._inactive_timer.timeout.connect(api)
        self._inactive_timer.timeout.connect(self.timecount)
        self._inactive_timer.start(1000)

    def timecount(self):
        time = self.ui.time_2.time()
        if time != QTime(0, 0, 0) and self.settings.button_status:
            time = time.addSecs(-1)  # subtract 1 second
            self.ui.time_2.setTime(time)

    def update_button_event(self, button: bool):
        if not button:
            self.ui.btnStop.setText("Start")
        else:
            self.ui.btnStop.setText("Stop")

    def update_temp_unit(self, celsius: bool):
        if not celsius:
            for label in [self.ui.temp1, self.ui.temp2, self.ui.temp3, self.ui.temp_2]:
                text = label.text()
                celsius = float(text.replace("°C", "").strip())
                fahrenheit = (celsius * 9 / 5) + 32
                label.setText(f"{fahrenheit:.1f}°F")
        else:
            for label in [self.ui.temp1, self.ui.temp2, self.ui.temp3, self.ui.temp_2]:
                text = label.text()
                celsius = float(text.replace("°F", "").strip())
                fahrenheit = (celsius - 32) / 9 * 5
                label.setText(f"{fahrenheit:.1f}°C")
        pass

    def update_theme(self, dark_mode: bool):
        if dark_mode:
            for i in [
                self.ui.widget2,
                self.ui.widget3,
                self.ui.widget4,
                self.ui.widget5,
                self.ui.widget6,
                self.ui.label_1_1,
                self.ui.btnStop,
            ]:
                i.setStyleSheet(
                    """
                                background-color: #000;
                                color: #fff;
                            """
                )

            for i in [self.ui.label2, self.ui.label3]:
                i.setStyleSheet(
                    """
                                                background-color: #000;
                                                color: #fff; " border-radius: 30px;
                                                font: 12pt \"MS Shell Dlg 2\";
                                                qproperty-alignment: 'AlignCenter';
                                           """
                )

            self.ui.label1.setStyleSheet(
                """
                                            background-color: #000;
                                            color: #fff;
                                            border-radius: 70px; 
                                            font: 24pt \"MS Shell Dlg 2\";
                                            qproperty-alignment: 'AlignCenter';
                                        """
            )

        else:
            for i in [
                self.ui.widget2,
                self.ui.widget3,
                self.ui.widget4,
                self.ui.widget5,
                self.ui.widget6,
                self.ui.label_1_1,
                self.ui.btnStop,
            ]:

                i.setStyleSheet(
                    """
                                background-color: #fff;
                                color: #000;
                            """
                )

            self.ui.label1.setStyleSheet(
                """
                                       background-color: #fff;
                                       color: #000;
                                        border-radius: 70px;
                                        font: 24pt \"MS Shell Dlg 2\";
                                        qproperty-alignment: 'AlignCenter';
                                   """
            )
            for i in [self.ui.label2, self.ui.label3]:
                i.setStyleSheet(
                    """
                                                background-color: #fff;
                                                color: #000;
                                                border-radius: 30px; 
                                                font: 12pt \"MS Shell Dlg 2\";
                                                qproperty-alignment: 'AlignCenter';
                                           """
                )
