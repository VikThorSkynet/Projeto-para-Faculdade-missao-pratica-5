# bubble.sort

# Implementação do algoritmo Bubble Sort
def bubbleSort(array):
    # Loop para percorrer o array
    for i in range(len(array)):
        # Loop interno para comparar os elementos adjacentes
        for j in range(0, len(array) - i - 1):
            # Se o elemento atual é maior que o próximo, troca os dois
            if array[j] > array[j + 1]:
                temp = array[j]  # Guarda o valor atual em uma variável temporária
                array[j] = array[j + 1]  # Troca o valor atual com o próximo
                array[j + 1] = temp  # Atribui o valor temporário ao próximo elemento

# Declaração de um array de 15 números
numeros = [34, 10, 24, 76, 54, 12, 33, 47, 67, 89, 23, 45, 67, 12, 9]

# Aplicando o método bubbleSort no array
bubbleSort(numeros)

# Imprimindo o array ordenado
print(numeros)  # Saída: [9, 10, 12, 12, 23, 24, 33, 34, 45, 47, 54, 67, 67, 76, 89]
