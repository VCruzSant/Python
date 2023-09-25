# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec

import sys
from PySide6.QtWidgets import (
    QApplication, QPushButton, QWidget, QGridLayout, QMainWindow)

# a vida da minha tela:
app = QApplication(sys.argv)
# definindo window principal
window = QMainWindow()
# widget principal:
central_widget = QWidget()
# definindo window principal com widget principal
window.setCentralWidget(central_widget)
# titulo para window:
window.setWindowTitle('My Window Python')


button = QPushButton('My Button')
button.setStyleSheet('font-size: 35px; color: black')

button2 = QPushButton('My Button 2')
button.setStyleSheet('font-size: 35px; color: black')

button3 = QPushButton('My Button 3')
button.setStyleSheet('font-size: 35px; color: black')
# button.show()  # adiciona o widget na hierarquia e exibe na tela]

# layout onde coloco todos meus outros widgets
layout = QGridLayout()
# apontando meu layout para widget principal
central_widget.setLayout(layout)
# apontando botão para meu layout
layout.addWidget(button, 1, 1)
layout.addWidget(button2, 1, 2)
layout.addWidget(button3, 2, 1, 1, 2)


# utilizasse window pq são exclusivos de window,
# widget não possui esses atributos:

# status bar
status_bar = window.statusBar()
status_bar.showMessage('a message')


def slot_example(status_bar):
    status_bar.showMessage('Show this Message')


# menu bar
menu_bar = window.menuBar()
first_menu = menu_bar.addMenu('first Menu')
first_action = first_menu.addAction('First action')

# trigger -> quando é clicado
# quando a minha ação for clicada, execute a função slot
first_action.triggered.connect(lambda: slot_example(status_bar))

window.show()
app.exec()  # loop da aplicação
