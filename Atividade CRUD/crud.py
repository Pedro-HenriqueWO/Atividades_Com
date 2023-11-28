# ///////////////////////////////////////////////////////////////////////////
# //         PROJETO - CADASTRO ACADEMIA | crud.py - Biblioteca            //
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

import sqlite3

# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|
# | 19 - INICIO | 139 - FIM | Criação tabelas e inserção de dados.  |
# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|

def criar_e_inserir_aluno():
    banco = sqlite3.connect('banco_alunos.db')

    criar_tabela_alunos = '''
        CREATE TABLE IF NOT EXISTS alunos (
            matricula INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL,
            telefone TEXT,
            email TEXT,
            endereco TEXT NOT NULL
        );
    '''
    banco.execute(criar_tabela_alunos)

    nome = input("Digite o nome do aluno: ")
    cpf = input("Digite o CPF do aluno: ")
    telefone = input("Digite o telefone do aluno: ")
    email = input("Digite o email do aluno: ")
    endereco = input("Digite o endereço do aluno: ")

    inserir_dados_alunos = f'''
        INSERT INTO alunos (nome, cpf, telefone, email, endereco) VALUES
        ('{nome}', '{cpf}', '{telefone}', '{email}', '{endereco}');
    '''
    banco.execute(inserir_dados_alunos)

    banco.commit()
    banco.close()
    print("Dados inseridos com sucesso!")


def criar_e_inserir_modalidade():
    banco = sqlite3.connect('banco_alunos.db')

    criar_tabela_modalidades = '''
        CREATE TABLE IF NOT EXISTS modalidades (
            id_mod INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT
        );
    '''
    banco.execute(criar_tabela_modalidades)

    nome_modalidade = input("Digite o nome da modalidade: ")

    inserir_dados_modalidades = f'''
        INSERT INTO modalidades (nome) VALUES
        ('{nome_modalidade}');
    '''
    banco.execute(inserir_dados_modalidades)

    banco.commit()
    banco.close()
    print("Dados inseridos com sucesso!")

def criar_e_inserir_personal():
    banco = sqlite3.connect('banco_alunos.db')

    criar_tabela_personal = '''
        CREATE TABLE IF NOT EXISTS personal (
            cpf TEXT NOT NULL,
            cref INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL
        );
    '''
    banco.execute(criar_tabela_personal)

    cpf_personal = input("Digite o CPF do personal: ")
    nome_personal = input("Digite o nome do personal: ")
    telefone_personal = input("Digite o telefone do personal: ")
    email_personal = input("Digite o email do personal: ")

    inserir_dados_personal = f'''
        INSERT INTO personal (cpf, nome, telefone, email) VALUES
        ('{cpf_personal}', '{nome_personal}', '{telefone_personal}', '{email_personal}');
    '''
    banco.execute(inserir_dados_personal)

    banco.commit()
    banco.close()
    print("Dados inseridos com sucesso!")

def criar_e_inserir_funcionario():
    banco = sqlite3.connect('banco_alunos.db')

    criar_tabela_funcionario = '''
        CREATE TABLE IF NOT EXISTS funcionario (
            id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL,
            departamento INTEGER NOT NULL,
            cpf_supervisor TEXT NOT NULL,
            salario DECIMAL(8,2)
        );
    '''
    banco.execute(criar_tabela_funcionario)

    nome_funcionario = input("Digite o nome do funcionário: ")
    cpf_funcionario = input("Digite o CPF do funcionário: ")
    departamento = int(input("Digite o departamento do funcionário: "))
    cpf_supervisor = input("Digite o CPF do supervisor: ")
    salario = float(input("Digite o salário do funcionário: "))

    inserir_dados_funcionario = f'''
        INSERT INTO funcionario (nome, cpf, departamento, cpf_supervisor, salario) VALUES
        ('{nome_funcionario}', '{cpf_funcionario}', {departamento}, '{cpf_supervisor}', {salario});
    '''
    banco.execute(inserir_dados_funcionario)

    banco.commit()
    banco.close()
    print("Dados inseridos com sucesso!")

# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|
# | 19 - INICIO | 139 - FIM | Criação tabelas e inserção de dados.  |
# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|


# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|
# | 142 - INICIO | 226 - FIM | Acessar contas existentes.           |
# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|

def acessar_conta_alunos():

    # Conectar ao banco de dados
    banco = sqlite3.connect('banco_alunos.db')

    # Commit para salvar as alterações
    # banco.commit()

    # Consultar dados (Read)
    meucursor = banco.cursor()
    pesquisa = "SELECT matricula, nome, CPF, telefone FROM alunos;"
    meucursor.execute(pesquisa)
    resultado = meucursor.fetchall()

    # Exibir resultados
    for linha in resultado:
        print("======================")
        print("Matrícula:", linha[0])
        print("Nome:", linha[1])
        print("CPF:", linha[2])
        print("Telefone:", linha[3])
        print("======================\n")

