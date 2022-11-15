import os

import psycopg2
from dotenv import load_dotenv
from textwrap import dedent

load_dotenv()


if __name__ == "__main__":

    try:
        conn = psycopg2.connect(
            host="200.129.44.249",
            database=os.environ.get("DATABASE"),
            user=os.environ.get("USER_DB"),
            password=os.environ.get("PASSWORD_DB"),
        )
    except Exception:
        print("Problema ao se conectar com o banco de dados!\n")
        exit(1)

    while True:
        print(
            dedent(
                """
                    -------------- MENU PRINCIPAL ---------------
                    1 - Resetar banco de dados
                    12 - Encerrar Aplicação
                """
            )
        )
        option = int(input("Digite qual operação deseja realizar: "))

        match option:
            case 1:
                pass
            case 12:
                conn.close()
                print("\nBanco de Dados desconectado!\n")
                exit(1)
            case _:
                print("Opção inválida!\n")
