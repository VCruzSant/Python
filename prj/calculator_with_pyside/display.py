from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt
import enviroment


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(F'font-size: {enviroment.BIG_FONT}px;')
        self.setMinimumHeight(enviroment.BIG_FONT * 2)
        self.setMinimumWidth(enviroment.MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[enviroment.DEFAULT_MARGIN for _ in range(4)])
