import psycopg2
from services.config import DB_HOST, DB_USER, DB_PORT, DB_PASSWORD, DB_NAME

class Database:

    # Construtor para conexão ao banco
    def __init__(self):
        self.connection = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            dbname=DB_NAME
        )

    def pesquisar(self, filtro):


        filtro_condicao = " AND rg <> ''  " if (filtro in[1,3]) else ''

        params_sql = [] # Vou adicionar para evitar SQL Injection. Utilizo %s dentro da Query

        sql = f"""
            SELECT DISTINCT 
                p.Cod_Cliente, 
                p.Cod_Pesquisa, 
                e.UF, 
                p.Data_Entrada, 
                COALESCE(p.nome_corrigido, p.nome) AS nome, 
                p.CPF, 
                COALESCE(p.rg_corrigido, p.rg),
                p.Nascimento, 
                COALESCE(p.mae_corrigido, p.mae), 
                p.anexo,
                ps.Resultado AS resultado, 
                ps.cod_spv_tipo
             FROM pesquisa p
            INNER JOIN servico s ON p.Cod_Servico = s.Cod_Servico
             LEFT JOIN lote_pesquisa lp ON p.Cod_Pesquisa = lp.Cod_Pesquisa
             LEFT JOIN lote l ON l.cod_lote = lp.cod_lote
             LEFT JOIN estado e ON e.Cod_UF = p.Cod_UF
             LEFT JOIN pesquisa_spv ps ON ps.Cod_Pesquisa = p.Cod_Pesquisa AND ps.Cod_SPV = 1 AND ps.filtro = %s
            WHERE p.Data_Conclusao IS NULL AND ps.resultado IS NULL
              AND p.tipo = 0 AND p.cpf <> '' {filtro_condicao}
              AND (e.UF = 'SP' OR p.Cod_UF_Nascimento = 26 OR p.Cod_UF_RG = 26)
              
            GROUP BY p.cod_pesquisa,
                p.Cod_Cliente,
                p.Cod_Pesquisa,
                e.UF,
                p.Data_Entrada,
                COALESCE(p.nome_corrigido, p.nome),
                p.CPF,
                COALESCE(p.rg_corrigido, p.rg),
                p.Nascimento,
                COALESCE(p.mae_corrigido, p.mae),
                p.anexo,
                ps.Resultado,
                ps.cod_spv_tipo
            ORDER BY nome ASC, resultado DESC
            LIMIT 210
        """

        params_sql.append(filtro) 

        cursor = self.connection.cursor()
        cursor.execute(sql, params_sql)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def inserir_pesquisa(self, cod_pesquisa, resultado, filtro):

        sql = """
            INSERT INTO pesquisa_spv
                (cod_pesquisa, cod_spv, cod_spv_computador, cod_spv_tipo, resultado, cod_funcionario, filtro, website_id)
            VALUES 
                (%s, 1, 36, NULL, %s, -1, %s, 1)
            ON CONFLICT  (cod_pesquisa) DO NOTHING
        """

        cursor = self.connection.cursor()
        cursor.execute(sql, [cod_pesquisa, resultado, filtro])
        self.connection.commit()
        cursor.close
