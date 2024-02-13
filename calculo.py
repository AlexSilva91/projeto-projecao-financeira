cotas_com_sobra = 0
valor_sobra = 0
sobra_valor = list()

def calculo_resto_divisao(valor_cota, aporte):
    global sobra_valor
    valor_sobra = aporte % valor_cota
    sobra_valor.append(valor_sobra)
    return float('{:.2f}'.format(valor_sobra))

def calcular_cotas_por_aporte(valor_cota, aporte):
    sobra = calculo_resto_divisao(valor_cota, aporte)
    cotas = (aporte-sobra)/valor_cota
    return float('{:.2f}'.format(cotas))

def calcular_dividendos(qtd_cotas, dividendo):
    return float('{:.2f}'.format(qtd_cotas*dividendo))

def calcular_cotas_com_sobra(valor_cota, lista_valores_sobra):
    if lista_valores_sobra: 
        indice = lista_valores_sobra[-1]
        if indice >= valor_cota:
            cotas_com_sobra = calcular_cotas_por_aporte(valor_cota, indice)
            print('\n+++++++++++++++++++++++++++++++++++++\nValor suficiente! -> {} cota(s)\n+++++++++++++++++++++++++++++++++++++'.format(cotas_com_sobra))
        else:
            cotas_com_sobra = 0
    else:
        print('\n+++++++++++++++++++++++++++\nValor insuficiente!\n+++++++++++++++++++++++++++')

    return cotas_com_sobra

def retorna_lista_cotas():
    global sobra_valor
    return sobra_valor
