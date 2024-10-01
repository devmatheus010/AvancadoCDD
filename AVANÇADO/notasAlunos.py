nota = [" "]*5
tamanho = len(nota)
soma = 0
cont = 0
for i in range(tamanho):
    nota[i] = float(input("Digite a nota: "))
for x in range(tamanho):
    soma = soma + nota[i]
media = soma/tamanho
for n in range(tamanho):
    if nota[n]>media:
        cont += 1
print(f"A média da turma é {media} e {cont} alunos passaram dela")



