import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from display import Display
from enviroment import WINDOW_ICON
from info import Info
from style import setupTheme
from buttons import Button


if __name__ == '__main__':
    # setando aplicação
    app = QApplication(sys.argv)
    # theme
    setupTheme()
    # setando janela principal
    window = MainWindow()

    # seta icone:
    icon = QIcon(str(WINDOW_ICON))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info:
    info = Info('27 ^ 2 = 729')
    window.addWidgetToVlayout(info)

    # set Display
    display = Display()
    display.setPlaceholderText('Digite um número')
    window.addWidgetToVlayout(display)

    # Button
    button = Button('A button')
    window.addWidgetToVlayout(button)

    # exec
    window.adjustFixedSize()
    window.show()
    app.exec()
