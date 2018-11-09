import re
import requests
requisicao = None
padrao = None
def email_site(requisicao):
    try:
        requisicao = requests.get('https://www.anhanguera.com/graduacao/localidades/faculdade-anhanguera-tecnologia-sao-bernardo-FAT.php')
        padrao = re.findall(r'[\w\.\-\_]+@[\w]+\.[\w\.]+', requisicao.text)
        if padrao != '':
            print(padrao)
        else:
            print('Valores não localizados')
    except Exception as ex:
        print('Requisição sem sucesso! ', ex)


email_site(requisicao)