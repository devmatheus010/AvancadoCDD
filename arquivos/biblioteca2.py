def gravarArquivo(nome):
    with open("Nomes.txt", "a") as arquivo:
        arquivo.write(f"{nome}\n")

def mostrarArquivo():
    with open("Nomes.txt", "r") as arquivo2:
        print(arquivo2.read())

def pesquisarArquivo(texto):
    cont = 0
    with open("Nomes.txt", "r") as pesq:
        for texto in pesq:
            cont+=1
        print(f"Achei {cont} ocorrência de {texto} no arquivo")


