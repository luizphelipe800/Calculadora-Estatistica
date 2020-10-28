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