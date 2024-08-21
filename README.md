# MySQL Metrics to AWS EC2 Instance Recommendation

Este projeto é um script Python que coleta métricas de um banco de dados MySQL e recomenda uma classe de instância AWS EC2 com base no uso de CPU, memória e I/O.

## Funcionalidades

- Conecta-se a um banco de dados MySQL.
- Coleta métricas internas, como threads em execução, consultas, leituras e escritas de buffers, e I/O de disco.
- Recomenda uma classe de instância AWS EC2 com base nas métricas coletadas.
- Exporta os dados e a recomendação para um arquivo Excel (`metricas_mysql.xlsx`).

## Estrutura do Projeto

O projeto é dividido em dois arquivos principais:

- **`rs-mysql.py`**: Responsável por coletar as métricas do MySQL e exportá-las para um arquivo Excel.
- **`instances.py`**: Contém a lógica para recomendar uma classe de instância AWS EC2 com base nas métricas coletadas.

## Dependências

As seguintes bibliotecas Python são necessárias para rodar este projeto:

- `pymysql==1.0.3`
- `pandas==2.0.3`

Você pode instalar todas as dependências utilizando o comando:

```bash
pip install -r requirements.txt
```

## Como Usar
Configurar o Banco de Dados: Certifique-se de que o banco de dados MySQL esteja configurado e acessível.

Editar as Credenciais: No arquivo rs-mysql.py, edite as credenciais de acesso ao banco de dados:

```bash
metricas_mysql = coletar_metricas_mysql(host='localhost', user='user, password='****', db='test')
```

Executar o Script: Execute o script rs_mysql.py para coletar as métricas e gerar a recomendação de instância:

```bash
python3 rs_mysql.py
```

Ver o Resultado: O script irá gerar um arquivo **`metricas_mysql.xlsx`** com as métricas coletadas e a recomendação de instância.

## Exemplo de Saída
O arquivo Excel gerado (metricas_mysql.xlsx) conterá as seguintes colunas:

- threads_running: Número de threads em execução.
- queries: Número de consultas executadas.
- buffer_reads: Leituras do buffer InnoDB.
- buffer_writes: Escritas no buffer InnoDB.
- tmp_disk_tables: Tabelas temporárias criadas no disco.
- tmp_tables: Tabelas temporárias criadas na memória.
- data_reads: Leituras de dados do InnoDB.
- data_writes: Escritas de dados do InnoDB.
- os_log_written: Quantidade de logs do sistema operacional escritos.
  
![image](https://github.com/user-attachments/assets/44e8b341-ae53-45e8-9047-42e136cea106)


## Explicação dos Termos de Monitoramento do MySQL

### threads_running
* Significado: Número de threads ativas atualmente executando consultas no MySQL.
* Implicações: Um número elevado pode indicar sobrecarga do servidor ou a execução de consultas pesadas.

### queries
* Significado: Número total de consultas executadas desde o último restart do servidor.
* Implicações: Um número muito alto pode indicar ineficiência nas consultas ou um alto volume de atividade.

### buffer_reads
* Significado: Número de vezes (em bytes) que o MySQL leu dados do disco para o buffer de memória.
* Implicações: Um número elevado pode indicar falta de memória suficiente ou consultas que estão acessando dados que não estão em cache.

### buffer_writes
* Significado: Número de vezes (em bytes) que o MySQL escreveu dados do buffer de memória para o disco.
* Implicações: Um número alto pode indicar que o MySQL está escrevendo muitas alterações no disco, o que pode afetar o desempenho.

### tmp_disk_tables
* Significado: Número de tabelas temporárias criadas no disco.
* Implicações: Tabelas temporárias no disco podem afetar o desempenho, especialmente em operações de leitura e escrita.

### tmp_tables
* Significado: Número total de tabelas temporárias criadas (incluindo as no disco).
* Implicações: Um número alto pode indicar consultas complexas ou ineficientes.

### data_reads
* Significado: Número total de bytes lidos do disco.
* Implicações: Um número alto pode indicar que o MySQL está lendo muitos dados do disco, o que pode afetar o desempenho.

### data_writes
* Significado: Número total de bytes escritos no disco.
* Implicações: Um número alto pode indicar que o MySQL está escrevendo muitos dados no disco, o que pode afetar o desempenho.

### os_log_written
* Significado: Número de mensagens de log escritas no sistema operacional.
* Implicações: Um número alto pode indicar problemas ou atividades intensas no servidor.
