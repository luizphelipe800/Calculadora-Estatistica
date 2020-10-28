def calcular_media(dados_prontos, dados):
    media = 0
    for k in dados_prontos:
        classe = dados_prontos[k][0]
        frequencia = len(dados_prontos[k][1])
        classe_media = round((classe[0]+classe[1])/2)

        media += classe_media*frequencia

    return round(media/len(dados))