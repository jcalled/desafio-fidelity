from abc import ABC, abstractmethod
class ScraperInterface(ABC):
    @abstractmethod
    def carregaSite(self, filtro, documento) -> str:
        pass