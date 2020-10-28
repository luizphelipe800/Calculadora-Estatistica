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