import sys
from PySide6.QtWidgets import (QApplication, QLabel)
from main_window import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    label1 = QLabel('My Label')
    label1.setStyleSheet('font-size: 50px')
    window.addWidgetToVlayout(label1)

    window.show()

    app.exec()
