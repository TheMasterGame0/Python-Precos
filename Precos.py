import requests
import time
from bs4 import BeautifulSoup
page = 1
# Toda vez que for executado irá apagar todo o arquivo antes de escrever.
# It will erase all the info from the document every time it executes.
with open('dados.txt', 'w') as dados:
   while page <= 10:
      # Determina o link e a pagina que será acessada
      # Determine which page will be accessed
      link = "https://www.amazon.com.br/s?k=manga&i=stripbooks&page="+ str(page) +"&__mk_pt_BR=ÅMÅŽÕÑ&crid=53AMKXUT0NQ5&qid=1691793524&sprefix=manga%2Cstripbooks%2C204&ref=sr_pg_1"

      response = requests.get(link)

      soup = BeautifulSoup(response.text, "lxml")
      Caixa = soup.select(".sg-col-inner .a-section .sg-col-inner .a-section.a-spacing-small.a-spacing-top-small", href=True)

      Titulos = []
      Precos = []
      Tipos = []
      for item in Caixa:
         # Pega o Título de cada caixa
         # Takes the Title of each box
         Titulos.append(item.select(".a-section.a-spacing-none.puis-padding-right-small.s-title-instructions-style .a-size-medium.a-color-base.a-text-normal", href=True)) 

         # Pega todos os preços de uma caixa
         # Takes all the prices of one box
         Precos.append(item.select(".sg-col-inner .a-row.a-size-base.a-color-base .a-price .a-offscreen", href = True))
         
         # Retorna o tipo do preço principal "[0]"
         # Return the type from the principal price "[0]"
         Tipos.append(item.select(".sg-col-inner .a-row.a-spacing-mini.a-size-base.a-color-base")) 

      for titulo, tipo, preco in zip(Titulos, Tipos, Precos):
         #print(titulo[0].text + ": "+ tipo[0].text + " - "+ preco[0].text)
         try:
            dados.write(titulo[0].text + ";"+ tipo[0].text + ";"+ preco[0].text + ';\n')
         except:
            print("Erro na escrita!")
      
      page += 1
      time.sleep(1)
