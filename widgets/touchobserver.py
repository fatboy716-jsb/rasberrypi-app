from PySide6.QtCore import QObject, QPoint, Signal, QEvent


class TouchObserver(QObject):
    """
    Observer to monitor the global touch events.
    """
    pressed = Signal(QPoint)
    released = Signal(QPoint)
    moved = Signal(QPoint)

    def __init__(self, window):
        super().__init__(window)
        self._window = window
        self.window.installEventFilter(self)

    @property
    def window(self):
        return self._window

    def eventFilter(self, obj: QObject, event: QEvent):
        if self.window is obj:
            if event.type() == QEvent.Type.MouseButtonPress:
                self.pressed.emit(event.pos())
            elif event.type() == QEvent.Type.MouseMove:
                self.moved.emit(event.pos())
            elif event.type() == QEvent.Type.MouseButtonRelease:
                self.released.emit(event.pos())
        return super().eventFilter(obj, event)
