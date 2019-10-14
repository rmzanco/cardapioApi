# Rodrigo Malosti Zanco - Sistemas de Informação 017
# Utilizacao do beautiful soup para simplificação do scraping

import requests
import html
from bs4 import BeautifulSoup

# data = input("digite a data que você deseja saber o cardápio (formato ex: AAAA-MM-DD): ")

URL = "https://www.sar.unicamp.br/RU/view/site/cardapio.php"

try:
    resp = requests.get(URL)
    txt_conteudo = resp.text
    # parser p/ converter html chars
    txt_parser = html.unescape(txt_conteudo)
    # transformar cada linha da str em uma lista
    lista_conteudo = txt_parser.splitlines()

    soup = BeautifulSoup(txt_parser, 'html.parser', parse_only=None)

    cardapio1 = soup.find_all(class_='fundo_cardapio')[0].get_text().splitlines()  # encontrar a tag que contém todos os elementos do cardápio.
    cardapio1 = list(dict.fromkeys(cardapio1))  # remover elementos repetidos de uma lista

    cardapio2 = soup.find_all(class_='fundo_cardapio')[1].get_text().splitlines()
    cardapio2 = list(dict.fromkeys(cardapio2))

    cardapio3 = soup.find_all(class_='fundo_cardapio')[2].get_text().splitlines()
    cardapio3 = list(dict.fromkeys(cardapio3))

    cardapio4 = soup.find_all(class_='fundo_cardapio')[3].get_text().splitlines()
    cardapio4 = list(dict.fromkeys(cardapio4))

    print(cardapio1)
    print(cardapio2)
    print(cardapio3)
    print(cardapio4)

except:
    print("Site Indisponível/Fora de operação")
