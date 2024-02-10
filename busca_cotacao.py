import requests
from chave_api import chave_api_4

# Função para obter dados
def obter_dados(cota):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={}.SAO&apikey={}'.format(cota, chave_api_4)
    r = requests.get(url)
    data = r.json()
    return data

