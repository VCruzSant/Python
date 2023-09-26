import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication, QPushButton, QWidget, QGridLayout, QMainWindow)

# definindo window principal


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # widget principal:
        self.central_widget = QWidget()
        # definindo window principal com widget principal
        self.setCentralWidget(self.central_widget)
        # titulo para window:
        self.setWindowTitle('My Window Python')

        # buttons
        self.button = self.make_button('B1')
        self.button.clicked.connect(self.second_slot_check)

        self.button2 = self.make_button('B2')
        self.button2.setStyleSheet('font-size: 35px; color: black')

        self.button3 = self.make_button('B3')
        self.button3.setStyleSheet('font-size: 35px; color: black')
        # button.show()  # adiciona o widget na hierarquia e exibe na tela

        # layout onde coloco todos meus outros widgets
        self.grid_layout = QGridLayout()
        # apontando meu layout para widget principal
        self.central_widget.setLayout(self.grid_layout)
        # apontando botão para meu layout
        self.grid_layout.addWidget(self.button, 1, 1)
        self.grid_layout.addWidget(self.button2, 1, 2)
        self.grid_layout.addWidget(self.button3, 2, 1, 1, 2)

        # utilizasse window pq são exclusivos de window,
        # widget não possui esses atributos:

        # status bar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('a message')

        # Slots -> Funções que se conectam a eventos:

        # menu bar
        self.menu_bar = self.menuBar()
        self.first_menu = self.menu_bar.addMenu('first Menu')

        # Signals -> Eventos:

        self.first_action = self.first_menu.addAction('First action')
        # trigger -> quando é clicado
        # quando a minha ação for clicada, execute a função slot
        self.first_action.triggered.connect(self.slot_example)

        self.second_action = self.first_menu.addAction('Second action')
        # quando a minha ação for clicada, check
        self.second_action.setCheckable(True)
        self.second_action.toggled.connect(self.second_slot_check)
        # quando meu mouse estiver em cima:
        self.second_action.hovered.connect(self.second_slot_check)

    @Slot()
    def slot_example(self, status_bar):
        status_bar.showMessage('Show this Message')

    @Slot()
    def second_slot_check(self):
        print('is checked?', self.second_action.isChecked())

    def make_button(self, name: str):
        button = QPushButton(name)
        button.setStyleSheet('font-size: 35px; color: purple')
        return button


if __name__ == '__main__':
    # a vida da minha tela:
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    app.exec()  # loop da aplicação
