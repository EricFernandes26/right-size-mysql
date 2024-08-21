import pymysql
from instances import recomendar_instancia_mysql
import pandas as pd

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
# Coletar métricas do MySQL
metricas_mysql = coletar_metricas_mysql(host='localhost', user='root', password='password', db='sakila')

# Recomendar instância AWS
instancia_recomendada = recomendar_instancia_mysql(metricas_mysql)

# Adicionar a recomendação às métricas
metricas_mysql['instancia_recomendada'] = instancia_recomendada

# Converter as métricas para um DataFrame
df = pd.DataFrame([metricas_mysql])

# Exportar para um arquivo Excel
df.to_excel('metricas_mysql.xlsx', index=False)

print(f"Métricas coletadas: {metricas_mysql}")
print(f"Arquivo 'metricas_mysql.xlsx' criado com sucesso.")
  
