with open("texto.txt", "w") as arquivo:
    texto = list()
    texto.append("arvore")  
    texto.append("vaca")
    texto.append("tesouro")
    texto.append("pirata")
    texto.append("palavra")
    for frase in texto:
        arquivo.write(frase + "\n")

