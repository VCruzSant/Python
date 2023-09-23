# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

# a vida da minha tela:
app = QApplication(sys.argv)

button = QPushButton('My Button')
button.setStyleSheet('font-size: 35px; color: black')

button2 = QPushButton('My Button 2')
button.setStyleSheet('font-size: 35px; color: black')

button3 = QPushButton('My Button 3')
button.setStyleSheet('font-size: 35px; color: black')
# button.show()  # adiciona o widget na hierarquia e exibe na tela]

# widget principal:
central_widget = QWidget()
# layout onde coloco todos meus outros widgets
layout = QGridLayout()
# apontando meu layout para widget principal
central_widget.setLayout(layout)
# apontando botão para meu layout
layout.addWidget(button, 1, 1)
layout.addWidget(button2, 1, 2)
layout.addWidget(button3, 2, 1, 1, 2)

central_widget.show()  # widget principal, entre na hierarquia e exiba
app.exec()  # loop da aplicação
