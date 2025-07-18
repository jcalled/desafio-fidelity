
from selenium.webdriver.support.select import Select

# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options
# from selenium.webdriver import Edge

from selenium.webdriver.chrome.service import Service

# Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome as WebDriver
from selenium.webdriver import Chrome

import time
import sys
import os

# from core.restarter import Restarter


class TJSPScraper:

    # def __init__(self):
    #     self.restarter = Restarter()

    def carregaSite(self, filtro, documento):
        CHROMEDRIVER_PATH = '/opt/homebrew/bin/chromedriver' #if sys.platform == 'darwin' else ''
        service = Service(CHROMEDRIVER_PATH)
        options = Options()
        # options.add_argument("-headless")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        # browser = webdriver.Edge(service=service, options=options) # Edge

        browser = Chrome(service=service, options=options)
        browser.get("https://esaj.tjce.jus.br/cpopg/open.do")

        if (filtro == 0 or filtro == 1 or filtro == 3):
            try:
                select_el = browser.find_element('xpath','//*[@id="cbPesquisa"]')
                select_ob = Select(select_el)
                select_ob.select_by_value('DOCPARTE')
                browser.find_element('xpath','//*[@id="campo_DOCPARTE"]').send_keys(documento)
                browser.find_element('xpath','//*[@id="botaoConsultarProcessos"]').click()
            except:
                time.sleep(120)
                self.restarta_programa(self)
        elif (filtro == 2):
            try:
                select_el = browser.find_element('xpath','//*[@id="cbPesquisa"]')
                select_ob = Select(select_el)
                select_ob.select_by_value('NMPARTE')
                browser.find_element('xpath','//*[@id="pesquisarPorNomeCompleto"]').click()
                browser.find_element('xpath','//*[@id="campo_NMPARTE"]').send_keys(documento)
                browser.find_element('xpath','//*[@id="botaoConsultarProcessos"]').click()
            except:
                time.sleep(120)
                self.restarta_programa(self)
        return browser.page_source
