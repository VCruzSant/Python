# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
import sys
from PySide6.QtWidgets import QApplication, QPushButton

# a vida da minha tela:
app = QApplication(sys.argv)

button = QPushButton('My Button')
button.show()  # adiciona o widget na hierarquia e exibe na tela

app.exec()  # loop da aplicação
