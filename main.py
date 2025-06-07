import sys
from PySide6.QtWidgets import QApplication
from screens.main_screen import MainScreen
from utils.settings import Settings
import os
os.environ['QT_API'] = 'pyside6'
os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'
import traceback
from PySide6 import QtGui
import glob
import signal
from utils.logger import logger
from utils.common import is_rpi, get_config, kill_process_by_name, disable_screen_saver
import threading
import time
from settings import INIT_SCREEN, APP_DIR, CRASH_FILE
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QTimer
from functools import partial
from widgets.touchobserver import TouchObserver
def main():
    sys._excepthook = sys.excepthook
    def exception_hook(exctype, value, exc_tb):
        msg = f"Exctype: {exctype}, Value: {value}\nTraceback:\n {','.join(traceback.format_tb(exc_tb, limit=20))}"
        logger.error(f"!!!! Crashed! {msg}")
        with open(CRASH_FILE, 'w') as f:
            f.write(msg.replace('\\n', '\n'))
        getattr(sys, "_excepthook")(exctype, value, exc_tb)
        QApplication.exit(MainScreen.EXIT_CODE_CRASH)

    sys.excepthook = exception_hook

    kill_process_by_name(proc_name='fbi', use_sudo=True, sig=signal.SIGTERM)

    disable_screen_saver()

    logger.info("========== Starting Router Monitor Kiosk App ==========")

    app = QApplication(sys.argv)

    # Register fonts
   
    cur_exit_code = MainScreen.EXIT_CODE_CRASH

    while cur_exit_code == MainScreen.EXIT_CODE_CRASH:
        settings = Settings()
        main_screen = MainScreen(settings)
        main_screen.show()
        #touch_observer = TouchObserver(main_screen.window().windowHandle())
        #touch_observer.released.connect(main_screen.on_touch_released)
        cur_exit_code = app.exec()
        main_screen.close()


    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
