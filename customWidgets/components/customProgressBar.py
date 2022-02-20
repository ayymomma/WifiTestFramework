import time

from PyQt5.QtWidgets import QProgressBar


style = """
QProgressBar {{
    border-style: solid;
    border-color: #E47900;
    border-radius: 7px;
    border-width: 2px;
    text-align: center;
    background-color: rgb(181, 181, 181);
}}
QProgressBar::chunk {{
    background-color: {bgColor};
}}
"""


class CustomProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMaximum(100)
        self._active = False
        self.setValue(0)

    def updateBar(self, i):
        while True:
            time.sleep(0.01)
            value = self.value() + i
            self.setValue(value)

            if value >= self.maximum() or self._active:
                self.setValue(100)
                break
            elif value >= self.maximum() or not self._active:
                break

    def setProgressBarStyle(self):
        adjustedStyle = style.format(bgColor="#de7c09")
        self.setStyleSheet(adjustedStyle)
