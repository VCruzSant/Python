# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python 😂
from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
PATH_IMAGE = ROOT_FOLDER / 'mtnt.jpg'
NEW_IMAGE = ROOT_FOLDER / 'new_image.jpg'

# passando a imagem pro editor PIL
pil_image = Image.open(PATH_IMAGE)

# desempacotando largura e altura da imagem passada pro pil
width, height = pil_image.size
# print(width, height)

# informações da foto:
exif = pil_image.info  # ou exif = pil_image.info['exif']
# print(exif)

# alterando tamanho em px da imagem
new_width = 640
# regra de três mantem proporção:
new_height = round(height * new_width / width)
# print(new_width, new_height)

# peguei a imagem com o pil, atribui a nova largura e altura:
new_image = pil_image.resize(size=(new_width, new_height))

# atribuindo as edições feitas para a nova imagem:
new_image.save(
    NEW_IMAGE,
    optimize=True,  # se vai otimizar ela
    quality=80,  # definindo a porcentagem de qualidade que a imagem vai ter
    # exif=exif,  # passando as configurações da imagem
)
