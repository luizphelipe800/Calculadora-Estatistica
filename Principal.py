import math
import numpy as np

dados = [1,1,1,2,2,1,1,2,2,5,5,5,4,4,4,4,3,3,3,3,6,6,6,8,100,200,102,104]
num_classes = round((1 + 3.322) * math.log(len(dados), 10))
intervalo = round((max(dados)-min(dados))/num_classes)

def gerador_classes(dados):
    tabela_de_classes = dict()
    frequencia_acumulada = 0

    for x in range(num_classes):
        x1 = min(dados)+ x + intervalo * x
        x2 = min(dados)+ x + intervalo * (x+1)
        frequencia = list(filter((lambda d: d >= x1 and d <= x2), dados))
        frequencia_acumulada += len(frequencia)
        tabela_de_classes[x] = [[x1, x2], frequencia, frequencia_acumulada]

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


dados_prontos = gerador_classes(dados)
media = calcular_media(dados_prontos)
mediana = calcular_mediana(dados_prontos)
moda = calcular_moda(dados_prontos)

for k in dados_prontos:
   print(f'{dados_prontos[k][0]} | {len(dados_prontos[k][1])} | {dados_prontos[k][2]}')

print(f'media: {media}\nmediana: {mediana}\nmoda: {moda}')