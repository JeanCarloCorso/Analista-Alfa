import requests
import psycopg2
import time


dbname = "Alfa"
user = "postgres"
password = "****"

conn = psycopg2.connect(dbname= dbname, user= user, password=password)
cur = conn.cursor()

filiais = (
  "82110818000121","82110818000202","82110818000393",
  "82110818001608","82110818000806","82110818002760",
  "82110818002094","82110818002507","82110818002841"
  )

def inserir(cnpj):
  
  while True:
    dados = requests.get("https://www.receitaws.com.br/v1/cnpj/"+cnpj)
    if dados.status_code == 200:
      break
    time.sleep(5)

  dados = dados.json()
  empresa = (
    dados['cnpj'],dados['nome'],
    dados['municipio'],dados['uf']
    )
  sql = ("INSERT INTO Filiais (cnpj,nome,cidade,estado) values (%s, %s, %s, %s)")
  cur.execute(sql,empresa)
  conn.commit()

for filial in filiais:
  inserir(filial)
print("Processo finalizado sem erros")
