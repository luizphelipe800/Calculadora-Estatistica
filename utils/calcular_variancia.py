import math

def calcular_variancia(dados_prontos, media, dados):
    soma_variancia = 0
    freq_total = len(dados)
    for k in dados_prontos:
        soma_variancia += len(dados_prontos[k][1])*math.pow((dados_prontos[k][3]-media), 2)

    return soma_variancia / freq_total