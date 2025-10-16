import os
import requests
import sqlite3
from datetime import datetime


caminho_pasta = r"C:\Users\viana\OneDrive\Documentos\Python Scripts\Sistemas distribuídos e mobile\atv2"
os.makedirs(caminho_pasta, exist_ok=True) 

caminho_bd = os.path.join(caminho_pasta, "bdcotacoes.db")

url = "https://api.hgbrasil.com/finance?key=fe302142"

response = requests.get(url)
data = response.json()

dolar = data['results']['currencies']['USD']['buy']
euro = data['results']['currencies']['EUR']['buy']

print(f"Dólar (compra): R$ {dolar}")
print(f"Euro  (compra): R$ {euro}")

conn = sqlite3.connect(caminho_bd)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS moedas (
    data TEXT,
    dolar REAL,
    euro REAL
)
''')

data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cursor.execute("INSERT INTO moedas (data, dolar, euro) VALUES (?, ?, ?)",
               (data_atual, dolar, euro))

conn.commit()
conn.close()

print(f"\n✅ Cotação salva com sucesso em: {caminho_bd}")
