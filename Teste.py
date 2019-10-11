import math

dados = [1,2,2,3,2,5,8,9,5,6,3]
intervalo = round(1+3.322*math.log(max(dados), 10))
distancia = round((max(dados)-min(dados))/intervalo)

def converter_list_values_in_int(dados):
    dados_inteiros = list()
    for x in dados:
        dados_inteiros.append(int(x))
    return dados_inteiros

def gerador_classes(dados):
    dados_trabalhados = {}

    for x in range(intervalo-1):
        dados_trabalhados[f'{min(dados) + x + distancia * x}-{min(dados)+ x + distancia * (x+1)}'] = list(filter(lambda d: (d >= (min(dados)+ x + distancia * x) and d <= min(dados)+ x + distancia * (x+1)), dados))

    return dados_trabalhados

def calculo_ponto_medio(dado_pronto):
    media_intervalo = {}
    media_classe = []
    soma = 0
    for x, y in dado_pronto.items():
        soma += len(y)
        val_do_intervalo = converter_list_values_in_int(x.split('-'))
        print(val_do_intervalo)
        media_classe.append(round((val_do_intervalo[0] + val_do_intervalo[1]))/2)
        media_intervalo[media_classe] = [len(y), soma]

    return {'amostragem': media_intervalo, 'media': media_classe}

def media(variavel):
    frequencia = len(dados)
    soma_total = 0
    for x, y in variavel['amostragem'].items():
        soma_total += round((x[0]+x[1])/2) * y[0]

    return round(soma_total / frequencia)

def mediana_e_moda(variavel):
    mediana_valor = 0
    pos = int(round(len(dados) / 2))
    for x in variavel:
        classe = variavel[x]
        if(pos >= (classe[1] - classe[0] + 1) and pos <= classe[1]):
            mediana_valor = x

    f_anterior = variavel[mediana_valor-1-distancia][0]
    f_posterior = variavel[mediana_valor+1+distancia][0]
    f_media = variavel[mediana_valor][0]
    d1 = f_media - f_anterior
    d2 = f_media - f_posterior

    mediana = round(mediana_valor + ((pos - f_anterior) / f_media) * distancia)
    moda = round((mediana_valor + (d1 / (d1+d2))*distancia))

    return [mediana, moda]

dados_prontos = gerador_classes(dados)
ponto_medio = calculo_ponto_medio(dados_prontos)

for x, y in dados_prontos.items():
    print(f'{x} | {len(y)}')

for x, y in ponto_medio.items():
    print(f'{x} | {y}')