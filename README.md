# desafio-fidelity


Automação para consulta processos judiciais (TJSP) com persistência em PostgreSQL.
OBS: Está modularizado para adicionar mais scrapers.


## Pré-requisitos

- Python 3.10 ou superior
- Google Chrome instalado
- ChromeDriver compatível com sua versão do Chrome
- Compativel com MSEdge

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/desafio-fidelity.git

# Criar o venv (Virtual)
# python -m venv venv

No windows - venv\Scripts\activate
Mac/Liunux - source venv/bin/activate

# Instalar os pacotes
pip install -r requirements.txt

# Entrar na pasta src
cd src
Rodar: python main.py


Como pedido no teste do deafio técnico, pediu para usar boas práticas e adicionar no PostgreSQL, embora no codigo tenha MariaDB
Caso seja para MariaDB não haveriam grandes modificações.

O sistema consulta os dados por CPF, RG ou Nome, e evita buscas repetidas no banco.
Os resultados são gravados automaticamente no banco de dados PostgreSQL.
O script reinicia automaticamente caso não encontre dados ou fique inativo por um tempo.