def acessar_conta_modalidade():
    banco = sqlite3.connect('banco_alunos.db')
    meucursor = banco.cursor()

    pesquisa = "SELECT id_mod, nome FROM modalidades;"
    meucursor.execute(pesquisa)
    resultado = meucursor.fetchall()

    for linha in resultado:
        print("======================")
        print("ID da Modalidade:", linha[0])
        print("Nome da Modalidade:", linha[1])
        print("======================\n")

    banco.close()

def acessar_conta_personal():
    banco = sqlite3.connect('banco_alunos.db')
    meucursor = banco.cursor()

    pesquisa = "SELECT cpf, cref, nome, telefone, email FROM personal;"
    meucursor.execute(pesquisa)
    resultado = meucursor.fetchall()

    for linha in resultado:
        print("======================")
        print("CPF do Personal:", linha[0])
        print("CREF do Personal:", linha[1])
        print("Nome do Personal:", linha[2])
        print("Telefone do Personal:", linha[3])
        print("Email do Personal:", linha[4])
        print("======================\n")

    banco.close()

def acessar_conta_funcionario():
    banco = sqlite3.connect('banco_alunos.db')
    meucursor = banco.cursor()

    pesquisa = "SELECT id_funcionario, nome, cpf, departamento, cpf_supervisor, salario FROM funcionario;"
    meucursor.execute(pesquisa)
    resultado = meucursor.fetchall()

    for linha in resultado:
        print("======================")
        print("ID do Funcionário:", linha[0])
        print("Nome do Funcionário:", linha[1])
        print("CPF do Funcionário:", linha[2])
        print("Departamento do Funcionário:", linha[3])
        print("CPF do Supervisor:", linha[4])
        print("Salário do Funcionário:", linha[5])
        print("======================\n")

    banco.close()

# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|
# | 142 - INICIO | 226 - FIM | Acessar contas existentes.           |
# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|


# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|
# | 230 - INICIO | 294 - FIM | Deletar registros.                   |
# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|

def deletar_registro_aluno():
    banco = sqlite3.connect('banco_alunos.db')
    meucursor = banco.cursor()

    matricula = int(input("Digite a matrícula do aluno que deseja deletar: "))

    deletar_dados_aluno = f'''
        DELETE FROM alunos WHERE matricula = {matricula};
    '''
    meucursor.execute(deletar_dados_aluno)

    banco.commit()
    banco.close()
    print("Registro deletado com sucesso!")

def deletar_registro_modalidade():
    banco = sqlite3.connect('banco_alunos.db')
    meucursor = banco.cursor()

    id_mod = int(input("Digite o ID da modalidade que deseja deletar: "))

    deletar_dados_modalidade = f'''
        DELETE FROM modalidades WHERE id_mod = {id_mod};
    '''
    meucursor.execute(deletar_dados_modalidade)

    banco.commit()
    banco.close()
    print("Registro deletado com sucesso!")

def deletar_registro_personal():
    banco = sqlite3.connect('banco_alunos.db')
    meucursor = banco.cursor()

    cref = int(input("Digite o CREF do personal que deseja deletar: "))

    deletar_dados_personal = f'''
        DELETE FROM personal WHERE cref = {cref};
    '''
    meucursor.execute(deletar_dados_personal)

    banco.commit()
    banco.close()
    print("Registro deletado com sucesso!")

def deletar_registro_funcionario():
    banco = sqlite3.connect('banco_alunos.db')
    meucursor = banco.cursor()

    id_funcionario = int(input("Digite o ID do funcionário que deseja deletar: "))

    deletar_dados_funcionario = f'''
        DELETE FROM funcionario WHERE id_funcionario = {id_funcionario};
    '''
    meucursor.execute(deletar_dados_funcionario)

    banco.commit()
    banco.close()
    print("Registro deletado com sucesso!")

# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|
# | 230 - INICIO | 294 - FIM | Deletar registros.                   |
# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|



# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|
# | 300 - INICIO | 312 - FIM | Fechar conexão com o banco de dados. |
# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|

def sair_banco():
    # Conectar ao banco de dados
    banco = sqlite3.connect('banco_alunos.db')

    # Fechar a conexão com o banco de dados
    banco.close()

# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|
# | 300 - INICIO | 312 - FIM | Fechar conexão com o banco de dados. |
# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|
