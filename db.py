import psycopg2


def conectar():
    return psycopg2.connect(
        host
        user
        password
        dbname
    )


def buscar_pesquisas(filtro):

    # Rg é diferente de nada
    filtro_condicao = "AND rg <> ''" if filtro in [1, 3] else ''

    sql = f'''
        SELECT * FROM tabela
        
    '''

    connection = connectar()
    cursor = connection.cursor()
    cursor.execute()
    results = cursor.fetchall()
    cursor.close()
    return results