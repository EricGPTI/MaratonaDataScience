import oauth2
import pprint
import json

apikey = 'D6LLCA3sSZguxi02wSTzfS0WX'
apisecret = 'pP0FFJs8FVVbnVp4hA6o3EWxMeMAcVrbEIBvABlqWAucAFXgSL'
accesstoken = '76047049-WKDoJWOwXAX5fQOohE1B8Wzfz3u5bnTU7qrrEMIT9'
secrettoken = 'qTPZBJiN4YIeAXJvdTlhHW24ka2YQDjssWyglvSjRv4tI'

pesquisa = input('Informe algo a ser pesquisado: ')

consumer = oauth2.Consumer(apikey, apisecret)
token = oauth2.Token(accesstoken, secrettoken)

cliente = oauth2.Client(consumer, token)

requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + pesquisa + '&lang=pt')
string = requisicao[1].decode()
dictionary = json.loads(string)
pprint.pprint(dictionary)