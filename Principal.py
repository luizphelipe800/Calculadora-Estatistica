import math
import numpy as np

dados = []

def gerador_classes(dados):
    tabela_de_classes = dict()
    frequencia_acumulada = 0
    num_classes = math.floor((1 + 3.322) * math.log(len(dados), 10)) - 3
    intervalo = round((max(dados) - min(dados)) / num_classes)

    for x in range(num_classes):
        x1 = min(dados)+ x + intervalo * x
        x2 = min(dados)+ x + intervalo * (x+1)
        frequencia = list(filter((lambda d: d >= x1 and d <= x2), dados))
        frequencia_acumulada += len(frequencia)
        media_classe = round((x1+x2)/2)
        freq_media = media_classe * len(frequencia)
        freq_media_quadrada = int(math.pow(media_classe, 2) * len(frequencia))
        tabela_de_classes[x] = [[x1, x2], frequencia, frequencia_acumulada, media_classe, freq_media, freq_media_quadrada]

    return tabela_de_classes

def recuperar_classe_mediana(dados_prontos, pos_freq):
    for k in dados_prontos:
        try:
            if(pos_freq in range(dados_prontos[k-1][2], dados_prontos[k][2])):
                classe_mediana = dados_prontos[k]
                classe_anterior = dados_prontos[k-1]
        except:
            if(pos_freq in range(dados_prontos[k][2])):
                classe_mediana = dados_prontos[k]
                classe_anterior = 0

    return [classe_mediana, classe_anterior]

def retornar_classe_moda(dados_prontos):
    aux = 0
    for k in dados_prontos:
        if(len(dados_prontos[k][1]) > aux):
            aux = len(dados_prontos[k][1])
            maior_freq = dados_prontos[k]
            try:
                freq_ant = dados_prontos[k-1]
            except:
                freq_ant = 0

            try:
                freq_pos = dados_prontos[k+1]
            except:
                freq_pos = 0

    return [freq_ant, maior_freq, freq_pos]


def calcular_media(dados_prontos):
    media = 0
    for k in dados_prontos:
        classe = dados_prontos[k][0]
        frequencia = len(dados_prontos[k][1])
        classe_media = round((classe[0]+classe[1])/2)

        media += classe_media*frequencia

    return round(media/len(dados))

def calcular_mediana(dados_prontos):
    pos_freq = math.ceil(len(dados)/2) #posição onde a mediana se encontra
    classe_mediana = recuperar_classe_mediana(dados_prontos, pos_freq)
    classe_inferior = classe_mediana[0][0][0]
    try:
        freq_anterior = classe_mediana[1][2]
    except:
        freq_anterior = 0
    amplitude = np.subtract.reduce(classe_mediana[0][0]) * (-1)
    freq_mediana = len(classe_mediana[0][1])


    mediana = (classe_inferior + (pos_freq-freq_anterior)*(amplitude/freq_mediana))

    return [classe_mediana[0][0], mediana]

def calcular_moda(dados_prontos):
    classes = retornar_classe_moda(dados_prontos)

    classe_min = classes[1][0][0]
    freq_media = len(classes[1][1])
    try:
        freq_ant = len(classes[0][1])
    except:
        freq_ant = 0
    freq_pos = len(classes[2][1])
    amplitude = np.subtract.reduce(classes[1][0]) * (-1)

    x1 = freq_media - freq_ant
    x2 = freq_media - freq_pos

    moda = classe_min + (x1/(x1+x2))*amplitude

    return [classes[1][0], moda]

def calcular_desvio_padrao(variancia):
    return math.sqrt(variancia)

def calcular_variancia(dados_prontos, media):
    soma_variancia = 0
    freq_total = len(dados)
    for k in dados_prontos:
        soma_variancia += len(dados_prontos[k][1])*math.pow((dados_prontos[k][3]-media), 2)

    return soma_variancia / freq_total

def imprimir_classe(classe):
    return f'{classe[0]} - {classe[1]}'

def main():
    while(True):
        entrada = input('Entre com os valores, separando-os por virgula\n pressione (Enter) | pressione (n) + (Enter) para calcular\n: ')
        if(entrada == 'n'):
            break

        for n in entrada.split(','):
            dados.append(int(n))


    dados_prontos = gerador_classes(dados)
    media = calcular_media(dados_prontos)
    mediana = calcular_mediana(dados_prontos)
    moda = calcular_moda(dados_prontos)
    variancia = calcular_variancia(dados_prontos, media)
    desvio = calcular_desvio_padrao(variancia)

    for k in dados_prontos:
       print(f'{dados_prontos[k][0][0]} - {dados_prontos[k][0][1]} | {len(dados_prontos[k][1])} | {dados_prontos[k][2]}')

    print(f'media: {media}\nmediana: {imprimir_classe(mediana[0])} | {round(mediana[1])}\nmoda: {imprimir_classe(moda[0])} | {round(moda[1])}')
    print(f'desvio padrão: {round(desvio, 2)} | variancia: {round(variancia, 2)}')

main()