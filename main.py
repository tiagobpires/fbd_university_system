import os

import psycopg2
from dotenv import load_dotenv

from menus import menu_principal

load_dotenv()


if __name__ == "__main__":

    try:
        conn = psycopg2.connect(
            host="200.129.44.249",
            database=os.environ.get("DATABASE"),
            user=os.environ.get("USER_DB"),
            password=os.environ.get("PASSWORD_DB"),
        )
    except Exception as error:
        print(f"Problema ao se conectar com o banco de dados!\n{error}")
        exit(1)

    menu_principal(conn)
