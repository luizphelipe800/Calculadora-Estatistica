from . import retornar_modas
import numpy as np

def calcular_moda(dados_prontos):
    classes = retornar_modas.retornar_classe_moda(dados_prontos)

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