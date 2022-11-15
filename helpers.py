from textwrap import dedent
from tabulate import tabulate


def _treat_exception(conn, error):
    """
    Tratar exceção gerada ao tentar realizar um commit no banco de dados

    params:
        - conn: conexão com o banco de dados
        - error: erro gerado
    """

    print(f"Problema ao realizar operação!\n{error}\n")
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
                print("Insira as informações do Endereço\n")
                street = input("Rua: ")
                number = input("Número: ")
                complement = input("Complemento: ")
                cep = input("Cep: ")
                state = input("Estado: ")
                city = input("Cidade: ")

                cur.execute(
                    """
                    INSERT INTO Endereço (rua, número, complemento, cep, estado, cidade)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """,
                    (street, number, complement, cep, state, city),
                )

                conn.commit()
                print(f"Endereço criado!\n")

            case 2:  # Visualização
                cur.execute("""SELECT * FROM Endereço ORDER BY id_endereço""")
                response = cur.fetchall()

                columns = [
                    "ID",
                    "Rua",
                    "Número",
                    "Complemento",
                    "CEP",
                    "Estado",
                    "Cidade",
                ]
                print(f"\n{len(response)} Resultados encontrados!\n")
                print(tabulate(response, headers=columns, tablefmt="fancy_grid"))

            case 3:  # Edição
                id_address = int(input("Digite o ID do endereço a ser atualizado: "))

                print("Insira as informações editadas do endereço\n")
                street = input("Rua: ")
                number = input("Número: ")
                complement = input("Complemento: ")
                cep = input("Cep: ")
                state = input("Estado: ")
                city = input("Cidade: ")

                cur.execute(
                    """
                    UPDATE Endereço 
                    SET rua = %s , número = %s, complemento = %s, cep = %s, estado = %s, cidade = %s
                    WHERE id_endereço = %s
                    """,
                    (street, number, complement, cep, state, city, id_address),
                )

                conn.commit()
                print(f"Endereço atualizado!\n")

            case 4:  # Deleção
                pass

        cur.close()
    except Exception as error:
        _treat_exception(conn, error)
