import json
from python.cotacao_acoes.tratamento_dados import acessar_dividendo

# Exemplo de estrutura JSON
estrutura_json = '''
{
    "Meta Data": {
        "1. Information": "Weekly Adjusted Prices and Volumes",
        "2. Symbol": "IBM",
        "3. Last Refreshed": "2024-02-09",
        "4. Time Zone": "US/Eastern"
    },
    "Weekly Adjusted Time Series": {
        "2024-02-01": {
            "1. open": "184.5100",
            "2. high": "186.1800",
            "3. low": "180.4900",
            "4. close": "185.3400",
            "5. adjusted close": "185.3400",
            "6. volume": "21784812",
            "7. dividend amount": "1.6600"
        },
        "2024-02-09": {
            "1. open": "185.5100",
            "2. high": "187.1800",
            "3. low": "181.4900",
            "4. close": "186.3400",
            "5. adjusted close": "186.3400",
            "6. volume": "22784812",
            "7. dividend amount": "1.6600"
        }
    }
}
'''

# Converter a string JSON para um objeto Python (dicionário)
dados = json.loads(estrutura_json)

acessar_dividendo(dados)
