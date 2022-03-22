from bs4 import BeautifulSoup
import requests
import pywhatkit as pw

# - Coletando dados
URL = "https://www.kabum.com.br/produto/181088/processador-amd-ryzen-5-5600g-3-9ghz-4-4ghz-max-turbo-am4-video-integrado-6-nucleos-100-100000252box"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39"
}

web = requests.get(URL, headers=headers)

soup = BeautifulSoup(web.content, 'html.parser')

price = soup.find('h4', itemprop='price').getText()
title = soup.find('h1', itemprop='name').getText()

# - Formatando o preço
num_price = price[3:8]
num_price = num_price.replace('.', '')
num_price = float(num_price)

# - Disparando mensagem condicional
price_range = (0, 1500) # limites de preço

if num_price in range(price_range):
    msg = "{} Baixou de preço 😁!! Aproveita 💙!! R${:.2f} => Aproveita: {}".format(
        title, price, URL
    )    
    pw.sendwhatmsg("SEUNUMEROAQUI", msg, 16, 10)


