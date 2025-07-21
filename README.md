# desafio-fidelity


Automação para consulta processos judiciais (TJSP) com persistência em PostgreSQL.
OBS: Está modularizado para adicionar mais scrapers.

Coloquei a opção para chrome, pois uso Mac M1 e não tem suporte para o Edge. Ajustavél no .env

## Pré-requisitos

- Python 3.10 ou superior
- Google Chrome instalado
- ChromeDriver compatível com sua versão do Chrome
- Compativel com MSEdge

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/jcalled/desafio-fidelity.git

# Configurações no .env
No .env pode alterar configuracoes do banco de dados e do browser que vai fazer o scrape
Chrome ou Edge


# Criar o venv (Virtual)
```bash
python -m venv venv
```

No windows - venv\Scripts\activate
Mac/Liunux - source venv/bin/activate

# Instalar os pacotes
```bash
pip install -r requirements.txt
```

# Instalar o schema no PostgreSQL
está dentro sql/schema.sql

# Entrar na pasta src
```bash
cd src
python main.py
```


Como pedido no teste do deafio técnico, pediu para usar boas práticas e adicionar no PostgreSQL, embora no codigo tenha MariaDB
Caso seja para MariaDB não haveriam grandes modificações.

O sistema consulta os dados por CPF, RG ou Nome, e evita buscas repetidas no banco.
Os resultados são gravados automaticamente no banco de dados PostgreSQL.
O script reinicia automaticamente caso não encontre dados ou fique inativo por um tempo.