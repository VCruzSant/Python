import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


ROOT_FOLDER = Path(__file__).parent
DRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    # opções para abrir o navegador:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    # serviço que executa o chrome:
    # obs: str foi para tirar o erro de tipagem bugado:
    chrome_service = Service(executable_path=str(DRIVER_EXEC))

    # configuração final do chrome:
    chrome_browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )

    return chrome_browser


if __name__ == '__main__':
    options = ('--disable-gpu', '--no-sandbox',)

    # abrir um site:
    browser = make_chrome_browser(*options)
    browser.get('https://www.google.com.br/')
    time.sleep(30)
