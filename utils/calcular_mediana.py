from . import retornar_medianas
import numpy as np
import math

def calcular_mediana(dados_prontos, dados):
    pos_freq = math.ceil(len(dados)/2) #posição onde a mediana se encontra
    classe_mediana = retornar_medianas.recuperar_classe_mediana(dados_prontos, pos_freq)
    classe_inferior = classe_mediana[0][0][0]
    try:
        freq_anterior = classe_mediana[1][2]
    except:
        freq_anterior = 0
    amplitude = np.subtract.reduce(classe_mediana[0][0]) * (-1)
    freq_mediana = len(classe_mediana[0][1])


    mediana = (classe_inferior + (pos_freq-freq_anterior)*(amplitude/freq_mediana))

    return [classe_mediana[0][0], mediana]