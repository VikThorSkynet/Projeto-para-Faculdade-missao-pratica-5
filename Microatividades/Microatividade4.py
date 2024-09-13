with open("loremipsum.txt", "r") as arquivo:
    conteudo = arquivo.readline()
    print(conteudo[:3])