from textwrap import dedent
from helpers import reset_database, crud_address


def menu_principal(conn):
    """
    Menu Principal

    params:
        - conn: conexão com o banco de dados
    """

    while True:
        print(
            dedent(
                """
                    -------------- MENU PRINCIPAL ---------------
                    1 - Resetar banco de dados
                    2 - CRUDs
                    3 - Consultas específicas
                    4 - Encerrar Aplicação
                """
            )
        )
        option = int(input("Digite qual operação deseja realizar: "))

        match option:
            case 1:
                reset_database(conn)
            case 2:
                menu_crud(conn)
            case 3:
                pass
            case 4:
                conn.close()
                print("\nBanco de Dados desconectado!\n")
                exit(1)
            case _:
                print("Opção inválida!\n")


def submenu_crud():
    """
    Submenu de CRUD

    Retorno:
        - Inteiro indicando a operação a ser realizada
        - None se nenhuma operação foi solicitada
    """

    print(
        dedent(
            """
                Operações disponíveis na tabela:
                1 - INSERIR
                2 - VISUALIZAR
                3 - ATUALIZAR
                4 - DELETAR
                OBS: aperte 5 para voltar
            """
        )
    )

    while True:
        option = int(
            input("Digite em qual entidade deseja realizar as operações do CRUD: ")
        )

        if option <= 1 and option >= 5:
            print("Opção inválida!\n")
            continue

        return option if option != 5 else None


def menu_crud(conn):
    """
    Menu de CRUDs

    params:
        - conn: conexão com o banco de dados
    """

    print(
        dedent(
            """
                -------------- MENU CRUD ---------------
                Entidades disponíveis:
                1 - ENDEREÇO  
                2 - ALUNO 
                3 - DISCIPLINA
                4 - PROFESSOR 
                5 - PROFESSOR_DISCIPLINA 
                6 - PROFESSOR_REITOR  
                7 - LOCAL 
                8 - HORÁRIO
                9 - TURMA
                10 - TURMA_HORÁRIO
                11 - TURMA_ALUNO
                12 - AVALIAÇÃO
                13 - MUNICÍPIO
                14 - CAMPUS
                15 - CENTRO
                16 - CURSO
                OBS: Aperte 17 para voltar
            """
        )
    )

    while True:
        option = int(
            input("Digite em qual entidade deseja realizar as operações do CRUD: ")
        )

        if option <= 1 and option >= 17:
            print("Opção inválida!\n")
            continue
        elif option == 17:
            break

        operation = submenu_crud()

        if operation is None:
            break

        match option:
            case 1:
                crud_address(conn, operation)
            case 2:
                pass