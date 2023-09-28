from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QWidget,)


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # config layout
        self.central_widget = QWidget()
        self.v_layout = QVBoxLayout()

        self.central_widget.setLayout(self.v_layout)

        self.setCentralWidget(self.central_widget)

        # Title
        self.setWindowTitle('Calculator')

    # Last Config
    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    # metod for add widjet simple
    def addWidgetToVlayout(self, widget: QWidget):
        self.v_layout.addWidget(widget)
        self.adjustFixedSize()
