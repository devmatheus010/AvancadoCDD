from arquivos.biblioteca2 import *
while True:
    menu = int(input("Selecione uma das opções: "))
    "1. Gravar"
    "2. Mostrar"
    "3. Pesquisar"
    "4. Sair"
    match menu:
        case 1:
             gravarArquivo(input("Digite o texto: "))
        case 2:
            mostrarArquivo()
        case 3:
             pesquisarArquivo(input("Qual nome você quer pesquisar? "))
        case 4:
            print("Saindo...")
            break
        case _:
            print("Opção inválida")





