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
                print("Endereço atualizado!\n")

            case 4:  # Deleção
                id_address = int(input("Digite o ID do endereço a ser deletado: "))

                cur.execute(
                    """
                    DELETE FROM Endereço
                    WHERE id_endereço = %s
                    """,
                    (id_address,),
                )

                conn.commit()
                print("Endereço deletado!\n")

        cur.close()
    except Exception as error:
        _treat_exception(conn, error)


def crud_student(conn, operation):
    """
    CRUD de Alunos

    params:
        - conn: conexão com o banco de dados
        - operation: inteiro indicando a operação a ser realizada
    """

    try:
        cur = conn.cursor()

        match operation:
            case 1:  # Inserção
                print("Insira as informações do Aluno\n")
                registration = input("Matrícula: ")
                birthdate = input("Data de nascimento (YYYY-MM-DD): ")
                email = input("Email: ")
                sex = input("Sexo: ")
                name = input("Nome: ")
                id_address = int(input("ID do endereço: "))
                id_curso = int(input("ID do curso: "))

                cur.execute(
                    """
                    INSERT INTO Aluno (matricula, data_nasc, email, sexo, nome, id_endereço, id_curso)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """,
                    (registration, birthdate, email, sex, name, id_address, id_curso),
                )

                conn.commit()
                print("Aluno criado!\n")

            case 2:  # Visualização
                cur.execute("""SELECT * FROM Aluno ORDER BY id_aluno""")
                response = cur.fetchall()

                columns = [
                    "ID",
                    "Matrícula",
                    "Data de Nascimento",
                    "Email",
                    "Sexo",
                    "Nome",
                    "ID_endereço",
                    "ID_curso",
                ]
                print(f"\n{len(response)} Resultados encontrados!\n")
                print(tabulate(response, headers=columns, tablefmt="fancy_grid"))

            case 3:  # Edição
                id_student = int(input("Digite o ID do aluno a ser atualizado: "))

                print("Insira as informações atualizadas do Aluno\n")
                registration = input("Matrícula: ")
                birthdate = input("Data de nascimento (YYYY-MM-DD): ")
                email = input("Email: ")
                sex = input("Sexo: ")
                name = input("Nome: ")
                id_address = int(input("ID do endereço: "))
                id_curso = int(input("ID do curso: "))

                cur.execute(
                    """
                    UPDATE Aluno
                    SET matricula = %s, data_nasc = %s, email = %s, sexo = %s, nome = %s, id_endereço = %s, id_curso = %s
                    WHERE id_aluno = %s
                    """,
                    (
                        registration,
                        birthdate,
                        email,
                        sex,
                        name,
                        id_address,
                        id_curso,
                        id_student,
                    ),
                )

                conn.commit()
                print("Aluno atualizado!\n")

            case 4:  # Deleção
                id_student = int(input("Digite o ID do aluno a ser deletado: "))

                cur.execute(
                    """
                    DELETE FROM Aluno
                    WHERE id_aluno = %s
                    """,
                    (id_student,),
                )

                conn.commit()
                print("Aluno deletado!\n")

        cur.close()
    except Exception as error:
        _treat_exception(conn, error)


def crud_subject(conn, operation):
    """
    CRUD de Disciplinas

    params:
        - conn: conexão com o banco de dados
        - operation: inteiro indicando a operação a ser realizada
    """

    try:
        cur = conn.cursor()

        match operation:
            case 1:  # Inserção
                print("Insira as informações da Disciplina\n")
                name = input("Nome: ")
                workload = input("Carga horária: ")
                course_syllabus = input("Ementa: ")
                cur.execute(
                    """
                    INSERT INTO Disciplina (nome, carga_horária, ementa)
                    VALUES (%s, %s, %s)
                    """,
                    (name, workload, course_syllabus),
                )

                conn.commit()
                print("Disciplina criada!\n")

            case 2:  # Visualização
                cur.execute("""SELECT * FROM Disciplina ORDER BY id_disciplina""")
                response = cur.fetchall()

                columns = ["ID", "Nome", "Carga Horária", "Ementa"]
                print(f"\n{len(response)} Resultados encontrados!\n")
                print(tabulate(response, headers=columns, tablefmt="fancy_grid"))

            case 3:  # Edição
                id_subject = int(input("Digite o ID da Disciplina a ser atualizada: "))

                print("Insira as informações atualizadas da Disciplina\n")
                name = input("Nome: ")
                workload = input("Carga horária: ")
                course_syllabus = input("Ementa: ")
                cur.execute(
                    """
                    UPDATE Disciplina
                    SET nome = %s, carga_horária = %s, ementa = %s
                    WHERE id_disciplina = %s
                    """,
                    (name, workload, course_syllabus, id_subject),
                )

                conn.commit()
                print("Disciplina atualizada!\n")

            case 4:  # Deleção
                id_subject = int(input("Digite o ID da Disciplina a ser deletada: "))

                cur.execute(
                    """
                    DELETE FROM Disciplina
                    WHERE id_disciplina = %s
                    """,
                    (id_subject,),
                )

                conn.commit()
                print("Disciplina deletada!\n")

        cur.close()
    except Exception as error:
        _treat_exception(conn, error)


