import oracledb

# configurações de conexão
usuario = "insira_seu_usuario_aqui" # Substitua pelo seu usuário do banco Oracle
senha = "insira_sua_senha_aqui"  # Substitua pela sua senha do banco Oracle 
dsn = "oracle.fiap.com.br:1521/orcl"


def conectar():
    try:
        conn = oracledb.connect(user=usuario, password=senha, dsn=dsn)
        return conn
    except oracledb.DatabaseError as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None


def inserir_registro(registro):
    conn = conectar()
    if conn is None:
        return

    sql = """
        INSERT INTO colheita (
            area_ha, producao_bruta, velocidade_kmh, faixa_velocidade,
            clima, percentual_perda, perda_ton, producao_liquida
        ) VALUES (
            :1, :2, :3, :4, :5, :6, :7, :8
        )
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (
            registro["area_ha"],
            registro["producao_bruta"],
            registro["velocidade_kmh"],
            registro["faixa_velocidade"],
            registro["clima"],
            registro["percentual_perda"],
            registro["perda_ton"],
            registro["producao_liquida"]
        ))
        conn.commit()
        print("Registro salvo no banco Oracle!")
    except oracledb.DatabaseError as e:
        print(f"Erro ao inserir no banco: {e}")
    finally:
        conn.close()


def listar_registros():
    conn = conectar()
    if conn is None:
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM colheita ORDER BY id DESC")
        colunas = [col[0].lower() for col in cursor.description]
        registros = [dict(zip(colunas, row)) for row in cursor.fetchall()]
        return registros
    except oracledb.DatabaseError as e:
        print(f"Erro ao consultar banco: {e}")
        return []
    finally:
        conn.close()