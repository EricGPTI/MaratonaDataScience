import requests

texto = None

try:
    requisicao = requests.get('https://putsreq.com/i7OYTxVeoUWusassbPS6')
    print(requisicao.text)
except Exception as e:
    print('Deu merda!', e)

print(texto)