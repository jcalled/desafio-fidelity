
from selenium.webdriver.support.select import Select

from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
# from selenium.webdriver import Edge


# Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver import Chrome as WebDriver
from selenium.webdriver import Chrome

import time
import sys
import os

from dotenv import load_dotenv

# from core.restarter import Restarter

# Adicionando interface
from interfaces.scraper_interface import ScraperInterface

class TJSPScraper(ScraperInterface):

    # def __init__(self):
    #     self.restarter = Restarter()

    def carregaSite(self, filtro, documento):

        # if BROWSER == "edge":
        #     service = EdgeService(executable_path=DRIVER_PATH)
        #     options = EdgeOptions()
        # else:
        #     service = ChromeService(executable_path=DRIVER_PATH)
        #     options = ChromeOptions()

        if os.getenv("BROWSER") == "edge":
            service = EdgeService(executable_path=EXECUTAVEL+"msedgedriver.exe")
            options = EdgeOptions()
        else:
            CHROMEDRIVER_PATH = '/opt/homebrew/bin/chromedriver' #if sys.platform == 'darwin' else ''
            service = ChromeService(CHROMEDRIVER_PATH)
            options = ChromeOptions()
        
        options.add_argument("-headless")
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
