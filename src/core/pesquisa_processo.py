import datetime, time
from tqdm import tqdm
from core.restarter import Restarter
from core.checar_resultado import ChecarResultado
from services.database import Database
from scraper.tjsp_scraper import TJSPScraper


SCRAPERS = {
    "TJSP": TJSPScraper()
}

class PesquisaProcesso:
    def __init__(self, filtro=0, scraper_name='TJSP'):
        self.filtro = filtro
        self.database = Database()
        self.scraper = self.get_scraper(scraper_name) 
        self.checar_resultado = ChecarResultado()
        self.restarter = Restarter()
        
    # Metodo para pegar qualquer outro scraper
    @staticmethod
    def get_scraper(nome: str):
        return SCRAPERS.get(nome)

    # Método para consultar no banco de dados 
    def pesquisar(self):
        i = self.filtro

        while(i <= 3):
            pesquisas = self.database.pesquisar(i)
        
            if not pesquisas:
                print("Nenhuma pesquisa encontrada. Reiniciando em 30 segundos")
                time.sleep(30)
                self.restarter.restart() # Método para reiniciar
                return
 
            inicio = datetime.datetime.now()

            for data in tqdm(pesquisas):
                cod_pesquisa, nome, cpf, rg, spv_tipo = data[1], data[4], data[5], data[6], data[11]
                self._executar_pesquisa(i, nome, cpf, rg, cod_pesquisa, spv_tipo)

                if (datetime.datetime.now() - inicio).total_seconds() > 600:
                    break

                i += 1
                print(i)

        print("Finalizando... reiniciando ciclo.")
        self.restarter.restart()



    
    def _executar_pesquisa(self, filtro, nome, cpf, rg, cod_pesquisa, spv_tipo):


        # Verificar se ja esta cadastrado. Já pesquidado? pula
        if self.database.existe_pesquisa_spv(cod_pesquisa):
            print(f"Pesquisa {cod_pesquisa} já realizado. Pulando...")
            return

        documento = cpf if filtro == 0 else rg if filtro in [1, 3] else nome
        if not documento:
            return
        html = self.scraper.carregaSite(filtro, documento)
        resultado = self.checar_resultado.checar(html)
        print('resultado')
        print(resultado)
        self.database.inserir_pesquisa(cod_pesquisa, resultado, filtro)
