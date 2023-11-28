def escolher_opcao_jogo():
    opc = input("Escolha entre pedra, papel ou tesoura: ")
    while opc not in ["pedra", "papel", "tesoura"]:
        opc = input("Erro - Escolha somente entre: pedra, papel ou tesoura: ")
    return opc

# Variáveis de jogadores e placar
jogador1 = input("Digite o nome do 1º jogador: ")
jogador2 = input("Digite o nome do 2º jogador: ")
placar1 = 0
placar2 = 0

# Quantidade de partidas
quantidade = int(input("Melhor de quantas? (Escolha um numero ímpar): "))
while quantidade % 2 == 0:
    quantidade = int(input("Erro - Quantidade de partidas deve ser um número ímpar. (Escolha um numero ímpar): "))

# Verificador se deseja jogar novamente
verificador = "s"
while verificador.lower() == "s":

    print("==========================\n"
          f" {jogador1} X {jogador2}  \n"
          f" {placar1} placar {placar2}  \n"
          f" Melhor de {quantidade}  \n"
          "==========================\n"
          "= 1 - Jogar              =\n"
          "= 2 - Trocar nomes       =\n"
          "= 3 - Melhor de quantas  =\n"
          "==========================\n"
          "= 0 - Encerrar Programa  =\n"
          "==========================\n")
    ops = int(input("\nEscolha uma opção: "))
    while ops not in [0, 1, 2, 3]:
        ops = int(input("\nErro - Escolha uma opção (entre 1, 2, 3 ou 0): "))
    print("")

    if ops == 3:
        # Quantidade de partidas
        quantidade = int(input("Melhor de quantas? (Escolha um numero ímpar): "))
        while quantidade % 2 == 0:
            quantidade = int(input("Erro - Quantidade de partidas deve ser um número ímpar. (Escolha um numero ímpar): "))

    # Trocar nomes
    elif ops == 2:
        print("=========================\n"
              "1 - Trocar nome do jogador 1 \n"
              "2 - Trocar nome do jogador 2 \n"
              "=========================\n"
              "0 - Voltar 2 \n"
              "=========================\n")
        ops2 = int(input("\nEscolha uma opção: "))
        while ops2 not in [0, 1, 2]:
            ops2 = int(input("\nEscolha uma opção: "))

        if ops2 == 1:
            jogador1 = input("Digite o nome do 1º jogador: ")
        elif ops2 == 2:
            jogador2 = input("Digite o nome do 2º jogador: ")

    # Jogar
    elif ops == 1:
        # Escolher quem será o primeiro jogador
        primeiro = int(input("Quem será o primeiro jogador? (1 para o primeiro jogador ou 2 para o segundo jogador): "))
        while primeiro not in [1, 2]:
            primeiro = int(input("Erro - Escolha 1 para o primeiro jogador ou 2 para o segundo jogador: "))

        # Variável e seleção das opções dos jogadores, quantidade de jogos e placar
        opc1 = ""
        opc2 = ""
        quantidade1 = quantidade  # Para não alterar a quantidade de jogos original

        while quantidade1 != 0:
            # Primeiro jogador selecionado anteriormente escolhe entre pedra, papel ou tesoura
            if primeiro == 1:
                opc1 = escolher_opcao_jogo()
                opc2 = escolher_opcao_jogo()
            # Segundo jogador escolhe entre pedra, papel ou tesoura
            else:
                opc2 = escolher_opcao_jogo()
                opc1 = escolher_opcao_jogo()

            # Condição de vitória, empate e derrota
            if opc1 == opc2:
                print(f"\nEmpate, jogador {jogador1} escolheu {opc1} e jogador {jogador2} escolheu {opc2}.")
                quantidade1 = 0
            elif (opc1 == "pedra" and opc2 == "tesoura") or (opc1 == "papel" and opc2 == "pedra") or (
                    opc1 == "tesoura" and opc2 == "papel"):
                quantidade1 -= 1
                print(f"\nJogador {jogador1} venceu, {opc1} ganha de {opc2}.\n"
                      f"Jogos restantes: {quantidade1}")
                placar1 += 1
            else:
                quantidade1 -= 1
                print(f"\nJogador {jogador2} venceu, {opc2} ganha de {opc1} \n."
                      f"Jogos restantes: {quantidade1}")
                placar2 += 1

            print("\n==========================\n"
                  f" {jogador1} X {jogador2}  \n"
                  f" {placar1} placar {placar2}\n"
                  f" Melhor de {quantidade}  \n"
                  f"Jogos restantes: {quantidade1}\n"
                  "==========================\n")

        if placar1 > placar2:
            print(f"O jogador {jogador1} ganhou de {placar1} a {placar2}")
        elif placar2 > placar1:
            print(f"O jogador {jogador2} ganhou de {placar2
