nome = [0]*2
senha = [0]*2
tamanho = len(nome)
for i in range(tamanho):
    nome[i] = input("Digite seu nome: ")
    senha[i] = int(input("Digite sua senha: "))
for x in range(tamanho):
    print(f" {nome[x]}, tem a senha {senha[x]}. na posição {x}")





