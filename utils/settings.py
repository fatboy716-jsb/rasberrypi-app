from PySide6.QtCore import QObject, Signal


class Settings(QObject):
    theme_changed = Signal(bool)  # True for dark mode, False for light mode
    temp_unit_changed = Signal(bool)  # True for Celsius, False for Fahrenheit
    button_event = Signal(bool)

    def __init__(self):
        super().__init__()
        self._dark_mode = False
        self._timechange = False
        self._celsius = True

    @property
    def dark_mode(self) -> bool:
        return self._dark_mode

    @property
    def celsius(self) -> bool:
        return self._celsius

    @property
    def button_status(self) -> bool:
        return self._timechange

    def button(self):
        self._timechange = not self._timechange
        self.button_event.emit(self._timechange)

    def toggle_theme(self):
        self._dark_mode = not self._dark_mode
        self.theme_changed.emit(self._dark_mode)

    def toggle_temp_unit(self):
        self._celsius = not self._celsius
        self.temp_unit_changed.emit(self._celsius)
