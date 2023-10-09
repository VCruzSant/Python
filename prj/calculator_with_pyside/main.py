import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from display import Display
from enviroment import WINDOW_ICON
from info import Info
from style import setupTheme
from buttons import Button, ButtonsGrid


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

    # Config Grid
    BGrid = ButtonsGrid()
    window.vLayout.addLayout(BGrid)

    BGrid.addWidget(Button('0'), 0, 0)
    BGrid.addWidget(Button('1'), 0, 1)
    BGrid.addWidget(Button('2'), 0, 2)

    BGrid.addWidget(Button('3'), 1, 0)
    BGrid.addWidget(Button('4'), 1, 1)
    BGrid.addWidget(Button('5'), 1, 2)

    # exec
    window.adjustFixedSize()
    window.show()
    app.exec()
