import random

def JogoDaForca():

    # Função para escolher uma palavra aleatoriamente
    def escolher_palavra():
        palavras = [("python", "Uma linguagem de programação"),
                    ("cdd4.0", "Melhor curso"),
                    ("ladrão", "Tem muito na cidade de Recife"),
                    ("wellington", "Melhor professor"),
                    ("casa", "Um lugar para relaxar"),
                    ("janga", "Um lugar cheio de árvores e vida selvagem."),
                    ("computador", "Um animal de estimação leal e amigável."),
                    ("onibus", "Um meio de transporte com quatro rodas.")]
        
        palavra, dica = random.choice(palavras)
        return palavra, dica

    # Boneco da forca
    def exibir_forca(erros):
        partes_forca = ["  O", " /|\\", " / \\"]
        print("\n=========== FORCA ===========")
        for i in range(erros):
            if i < len(partes_forca):
                print(partes_forca[i])
        print("=============================\n")
        

    # ocultar letras na hora do jogo
    def ocultar_letras(palavra, letras_certas):
        resultado = ""
        for letra in palavra:
            if letra in letras_certas:
                resultado += letra
            else:
                resultado += "_"
        return resultado

    def jogo_da_forca():
        print("=============================\n"
            "Bem-vindo ao Jogo da Forca!\n"
            "=============================\n")
        
        palavra, dica = escolher_palavra()
        letras_certas = []
        letras_erradas = []
        tentativas = 0
        max_tentativas = 3
        
        print(f"Dica: {dica}")
        palavra_oculta = ocultar_letras(palavra, letras_certas)
        print(f"Palavra: {palavra_oculta}")
        
        while True:
            letra = input("Digite uma letra: ").lower()
            
            if letra in letras_certas:
                print("Você já tentou essa letra.")
                continue

            if letra in letras_erradas:
                print("Você já tentou essa letra e errou.")
                continue
            
            if letra in palavra:
                letras_certas.append(letra)
                palavra_oculta = ocultar_letras(palavra, letras_certas)
                print(f"Palavra: {palavra_oculta}")
                
                if palavra_oculta == palavra:
                    print("\n========================"
                        "Parabéns! Você venceu."
                        "========================")
                    break
            else:
                letras_erradas.append(letra)
                tentativas += 1
                exibir_forca(tentativas)
                
                if tentativas == max_tentativas:
                    print(f"\nFim de jogo! Você perdeu. A palavra era: {palavra}")
                    break


    # Menu para escolher entre 5 palavras diferentes
    while True:
        print("\n=============================\n"
            "JOGO DA FORCA\n"
            "=============================\n")
        escolha = input("Escolha o número da palavra (1 a 5) ou 0 para sair: ")
        
        if escolha == '0':
            break
        elif escolha in "12345":
            jogo_da_forca()
        else:
            print("Escolha inválida. Tente novamente.")
