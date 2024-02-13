import calculo

def calculo_test():
    valor_cota = 10.07
    dv_total = 0
    montante = 0
    cotas = 0
    aporte = 500
    aporte_sobra = 0
    tempo = 48
    for x in range(0, tempo):
        cotas += calculo.calcular_cotas_por_aporte(valor_cota, aporte)
        print(f'{cotas}')
        montante += aporte
        list = calculo.retorna_lista()
        x = 0
        lista = []
        for item in list:
            x += item
            lista.append(float(float('{:.2f}'.format(x))))
        print('======={:.2f}======'.format(x))


    print('\n')
    print(lista)
    print(lista[-1])
    cotas += calculo.calcular_cotas_com_sobra(valor_cota, lista)

    dv_total += calculo.calcular_dividendos(cotas, 0.11)
    print(f'\n# Total -> R$ {dv_total+montante}')
    print(f'# Total investido -> R$ {montante}')
    print(f'# Dividendos -> R$ {dv_total}')
    print(f'# Cotas -> {cotas}')

calculo_test()
