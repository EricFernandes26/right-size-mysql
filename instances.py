def recomendar_instancia_mysql(metricas):
    # Inicializar uma variável de pontuação
    pontuacao = 0

    # Pesos para cada métrica
    peso_threads = 1.5
    peso_queries = 1.2
    peso_buffer = 1.8
    peso_io = 2.0

    # Adicionar pontuação baseada nas métricas
    pontuacao += (metricas['threads_running'] * peso_threads)
    pontuacao += (metricas['queries'] * peso_queries)
    pontuacao += ((metricas['buffer_reads'] + metricas['buffer_writes']) * peso_buffer)
    pontuacao += ((metricas['data_reads'] + metricas['data_writes']) * peso_io)

    # Definir faixas de pontuação para recomendar a instância
    if pontuacao < 5000:
        instancia = 't3.small'
    elif pontuacao < 10000:
        instancia = 't3.medium'
    elif pontuacao < 20000:
        instancia = 'm5.large'
    elif pontuacao < 40000:
        instancia = 'm5.xlarge'
    elif pontuacao < 80000:
        instancia = 'm5.2xlarge'
    elif pontuacao < 160000:
        instancia = 'r6i.4xlarge'
    elif pontuacao < 320000:
        instancia = 'r6i.8xlarge'
    elif pontuacao < 640000:
        instancia = 'r6i.12xlarge'
    elif pontuacao < 1280000:
        instancia = 'x2iedn.16xlarge'
    else:
        instancia = 'x2iedn.24xlarge'

    return instancia, pontuacao
