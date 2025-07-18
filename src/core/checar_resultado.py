class ChecarResultado:
    def checar(self, html):
        if 'Não existem informações disponíveis' in html:
            return 1
        elif ('Processos encontrados' in html or 'Audiências' in html):
            if 'criminal' in html.lower():
                return 2
            return 5
        return 7

# Codigos:
# 1 = Não existe informações disponíveis 
# 2 = Encontrou processo ou Audiências criminais
# 5 = Encontrou processo ou Audiêna Civeis
# 7 = Outros

