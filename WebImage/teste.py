import requests
import pandas as pd
from bs4 import BeautifulSoup

# Download WebPage
pudim = "http://pudim.com.br/"
resultado = requests.get(pudim)

# Se der certo analiza o download pelo BeaultfulSoup objeto, oque permitila uma melhor manipulação
if resultado.status_code == 200:
    soup = BeautifulSoup(resultado.content, "html.parser")

# Procurar o objeto com a class HTML classificado na webpage
table = soup.find('table',{'class':'wikitable sortable'})

# Uma volta sobre todas as linhas e as puxando(lendo) como texto
new_table = []
for row in table.find_all('tr')[1:]:
    column_maker = 0
    columns = row.find_all('td')
    bew_table.append({column.get_text() for column in columns})

df = pd.Dataframe(new_table, columns = ['ContinetCode','Alpha2','Alpha3','PhoneCode','Name'])
df['Name'] = df['Name'].str.replace('\n','')
df
