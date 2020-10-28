from terminaltables import SingleTable
import re

from utils import calcular_media
from utils import calcular_mediana
from utils import calcular_moda
from utils import calcular_variancia
from utils import calcular_desvio_padrao
from utils import gerar_classes
from utils import converter_numero

def imprimir_classe(classe):
    return f'{classe[0]} - {classe[1]}'

def main():
    dados = []
    dados_tabela = [
        ['classes', 'dados tratados', 'montante']
    ]

    entrada = input('Entre com os valores, separando-os por virgula e pressione (Enter):\n ')

    try:
        for n in entrada.split(','):
            dados.append(converter_numero.converter_numero(n))

        dados_prontos = gerar_classes.gerador_classes(dados)
        media = calcular_media.calcular_media(dados_prontos, dados)
        mediana = calcular_mediana.calcular_mediana(dados_prontos, dados)
        moda = calcular_moda.calcular_moda(dados_prontos)
        variancia = calcular_variancia.calcular_variancia(dados_prontos, media, dados)
        desvio = calcular_desvio_padrao.calcular_desvio_padrao(variancia)

        for k in dados_prontos:
            dados_tabela.append([f'{dados_prontos[k][0][0]} - {dados_prontos[k][0][1]}', f'{dados_prontos[k][1]}', f'{dados_prontos[k][2]}'])

        calculos_tabela = [
            ['media', 'moda', 'mediana', 'desvio padrão', 'variancia']
        ]
        
        calculos_tabela.append([f'{media}', f'{round(mediana[1])}', f'{round(moda[1])}', f'{round(desvio, 2)}', f'{round(variancia, 2)}'])

        tabela1 = SingleTable(dados_tabela)
        tabela2 = SingleTable(calculos_tabela);

        print(tabela1.table)
        print(tabela2.table)
    except:
        print('os dados inseridos devem ser apenas numericos')

main()