def crud_teacher(conn, operation):
    """
    CRUD de Professores

    params:
        - conn: conexão com o banco de dados
        - operation: inteiro indicando a operação a ser realizada
    """

    try:
        cur = conn.cursor()

        match operation:
            case 1:  # Inserção
                print("Insira as informações do Professor\n")
                birthdate = input("Data de Nascimento (YYYY-MM-DD): ")
                name = input("Nome: ")
                formation = input("Formação: ")
                email = input("Email: ")
                sex = input("Sexo: ")

                cur.execute(
                    """
                    INSERT INTO Professor (data_nasc, nome, formação, email, sexo)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (birthdate, name, formation, email, se),
                )

                conn.commit()
                print("Professor criado!\n")

            case 2:  # Visualização
                cur.execute("""SELECT * FROM Professor ORDER BY id_profs""")
                response = cur.fetchall()

                columns = [
                    "ID",
                    "Data de Nascimento",
                    "Nome",
                    "Formação",
                    "Email",
                    "Sexo",
                    "ID Curso",
                ]
                print(f"\n{len(response)} Resultados encontrados!\n")
                print(tabulate(response, headers=columns, tablefmt="fancy_grid"))

            case 3:  # Edição
                id_profs = int(input("Digite o ID do professor a ser atualizado: "))

                print("Insira as informações atualizadas do Professor\n")
                birthdate = input("Data de Nascimento (YYYY-MM-DD): ")
                name = input("Nome: ")
                formation = input("Formação: ")
                email = input("Email: ")
                sex = input("Sexo: ")
                id_course = input("ID do curso: ")

                cur.execute(
                    """
                    UPDATE Professor
                    SET data_nasc = %s, nome = %s, formação = %s, email= %s, sexo=%s, id_curso = %s
                    WHERE id_profs = %s
                    """,
                    (birthdate, name, formation, email, sex, id_course, id_profs),
                )

                conn.commit()
                print("Professor atualizado!\n")

            case 4:  # Deleção
                id_profs = int(input("Digite o ID do Professor a ser deletado: "))

                cur.execute(
                    """
                    DELETE FROM Professor
                    WHERE id_profs = %s
                    """,
                    (id_profs,),
                )

                conn.commit()
                print("Professor deletado!\n")

        cur.close()
    except Exception as error:
        _treat_exception(conn, error)


def crud_teacher_subject(conn, operation):
    """
    CRUD de Professor_Disciplina

    params:
        - conn: conexão com o banco de dados
        - operation: inteiro indicando a operação a ser realizada
    """

    try:
        cur = conn.cursor()

        match operation:
            case 1:  # Inserção
                print("Insira as informações necessárias:\n")
                id_teacher = int(input("ID do professor: "))
                id_subject = int(input("ID da disciplina: "))

                cur.execute(
                    """
                    INSERT INTO Professor_Disciplina (id_profs, id_disciplina)
                    VALUES (%s, %s)
                    """,
                    (id_teacher, id_subject),
                )

                conn.commit()
                print("Relação Professor-Disciplina criada!\n")

            case 2:  # Visualização
                cur.execute("""SELECT * FROM Professor_Disciplina ORDER BY id_profs""")
                response = cur.fetchall()

                columns = ["ID Professor", "ID Disciplina"]
                print(f"\n{len(response)} Resultados encontrados!\n")
                print(tabulate(response, headers=columns, tablefmt="fancy_grid"))

            case 3:  # Edição
                print("Insira as informações atuais da relação Professor-Disciplina\n")
                id_teacher = int(input("ID do professor: "))
                id_subject = int(input("ID da disciplina: "))

                print(
                    "Insira as informações atualizadas da relação Professor-Disciplina\n"
                )
                new_id_teacher = int(input("ID atualizado do professor: "))
                new_id_subject = int(input("ID atualizado da disciplina: "))

                cur.execute(
                    """
                    UPDATE Professor_Disciplina (id_profs, id_disciplina)
                    SET id_profs = %s, id_disciplina = %s
                    WHERE id_profs = %s AND id_disciplina = %s
                    """,
                    (new_id_teacher, new_id_subject, id_teacher, id_subject),
                )

                conn.commit()
                print("Relação Professor_Disciplina atualizada!\n")

            case 4:  # Deleção
                print("Insira os identificadores da relação Professor-Disciplina\n")
                id_teacher = int(input("ID do professor: "))
                id_subject = int(input("ID da disciplina: "))

                cur.execute(
                    """
                    DELETE FROM Professor_Disciplina
                    WHERE id_profs = %s AND id_disciplina = %s
                    """,
                    (id_teacher, id_subject),
                )

                conn.commit()
                print("Relação Professor_Disciplina deletada!\n")

        cur.close()
    except Exception as error:
        _treat_exception(conn, error)


def crud_teacher_dean(conn, operation):
    """
    CRUD de Reitor

    params:
        - conn: conexão com o banco de dados
        - operation: inteiro indicando a operação a ser realizada
    """

    try:
        cur = conn.cursor()

        match operation:
            case 1:  # Inserção
                print("Insira as informações do Reitor\n")
                dean_code = input("Código do Reitor: ")
                id_teacher = input("ID do professor: ")
                admission_date = input("Data de admissão (YYYY-MM-DD): ")
                cur.execute(
                    """
                    INSERT INTO Professor_Reitor (código_reitor, id_profs, data_admissão)
                    VALUES (%s, %s, %s)
                    """,
                    (dean_code, id_teacher, admission_date),
                )

                conn.commit()
                print("Reitor criado!\n")

            case 2:  # Visualização
                cur.execute("""SELECT * FROM Professor_Reitor ORDER BY data_admissão""")
                response = cur.fetchall()

                columns = ["Código de Reitor", "ID Professor", "Data de Admissão"]
                print(f"\n{len(response)} Resultados encontrados!\n")
                print(tabulate(response, headers=columns, tablefmt="fancy_grid"))

            case 3:  # Edição
                dean_code = int(input("Digite o código do reitor a ser atualizado: "))

                print("Insira as informações atualizadas do Reitor\n")
                dean_code = input("Código do Reitor: ")
                id_teacher = input("ID do professor: ")
                admission_date = input("Data de admissão (YYYY-MM-DD): ")

                cur.execute(
                    """
                    UPDATE Professor_Reitor
                    SET código_reitor = %s, id_profs = %s, data_admissão = %s
                    WHERE código_reitor = %s
                    """,
                    (dean_code, id_teacher, admission_date, dean_code),
                )

                conn.commit()
                print("Professor atualizado!\n")

            case 4:  # Deleção
                dean_code = int(input("Digite o código do Reitor a ser deletado: "))

                cur.execute(
                    """
                    DELETE FROM Professor_Reitor
                    WHERE código_reitor = %s
                    """,
                    (dean_code,),
                )

                conn.commit()
                print("Reitor deletado!\n")

        cur.close()
    except Exception as error:
        _treat_exception(conn, error)


def crud_local(conn, operation):
    """
    CRUD de Local

    params:
        - conn: conexão com o banco de dados
        - operation: inteiro indicando a operação a ser realizada
    """

    try:
        cur = conn.cursor()

        match operation:
            case 1:  # Inserção
                local_types = {
                    1: "Sala",
                    2: "Laboratório",
                    3: "Auditório",
                    4: "Biblioteca",
                    5: "Bloco",
                }

                while True:
                    print(
                        dedent(
                            """
                                Opções de Locais disponíveis para criação:
                                1 - Sala
                                2 - Laboratório
                                3 - Auditório
                                4 - Biblioteca 
                                5 - Bloco
                            """
                        )
                    )
                    local_type = int(input("Qual tipo de local deseja criar? "))
                    if local_type >= 1 and local_type <= 5:
                        break

                print("Insira as informações do Local\n")
                name = input("Nome do local:")
                max_people = int(input("Lotação: "))
                description = input("Descrição: ")
                id_center = input("ID do centro: ")
                id_bloco = input("ID do bloco: ") if local_type != 5 else None

                cur.execute(
                    """
                    INSERT INTO Local (nome, lotação, descrição, id_centro, id_bloco, tipo_local)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    RETURNING id_local
                    """,
                    (
                        name,
                        max_people,
                        description,
                        id_center,
                        id_bloco,
                        local_types[local_type],
                    ),
                )

                id_local = cur.fetchone()

                match local_type:
                    case 1:  # Sala
                        cur.execute(
                            """
                            INSERT INTO Local_Sala (id_local)
                            VALUES (%s)
                            """,
                            (id_local),
                        )
                    case 2:  # Laboratório
                        cur.execute(
                            """
                            INSERT INTO Local_Laboratório
                            VALUES (%s)
                            """,
                            (id_local),
                        )
                    case 3:  # Auditório
                        cur.execute(
                            """
                            INSERT INTO Local_Auditório
                            VALUES (%s)
                            """,
                            (id_local),
                        )
                    case 4:  # Biblioteca
                        cur.execute(
                            """
                            INSERT INTO Local_Biblioteca
                            VALUES (%s)
                            """,
                            (id_local),
                        )
                    case 5:  # Bloco
                        cur.execute(
                            """
                            INSERT INTO Local_Bloco
                            VALUES (%s)
                            """,
                            (id_local),
                        )

                conn.commit()
                print("Local criado!\n")

            case 2:  # Visualização
                cur.execute("""SELECT * FROM Local ORDER BY id_local""")
                response = cur.fetchall()

                columns = [
                    "ID",
                    "Nome",
                    "Lotação",
                    "Descrição",
                    "Tipo do Local",
                    "ID Centro",
                    "ID Bloco",
                ]
                print(f"\n{len(response)} Resultados encontrados!\n")
                print(tabulate(response, headers=columns, tablefmt="fancy_grid"))

            case 3:  # Edição
                id_local = int(input("Digite o código do local a ser atualizado: "))

                print("Insira as informações atualizadas do Local\n")
                name = input("Nome do local:")
                max_people = int(input("Lotação: "))
                description = input("Descrição: ")
                id_center = input("ID do centro: ")
                id_bloco = input("ID do bloco: ") if local_type != 5 else None

                cur.execute(
                    """
                    UPDATE Local
                    SET name = %s, max_people = %s, description = %s, id_center = %s, id_bloco = %s
                    WHERE id_local = %s
                    """,
                    (name, max_people, description, id_center, id_bloco, id_local),
                )

                conn.commit()
                print("Local atualizado!\n")

            case 4:  # Deleção
                id_local = int(input("Digite o ID do Local a ser deletado: "))

                cur.execute(
                    """
                    DELETE FROM Local
                    WHERE id_local = %s
                    """,
                    (id_local,),
                )

                conn.commit()
                print("Local deletado!\n")

        cur.close()
    except Exception as error:
        _treat_exception(conn, error)


def students_avarage_grade_in_closed_class(conn):
    """
    Visualizar média de cada aluno matriculado em uma turma já concluída

    params:
        - conn: conexão com o banco de dados
    """

    class_id = int(input("ID da turma: "))

    try:
        cur = conn.cursor()

        cur.execute("""SELECT estado FROM Turma WHERE id_turma = (%s);""", (class_id,))
        class_status = cur.fetchone()[0]

        if class_status == "ABERTA":
            print("Turma deve estar concluída!\n")
            return

        cur.execute(
            """
            SELECT A.id_aluno, A.nome, A.matricula, AVG(AV.nota)
            FROM Turma T
            JOIN Turma_Aluno TA
            ON TA.id_turma = T.id_turma
            JOIN Aluno A
            ON TA.id_aluno = A.id_aluno
            JOIN Avaliação AV
            ON AV.id_aluno = A.id_aluno AND AV.id_turma = T.id_turma
            WHERE T.id_turma = 1
            GROUP BY (A.id_aluno);
            """
        )

        response = cur.fetchall()

        columns = ["ID Aluno", "Nome", "Matrícula", "Média"]
        print(f"\n{len(response)} Resultados encontrados!\n")
        print(tabulate(response, headers=columns, tablefmt="fancy_grid"))

        cur.close()
    except Exception as error:
        _treat_exception(conn, error)


def get_local_by_bloc(conn):
    """
    Visualizar locais por determinado bloco

    params:
        - conn: conexão com o banco de dados
    """

    bloc_id = int(input("ID do bloco: "))

    try:
        cur = conn.cursor()

        cur.execute(
            """SELECT id_local, nome FROM local WHERE id_bloco = (%s);""", (bloc_id,)
        )
        response = cur.fetchall()

        columns = ["ID Local", "Nome"]
        print(f"\n{len(response)} Resultados encontrados!\n")
        print(tabulate(response, headers=columns, tablefmt="fancy_grid"))

        cur.close()
    except Exception as error:
        _treat_exception(conn, error)


def get_school_record_by_student(conn):
    """
    Visualizar histórico escolar por aluno

    params:
        - conn: conexão com o banco de dados
    """

    student_id = int(input("ID do aluno: "))

    try:
        cur = conn.cursor()

        cur.execute(
            """SELECT D.nome, AVG(AV.nota)
            FROM Aluno A
            JOIN Turma_Aluno TA
            ON TA.id_aluno = A.id_aluno
            JOIN Turma T
            ON TA.id_turma = T.id_turma
            JOIN Avaliação AV
            ON AV.id_turma = T.id_turma AND AV.id_aluno = A.id_aluno
            JOIN Disciplina D
            ON D.id_disciplina = T.id_disciplina
            WHERE A.id_aluno =  (%s)
            GROUP BY (D.nome);
            """,
            (student_id,),
        )
        response = cur.fetchall()

        columns = ["Nome da Disciplina", "Média"]
        print(f"\n{len(response)} Resultados encontrados!\n")
        print(tabulate(response, headers=columns, tablefmt="fancy_grid"))

        cur.close()
    except Exception as error:
        _treat_exception(conn, error)
