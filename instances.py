def recomendar_instancia_mysql(metricas):
    # Critérios para recomendação de instância baseado em CPU, Memória e I/O
    if metricas['threads_running'] < 5 and metricas['queries'] < 1000:
        return 't3.small'
    elif metricas['threads_running'] < 10 and metricas['queries'] < 5000:
        return 't3.medium'
    elif metricas['threads_running'] < 15 and metricas['queries'] < 10000:
        return 't3.large'
    elif metricas['buffer_reads'] > 1000000 or metricas['buffer_writes'] > 500000:
        return 'm5.xlarge'
    elif metricas['buffer_reads'] > 5000000 or metricas['buffer_writes'] > 2500000:
        return 'm5.2xlarge'
    elif metricas['data_reads'] > 1000000 or metricas['data_writes'] > 500000:
        return 'r6i.4xlarge'
    elif metricas['data_reads'] > 5000000 or metricas['data_writes'] > 2500000:
        return 'r6i.8xlarge'
    elif metricas['data_reads'] > 10000000 or metricas['data_writes'] > 5000000:
        return 'r6i.12xlarge'
    elif metricas['data_reads'] > 20000000 or metricas['data_writes'] > 10000000:
        return 'x2iedn.16xlarge'
    else:
        return 'x2iedn.24xlarge'
