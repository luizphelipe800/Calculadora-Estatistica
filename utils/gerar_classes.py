import math

def gerador_classes(dados):
    tabela_de_classes = dict()
    frequencia_acumulada = 0
    calc_num_classes = num_classes = math.floor((1 + 3.322) * math.log(len(dados), 10)) - 3
    num_classes = 1 if calc_num_classes <= 0 else calc_num_classes
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