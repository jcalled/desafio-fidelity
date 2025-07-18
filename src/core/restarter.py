import sys
import os

class Restarter:

    @staticmethod
    def restart():
        try:
            python = sys.executable
            os.execl(python, python, *sys.argv)
        except Exception:
            print("Erro ao reiniciar")
            quit()
