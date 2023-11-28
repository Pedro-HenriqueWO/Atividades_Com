from Biblioteca import JogoDaForca

verificador = "s"
while verificador in "sS":

    print("\n\n=== JOGO DA FORCA ===\n"
    "1  - Jogar \n"
    "=====================\n"
    "0 - Encerrar Jogo\n"
    "=====================\n")
    ops = input("Escolha uma opção: ")
    while ops not in "10":
        ops = input("Opção invalida, tente novamente...\n"
                    "Escolha uma opção acima: ")
        
    if ops == "1":
        JogoDaForca()

    elif ops in "0":
        verificador = "0"
        print("\nFinalizando o Jogo...")

    else:
        print("\n inválidd, tente novamente.\n")