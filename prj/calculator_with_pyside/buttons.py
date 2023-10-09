from PySide6.QtWidgets import QPushButton, QGridLayout
from enviroment import MEDIUM_FONT


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        # self.setStyleSheet(f'font-size: {MEDIUM_FONT}px')
        # instanciando a fonte numa variavel
        font = self.font()
        # passando uma configuração para fonte
        font.setPixelSize(MEDIUM_FONT)
        # setando a fonte configurada
        self.setFont(font)
        # setando tamanho minimo
        self.setMinimumSize(60, 60)
        # setando estilo
        self.setProperty('cssClass', 'specialButton')


class ButtonsGrid(QGridLayout):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
