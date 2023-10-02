import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from display import Display
from enviroment import WINDOW_ICON


if __name__ == '__main__':
    # setando aplicação
    app = QApplication(sys.argv)
    # setando janela principal
    window = MainWindow()

    # seta icone:
    icon = QIcon(str(WINDOW_ICON))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # set Display
    display = Display()
    display.setPlaceholderText('Digite um número')
    window.addWidgetToVlayout(display)

    # exec
    window.adjustFixedSize()
    window.show()
    app.exec()
