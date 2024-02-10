from busca_cotacao import obter_dados
import tratamento_dados

# Chamar a função para obter dados
dados = obter_dados('SNAG11')
#tratamento_dados.salvar_dados(dados)
#tratamento_dados.divididendo_mais_recente(dados)
print('{:.2f}'.format(tratamento_dados.obter_close_mais_recente(dados)))
