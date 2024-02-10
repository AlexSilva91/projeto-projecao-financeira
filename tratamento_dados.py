import json

def salvar_dados(dados):
    with open('arquivo.txt', 'a') as file:
        formatted_data = json.dumps(dados, indent=4)
        file.write(formatted_data + '\n')

    print("Dados adicionados ao arquivo existente de forma formatada.")

def obter_simbolo(dados):
    simbolo = dados.get("Meta Data", {}).get("2. Symbol")
    if simbolo:
        return simbolo
    else:
        return 'Não localizado!'
    

def obter_close_mais_recente(dados):
    # Encontrar a data mais recente
    data_mais_recente = max(dados["Weekly Adjusted Time Series"].keys())

    # Acessar os dados da data mais recente
    dados_da_data_mais_recente = dados["Weekly Adjusted Time Series"][data_mais_recente]

    # Acessar o valor de "4. close" para a data mais recente
    close_mais_recente = dados_da_data_mais_recente.get("4. close")

    if close_mais_recente:
        return float(close_mais_recente)
    else:
        return None 
    
    
def divididendo_mais_recente(dados):
    for data in sorted(dados["Weekly Adjusted Time Series"], reverse=True):
        dados_da_data = dados["Weekly Adjusted Time Series"][data]
        dividendo = dados_da_data.get("7. dividend amount")
        if dividendo and float(dividendo) > 0.0:
            print('O primeiro dividendo maior ou igual a zero para a data {} é: {:.2f}'.format(data, float(dividendo)))
            return 

