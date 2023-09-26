import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication, QPushButton, QWidget, QGridLayout, QMainWindow)

# a vida da minha tela:
app = QApplication(sys.argv)

# definindo window principal


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)


window = MyWindow()
# widget principal:
central_widget = QWidget()
# definindo window principal com widget principal
window.setCentralWidget(central_widget)
# titulo para window:
window.setWindowTitle('My Window Python')

button2 = QPushButton('My Button 2')
button2.setStyleSheet('font-size: 35px; color: black')

button3 = QPushButton('My Button 3')
button3.setStyleSheet('font-size: 35px; color: black')
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

# Slots -> Funções que se conectam a eventos:


@Slot()
def slot_example(status_bar):
    status_bar.showMessage('Show this Message')


@Slot()
def other_slot(checked):
    print('is checked?', checked)

# adiando a execução do slot:
# o signal hovered não possui argumentos a serem passados
# então a função interna verifica se está checkado, passando assim o True/False
# correspondente


# def thirdy_slot(action):
#     def inner():
#         other_slot(action.isChecked())
#     return inner

# mesma coisa com lambda:
@Slot()
def thirdy_slot(action):
    return other_slot(action.isChecked())


# menu bar
menu_bar = window.menuBar()
first_menu = menu_bar.addMenu('first Menu')

# Signals -> Eventos:

first_action = first_menu.addAction('First action')
# trigger -> quando é clicado
# quando a minha ação for clicada, execute a função slot
first_action.triggered.connect(lambda: slot_example(status_bar))

second_action = first_menu.addAction('Second action')
# quando a minha ação for clicada, check
second_action.setCheckable(True)
second_action.toggled.connect(other_slot)  # Me conectando a um slot
# quando meu mouse estiver em cima:
second_action.hovered.connect(lambda: thirdy_slot(second_action))

button.clicked.connect(lambda: thirdy_slot(second_action))

window.show()
app.exec()  # loop da aplicação
