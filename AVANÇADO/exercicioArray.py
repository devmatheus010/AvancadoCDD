A = [0]*10
M = [0]*10
tamanho = len(A)
cont = 0
resultado = 0
for i in range(tamanho):
    A[i] = int(input("Digite um número: "))
x = int(input("Digite mais o multiplicador: "))
for n in range(tamanho):
    M[n] = A[n]* x
print(f"{A}\n {x}\n {M}")






