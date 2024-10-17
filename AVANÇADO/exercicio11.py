numero = [0]*3
tamanho = len(numero)
cont = 0
for i in range(tamanho):
    numero[i] = int(input("Digite um número: "))
n2 = int(input("Digire outro número: "))
print(numero.count(n2))

