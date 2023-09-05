import time
from pathlib import Path

from selenium import webdriver  # webdriver para o ".Chrome" e "ChromeOptions"
from selenium.webdriver.chrome.service import Service  # driver executavel
from selenium.webdriver.common.by import By  # seleciona o obj da page
from selenium.webdriver.common.keys import Keys  # tecla importante ex: enteder
# Codição esperada:
from selenium.webdriver.support import expected_conditions as EC
# faz a espera de algo ser exibido para continuar a ação:
from selenium.webdriver.support.wait import WebDriverWait

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html


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
    TIME_TO_WAIT = 10
    options = ('--disable-gpu', '--no-sandbox',)

    # atribuindo a função que configura no navegador
    browser = make_chrome_browser(*options)
    # navegador abra nesse site:
    browser.get('https://www.google.com.br/')

    # navegador espere para encontrar o input, tempo de espera, espere até que:
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        # a condição de espera é a preseça do elemento ser localizada:
        EC.presence_of_element_located(
            # pelo nome 'q' -> name html
            (By.NAME, 'q')
        )
    )
    # pesquise por:
    search_input.send_keys('Hello World!')
    # de enteder:
    search_input.send_keys(Keys.ENTER)

    # Caso tenha certeza que o elemento vai estar na tela, pode pular o Wait:
    # Selecionando os resultados:
    results = browser.find_element(By.ID, 'search')
    # Dos resultados, selecione os links
    links = results.find_elements(By.TAG_NAME, 'a')
    # clique no primeiro link:
    links[0].click()

    # dorme por 10 segundos:
    time.sleep(TIME_TO_WAIT)
