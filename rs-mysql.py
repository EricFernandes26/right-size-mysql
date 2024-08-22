import pymysql
from instances import recomendar_instancia_mysql
from relatorio import gerar_relatorio
import pandas as pd
from getpass import getpass

def coletar_metricas_mysql(host, user, password, db):
    conexao = pymysql.connect(host=host, user=user, password=password, db=db)
    cursor = conexao.cursor()

    # Coletando métricas de CPU
    cursor.execute("SHOW STATUS LIKE 'Threads_running';")
    threads_running = int(cursor.fetchone()[1])

    cursor.execute("SHOW STATUS LIKE 'Queries';")
    queries = int(cursor.fetchone()[1])

    # Coletando métricas de Memória
    cursor.execute("SHOW STATUS LIKE 'Innodb_buffer_pool_read_requests';")
    buffer_reads = int(cursor.fetchone()[1])

    cursor.execute("SHOW STATUS LIKE 'Innodb_buffer_pool_write_requests';")
    buffer_writes = int(cursor.fetchone()[1])

    cursor.execute("SHOW STATUS LIKE 'Created_tmp_disk_tables';")
    tmp_disk_tables = int(cursor.fetchone()[1])

    cursor.execute("SHOW STATUS LIKE 'Created_tmp_tables';")
    tmp_tables = int(cursor.fetchone()[1])

    # Coletando métricas de I/O de Disco
    cursor.execute("SHOW STATUS LIKE 'Innodb_data_reads';")
    data_reads = int(cursor.fetchone()[1])

    cursor.execute("SHOW STATUS LIKE 'Innodb_data_writes';")
    data_writes = int(cursor.fetchone()[1])

    cursor.execute("SHOW STATUS LIKE 'Innodb_os_log_written';")
    os_log_written = int(cursor.fetchone()[1])

    conexao.close()

    return {
        'threads_running': threads_running,
        'queries': queries,
        'buffer_reads': buffer_reads,
        'buffer_writes': buffer_writes,
        'tmp_disk_tables': tmp_disk_tables,
        'tmp_tables': tmp_tables,
        'data_reads': data_reads,
        'data_writes': data_writes,
        'os_log_written': os_log_written
    }

if __name__ == "__main__":
    # Solicitar entrada do usuário para as credenciais e informações do banco de dados
    host = input("Digite o host do MySQL: ")
    user = input("Digite o usuário do MySQL: ")
    password = getpass("Digite a senha do MySQL: ")  # getpass oculta a entrada da senha
    db = input("Digite o nome do banco de dados: ")

    # Coletar métricas do MySQL
    metricas_mysql = coletar_metricas_mysql(host=host, user=user, password=password, db=db)

    # Recomendar instância AWS e calcular pontuação
    instancia_recomendada, pontuacao = recomendar_instancia_mysql(metricas_mysql)

    # Adicionar a recomendação e pontuação às métricas
    metricas_mysql['instancia_recomendada'] = instancia_recomendada
    metricas_mysql['pontuacao'] = pontuacao

    # Converter as métricas para um DataFrame
    df = pd.DataFrame([metricas_mysql])

    # Exportar para um arquivo Excel
    df.to_excel('metricas_mysql.xlsx', index=False)

    # Gerar o relatório detalhado
    gerar_relatorio(metricas_mysql, pontuacao)

    print(f"Métricas coletadas: {metricas_mysql}")
    print(f"Pontuação calculada: {pontuacao}")
    print(f"Arquivo 'metricas_mysql.xlsx' criado com sucesso.")
    print(f"Relatório salvo como 'relatorio_pontuacao.txt'.")
