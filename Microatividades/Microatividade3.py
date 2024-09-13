#selection.sort


def selectionSort(array):
    # Percorre toda a lista
    for posicao_atual in range(len(array)):
        # Acha o menor elemento na parte desordenada da lista
        posicao_menor_valor = posicao_atual
        for proxima_posicao in range(posicao_atual + 1, len(array)):
            if array[proxima_posicao] < array[posicao_menor_valor]:
                posicao_menor_valor = proxima_posicao
        
        # Troca o menor elemento encontrado com o elemento na posição atual
        array[posicao_atual], array[posicao_menor_valor] = array[posicao_menor_valor], array[posicao_atual]
        
numeros = [34, 10, 24, 76, 54, 12, 33, 47, 67, 89, 23, 45, 67, 12, 9]

selectionSort(numeros)

# Mostra a lista ordenada
print(numeros)
