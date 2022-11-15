from textwrap import dedent


def _treat_exception(conn, error):
    """
    Tratar exceção gerada ao tentar realizar um commit no banco de dados

    params:
        - conn: conexão com o banco de dados
        - error: erro gerado
    """

    print(f"Problema ao realizar operação no banco de dados!\n{error}\n")
    if conn is not None:
        conn.close()
    print("Banco de dados desconectado!")
    exit(1)


def reset_database(conn):
    """
    Resetar banco de dados

    params:
        - conn: conexão com o banco de dados
    """

    while True:
        option = int(
            input(
                dedent(
                    """
                    Deseja popular o banco de dados?
                    1 - SIM
                    2 - NÃO
                    """
                )
            )
        )

        match option:
            case 1:
                populate = True
                break
            case 2:
                populate = False
                break
            case _:
                print("Opção inválida\n")

    # Utiliza os arquivos sql para criar o banco de dados e populá-lo
    with open("sql/create_database.sql", "r", encoding="utf8") as create_database, open(
        "sql/seed_database.sql", "r", encoding="utf8"
    ) as seed_database:
        try:
            cur = conn.cursor()

            cur.execute(create_database.read())

            if populate:
                cur.execute(seed_database.read())

            conn.commit()
            cur.close()

        except Exception as error:
            _treat_exception(conn, error)


def crud_address(conn, operation):
    """
    CRUD de Endereço

    params:
        - conn: conexão com o banco de dados
        - operation: inteiro indicando a operação a ser realizada
    """

    try:
        cur = conn.cursor()

        match operation:
            case 1:  # Inserção
                pass
            case 2:  # Visualização
                pass
            case 3:  # Visualização
                pass
            case 4:  # Visualização
                pass

        cur.close()
    except Exception as error:
        _treat_exception(conn, error)
