import calculo

def calculo_test():
    valor_cota = 10.07
    dv_total = 0
    montante = 0
    cotas = 0
    aporte = 300
    tempo = 5
    for x in range(0, tempo):
        #Calcula a quantidade de cotas
        cotas += calculo.calcular_cotas_por_aporte(valor_cota, aporte)
        print(f'{cotas}')
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
        print('======={:.2}======'.format('#'))
    print(lista_cotas_fomatadas)
    #Acrescenta novas cotas com o valor que sobrou de cada aporte realizada. 
    cotas += calculo.calcular_cotas_com_sobra(valor_cota, lista_cotas_fomatadas)

    #Calcula o dividendo total
    dv_total += calculo.calcular_dividendos(cotas, 0.11)
    print(f'\n# Total investido -> R$ {montante}')
    print(f'# Total de dividendos ao final do período-> R$ {dv_total}')
    print(f'# Total de cotas -> {cotas}')
    print(f'# Montante + Dividendo = R$ {dv_total+montante}')

calculo_test()
