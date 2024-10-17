def vogais(texto):
    cont = 0
    t = len(texto)
    for i in range(t):
        if texto[i] in "aeiouAEIOU":
            cont +=1
    print(cont)
def somar(*num):
    t = len(num)
    soma = 0
    for i in num:
        soma += i
    print(soma)
def texto(letras):
    t = len(letras)
    cont = 0
    for i in letras:
        if i not in "!@#$%&*":
            cont +=1
        print(cont)
        print(letras[::-1])
def novaLista(num):
    list = []
    for i in 1:
        if i not in list:
            list.append(num)
    print(list)
a = [10, 12, 12, 31, 4, 4, 31, 6, 7, 6, 8]
list(a)
def testPrimo(n):
    for i in range(n):










