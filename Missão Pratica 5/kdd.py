import time

def ordenacao_bolha(lista):
    tamanho = len(lista)
    for passo in range(tamanho):
        for indice in range(0, tamanho-passo-1):
            if lista[indice] > lista[indice+1]:
                lista[indice], lista[indice+1] = lista[indice+1], lista[indice]


def ordenacao_selecao(lista):
    tamanho = len(lista)
    for posicao_atual in range(tamanho):
        indice_menor = posicao_atual
        for posicao_comparacao in range(posicao_atual+1, tamanho):
            if lista[posicao_comparacao] < lista[indice_menor]:
                indice_menor = posicao_comparacao
        lista[posicao_atual], lista[indice_menor] = lista[indice_menor], lista[posicao_atual]


palavras = list()
with open("C:\\Users\\Number One\Music\\22 9 3 20 15 18\\Python\Pratica 5\\Missão Pratica 5\\loren.txt", "r") as arquivo:
    for linha in arquivo:
        palavras_da_linha = linha.strip().split()
        palavras.extend(palavras_da_linha)


palavras_para_bolha = palavras.copy()
palavras_para_selecao = palavras.copy()
palavras_para_sort_nativo = palavras.copy()

inicio_bolha = time.time()
ordenacao_bolha(palavras_para_bolha)
fim_bolha = time.time()
tempo_bolha = fim_bolha - inicio_bolha

inicio_selecao = time.time()
ordenacao_selecao(palavras_para_selecao)
fim_selecao = time.time()
tempo_selecao = fim_selecao - inicio_selecao

inicio_sort_nativo = time.time()
palavras_para_sort_nativo.sort()
fim_sort_nativo = time.time()
tempo_sort_nativo = fim_sort_nativo - inicio_sort_nativo

print(f"Tempo de execução da Ordenação Bolha: {tempo_bolha:.6f} segundos")
print(f"Tempo de execução da Ordenação por Seleção: {tempo_selecao:.6f} segundos")
print(f"Tempo de execução do método sort() nativo: {tempo_sort_nativo:.6f} segundos")

def salvar_palavras_ordenadas(nome_arquivo, palavras):
    with open(nome_arquivo, "w") as arquivo:
        for palavra in palavras:
            arquivo.write(palavra + "\n")

salvar_palavras_ordenadas("palavras_ordenadas_bolha.txt", palavras_para_bolha)
salvar_palavras_ordenadas("palavras_ordenadas_selecao.txt", palavras_para_selecao)
salvar_palavras_ordenadas("palavras_ordenadas_nativo.txt", palavras_para_sort_nativo)

print("\nArquivos criados com as palavras ordenadas:")
