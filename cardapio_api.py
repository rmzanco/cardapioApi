# Rodrigo Malosti Zanco - Sistemas de Informação 017
# Sistema que através de request pode ser resgatado o cardápio do Restaurante Universitário de Limeira (FT/FCA)

import requests
import html
import re

data = input("digite a data que você deseja saber o cardápio (formato ex: AAAA-MM-DD): ")
URL = "https://www.sar.unicamp.br/RU/view/site/cardapio.php?data=" + data

try:
    resp = requests.get(URL)
    txt_conteudo = resp.text
    # parser p/ converter html chars
    txt_parser = html.unescape(txt_conteudo)
    # transformar cada linha da str em uma lista
    lista_conteudo = txt_parser.splitlines()

    i = 0  # contador da lista
    tipo = 0  # critério utilizado para definir o tipo de cardápio
    horario = 0  # criterio utilizado para separar as definições de refeição almoço/janta

    for l in lista_conteudo:
        result = re.search("ARROZ", l)
        if result is not None:

            tipo = tipo + 1

            if tipo % 2 == 0:
                cardapio = "vegetariano"
            else:
                cardapio = "convencional"

            if horario <= 1:
                tipo_horario = "do almoço"
                horario = horario + 1
            else:
                tipo_horario = "da janta"

            arroz = l[52:-5]
            prato = lista_conteudo[i + 3][89:-5]
            guarnicao = lista_conteudo[i + 6][80:-5]
            proteina = lista_conteudo[i + 9][79:-5]
            salada = lista_conteudo[i + 12][77:-5]
            sobremesa = lista_conteudo[i + 15][80:-5]
            suco = lista_conteudo[i + 18][75:-5]

            print("Cardápio", cardapio, tipo_horario, "de hoje:\n",
                  arroz,     ",",
                  prato,     ",",
                  guarnicao, ",",
                  proteina,  ",",
                  salada,    ",",
                  sobremesa, ",",
                  "Suco de", suco)
        i = i + 1


except:
    print("Site Indisponível/Fora de operação")
