from PySide6.QtWidgets import QPushButton, QGridLayout
from enviroment import MEDIUM_FONT
from utils import isEmpty, isNumOrNot


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

        self._makeGrid()

    def _makeGrid(self):
        # linhas
        for i, row in enumerate(self._grid_mask):
            for j, button_text in enumerate(row):
                # colunas
                button = Button(button_text)

                # se o botão não for número e não for vazio
                # (de acordo com minha função em utils.py) faça:
                if not isNumOrNot(button_text) and not isEmpty(button_text):
                    # setando estilo
                    # button pq se eu colocar self, ele vai aplicar o estilo na
                    # grid
                    button.setProperty('cssClass', 'specialButton')

                self.addWidget(button, i, j)
