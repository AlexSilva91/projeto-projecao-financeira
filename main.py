from busca_cotacao import obter_dados
import tratamento_dados
import calculo

nome_cota = 'SNAG11'
aporte = 300
tempo_meses = 48
# Chamar a função para obter dados
dados = obter_dados(nome_cota)
#tratamento_dados.salvar_dados(dados)
dv_por_cota = float('{:.2f}'.format(tratamento_dados.divididendo_mais_recente(dados)))
valor_cota = tratamento_dados.obter_close_mais_recente(dados)


def progessao_investimento(nome_cota, aporte, tempo_meses, valor_cota, dv_por_cota):
    dic_progressao = dict()
    dv_total = 0
    montante = 0
    cotas = 0
    for x in range(0, tempo_meses):
        #Calcula a quantidade de cotas
        cotas += calculo.calcular_cotas_por_aporte(valor_cota, aporte)
        #Calcula o montante com base nos aportes. A cada novo aporte o montante é acrescido de um novo aporte
        montante += aporte
        list_cotas = calculo.retorna_lista_cotas()
        x = 0
        #guarda o valor que sobra ao coprar as cotas com cada novo aporte
        lista_cotas_fomatadas = list()
        for item in list_cotas:
            #a cada novo aporte ele soma o valor anterior com o novo valor que será adcionado
            x += item
            lista_cotas_fomatadas.append(float(float('{:.2f}'.format(x))))
    #Acrescenta novas cotas com o valor que sobrou de cada aporte realizada. 
    cotas += calculo.calcular_cotas_com_sobra(valor_cota, lista_cotas_fomatadas)
    #Calcula o dividendo total
    dv_total += calculo.calcular_dividendos(cotas, dv_por_cota)
    dic_progressao['nome_cota'] = nome_cota
    dic_progressao['montante_investido_R$'] = montante
    dic_progressao['dv_final_periodo_R$'] = dv_total
    dic_progressao['total_cotas'] = cotas
    dic_progressao['montante_final_R$'] = montante + dv_total
    return dic_progressao


dic_test = progessao_investimento(nome_cota, aporte, tempo_meses, valor_cota, dv_por_cota)
print('\n{}\n'.format(dic_test))
