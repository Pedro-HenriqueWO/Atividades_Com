# ///////////////////////////////////////////////////////////////////////////
# //            PROJETO - CADASTRO ACADEMIA | main.py - Menu               //
# ///////////////////////////////////////////////////////////////////////////
# // Registro de Alterações:                                               //
# // 18/11/2023 | Criação inicial do script.                               //
# // 00/00/0000 |                                                          //
# // 00/00/0000 |                                                          //
# // 00/00/0000 |                                                          //
# ///////////////////////////////////////////////////////////////////////////
# // Desenvolvedores:  Anderson Celso Menzes Diniz Ribeiro                 //
# //                   Kelvyn Luiz Peixoto de Freitas                      //
# //                                                                       //
# //                                                                       //
# ///////////////////////////////////////////////////////////////////////////

from crud import criar_e_inserir_aluno, criar_e_inserir_modalidade, criar_e_inserir_personal, criar_e_inserir_funcionario, acessar_conta_alunos, acessar_conta_modalidade, acessar_conta_personal, acessar_conta_funcionario, deletar_registro_aluno, deletar_registro_modalidade, deletar_registro_personal, deletar_registro_funcionario, sair_banco

while True:
    print("=============================\n"
          "Bem vindo a academia CDD:\n"
           "=============================\n"
           "1. Criar conta\n"
           "2. Acessar contas existentes\n"
           "3. Deletar dados\n"
           "0. Sair\n"
           "=============================\n")

    # repetição se escolher opção errado
    escolha = input("Opção: ")
    while escolha not in ["1", "2", "3", "0"]:
        escolha = input("\nOpção invalida, tente novamente: ")

    # criar conta na academia
    if escolha == "1":

        print("=============================\n"
              "Bem vindo ao cadastro - academia CDD:\n"
              "=============================\n"
              "1. Cadastro alunos\n"
              "2. Cadastro modalidade\n"
              "3. Cadastro funcionarios\n"
              "4. Cadastro Personal\n"
              "0. Voltar ao menu principal\n"
              "=============================\n")
        
        # repetição se escolher opção errado
        escolha = input("Opção: ")
        while escolha not in ["1", "2", "3", "4", "0"]:
            escolha = input("\nOpção invalida, tente novamente: ")

        if escolha == "1":
            criar_e_inserir_aluno()
            print("\nConta aluno criada com sucesso!")

        if escolha == "2":
            criar_e_inserir_modalidade()
            print("\nConta modalidade criada com sucesso!")

        elif escolha == "3":
            criar_e_inserir_funcionario()
            print("\nConta funcionario criada com sucesso!")

        elif escolha == "4":
            criar_e_inserir_personal()
            print("\nConta personal criada com sucesso!")

        elif escolha == "0":
            print("\nVoltando para o menu!")
            break

    # verificar contas existentes
    elif escolha == "2":

        print("=============================\n"
              "Bem vindo ao consultar tabelas - academia CDD:\n"
              "=============================\n"
              "1. Tabela alunos\n"
              "2. Tabela modalidade\n"
              "3. Tabela funcionarios\n"
              "4. Tabela Personal\n"
              "0. Voltar ao menu principal\n"
              "=============================\n")
        
        # repetição se escolher opção errado
        escolha = input("Opção: ")
        while escolha not in ["1", "2", "3", "4", "0"]:
            escolha = input("\nOpção invalida, tente novamente: ")

        if escolha == "1":
            acessar_conta_alunos()

        if escolha == "2":
            acessar_conta_modalidade()

        elif escolha == "3":
            acessar_conta_funcionario()

        elif escolha == "4":
            acessar_conta_personal()

        elif escolha == "0":
            print("\nVoltando para o menu!")
            break

    # Deletar dados
    elif escolha == "3":

        print("=============================\n"
              "Bem vindo ao deletar dados - academia CDD:\n"
              "=============================\n"
              "1. Deletar da tabela alunos\n"
              "2. Deletar da tabela modalidade\n"
              "3. Deletar da tabela funcionarios\n"
              "4. Deletar da tabela Personal\n"
              "0. Voltar ao menu principal\n"
              "=============================\n")
        
        # repetição se escolher opção errado
        escolha = input("Opção: ")
        while escolha not in ["1", "2", "3", "4", "0"]:
            escolha = input("\nOpção invalida, tente novamente: ")

        if escolha == "1":
            deletar_registro_aluno()

        if escolha == "2":
            deletar_registro_modalidade()

        elif escolha == "3":
            deletar_registro_funcionario()

        elif escolha == "4":
            deletar_registro_personal()

        elif escolha == "0":
            print("\nVoltando para o menu!")
            break

    # Sair do programa
    elif escolha == "0":
        sair_banco()
        print("\nEncerrando o programa...")
        break

    else:
        print("\nOpção inválida, tente novamente: ")