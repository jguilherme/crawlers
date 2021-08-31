from lxml import html
import requests

def getBovespaCNPJ(num):
    page = requests.get('http://www.bmfbovespa.com.br/pt-br/mercados/acoes/empresas/ExecutaAcaoConsultaInfoEmp.asp?CodCVM='+str(num)+'&ViewDoc=0#a')
    tree = html.fromstring(page.text)
    return tree.xpath('//td[@class="IdentificacaoDado" or @class="Dado"]/text()')
   
lista_paginas = [94, 108, 140, 434, 566, 574, 701, 787, 906, 922]
for num in lista_paginas:
    cnpj = False
    for linha in getBovespaCNPJ(num):
        words = ''
        for one_word in linha.split(): words = words + ' ' + one_word
        if cnpj == True: 
            print str(num) + " CNPJ: " + words
            break
        if words == " CNPJ:": cnpj = True
