numero = [0]*5
tamanho = len(numero)
for i in range(tamanho):
    numero[i] = int(input("Digite um número: "))
for n in range(4, -1, -1):
    print(numero[n])
