def converter_numero(valor):
    try:
        valor_parseado = int(valor)
        return valor_parseado
    except:
        return float(valor)