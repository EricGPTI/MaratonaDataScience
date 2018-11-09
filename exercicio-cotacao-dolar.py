import json
import requests
import time
import datetime

req = None
cotacao = []
dictionary = None

def cotacao_dolar(cotacao):
    dataAtual = datetime.datetime.now()
    dataAtualTxt = dataAtual.strftime('%d/%m/%Y %H:%M')
    while True:
        try:
            req = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=BRL&apikey=5ZYUQIK6YMZ0W2D3')
            dictionary = json.loads(req.text)
            print(dictionary)
            print('####################################################################')
            print('###################Cotação do Dólar em Tempo Real###################')
            print('###################    Data: ', dataAtualTxt,'  ###################')
            print('###################  USD 1,00 = R$ ' + dictionary['Realtime Currency Exchange Rate']['5. Exchange Rate'],'   ###################')
            print('####################################################################')
        except Exception as e:
            print('Não foi possível estabeler conexão!', e)
        time.sleep(20)
        cotacao_dolar(dictionary)
cotacao_dolar(cotacao)