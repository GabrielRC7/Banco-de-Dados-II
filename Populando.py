import mysql.connector
import names
import numpy as np

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Root123!",
  database="registros"
)

cursor = mydb.cursor()

cursor.execute("CREATE TABLE registros.Pessoas (cpf varchar(15), nome varchar(50), email varchar(100), telefone varchar(10), v INT, PRIMARY KEY (cpf));")


for i in range(100000):
    first_name = names.get_first_name()
    gmail = f"{first_name.lower()}@gmail.com"
    cpf = f"{np.random.randint(100,1000)}.{np.random.randint(100,1000)}.{np.random.randint(100,1000)}-{np.random.randint(10,100)}"
    cellphone = f"9{np.random.randint(10000000, 100000000)}"

    cursor.execute(f"INSERT INTO registros.Pessoas VALUES ('{cpf}', '{first_name}', '{gmail}','{cellphone}', 1);")

mydb.commit()