from textwrap import dedent
from helpers import *


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
                specific_queries_menu(conn)
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
        option = int(input("Digite qual operação deseja realizar: "))

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
                crud_student(conn, operation)
            case 3:
                crud_subject(conn, operation)
            case 4:
                crud_teacher(conn, operation)
            case 5:
                crud_teacher_subject(conn, operation)
            case 6:
                crud_teacher_dean(conn, operation)
            case 7:
                crud_local(conn, operation)

        break


def specific_queries_menu(conn):
    """
    Menu de Consultas Específicas

    params:
        - conn: conexão com o banco de dados
    """

    while True:
        print(
            dedent(
                """
                    -------------- MENU DE CONSULTAS ESPECÍFICAS ---------------
                    1 - Visualizar a média de cada aluno matriculado em uma turma já concluída 
                    2 - Verificar todas as turmas de determinado semestre
                    3 - Quais locais estão em um dado bloco
                    4 - Visualizar quais turmas estão alocadas em determinado local, mostrando os nomes da turma e da disciplina e os horários de aula
                    5 - Visualizar as médias de um aluno dada a matrícula (Simular a um histórico escolar)
                    6 - Voltar
                """
            )
        )
        option = int(input("Digite qual operação deseja realizar: "))

        match option:
            case 1:
                students_avarage_grade_in_closed_class(conn)
            case 2:
                pass
            case 3:
                get_local_by_bloc(conn)
            case 4:
                pass
            case 5:
                get_school_record_by_student(conn)
            case 6:
                break
            case _:
                print("Opção inválida!\n")
