import mysql.connector
import numpy as np
import time

# Configuração da conexão com o banco de dados
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Root123!',
    database='registros'
)
cursor = conn.cursor()

# Número de execuções para calcular a média
num_execucoes = 10
tempos_totais = []

cursor.execute("CREATE INDEX idx_cpf ON registros.Pessoas(cpf)")

for _ in range(num_execucoes):
    # Início da medição de tempo
    start_time = time.time()

    # Atualização de % dos registros existentes para simular conflito
    registros_totais = 100000
    conflito_percentual = 0.1
    registros_conflito = int(registros_totais * conflito_percentual)

    for i in range(registros_conflito):
        cpf = f"{np.random.randint(100,1000)}.{np.random.randint(100,1000)}.{np.random.randint(100,1000)}-{np.random.randint(10,100)}"
        novo_telefone = f"9{np.random.randint(10000000, 100000000)}"


        cursor.execute('''
            UPDATE Pessoas
            SET telefone = %s
            WHERE cpf = %s
        ''', (novo_telefone, cpf))

    # Commit da transação
    conn.commit()

    # Fim da medição de tempo
    end_time = time.time()

    # Tempo total decorrido
    tempo_decorrido = end_time - start_time
    print(f'Tempo decorrido na execução {len(tempos_totais) + 1}: {tempo_decorrido:.2f} segundos')

    # Armazenar tempo total para cálculo da média
    tempos_totais.append(tempo_decorrido)

# Calcular a média do tempo gasto
media_tempo = sum(tempos_totais) / num_execucoes
print(f'\nMédia do tempo gasto nas {num_execucoes} execuções: {media_tempo:.2f} segundos')

# Fechamento da conexão
conn.close()
