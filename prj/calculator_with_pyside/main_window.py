from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QWidget,)

# Configurações da minha window


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # config layout
        self.central_widget = QWidget()
        self.vLayout = QVBoxLayout()

        self.central_widget.setLayout(self.vLayout)

        self.setCentralWidget(self.central_widget)

        # Title
        self.setWindowTitle('Calculator')

    # Last Config -> ajusta window para ficar fixa

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    # metod for add widjet simple
    def addWidgetToVlayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
