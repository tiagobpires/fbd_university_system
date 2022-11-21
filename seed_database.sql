
INSERT INTO 
Professor(data_nasc, nome, formação, email, sexo)
VALUES ('1960-05-06', 'Javam de Castro Machado', 'Doutor', 'javamcastro@ufc.br', 'Masculino');

INSERT INTO 
Professor(data_nasc, nome, formação, email, sexo)
VALUES ('1976-04-06', 'Rudini Sampaio', 'Doutor', 'rundinisampio@ufc.br', 'Masculino');

INSERT INTO 
Professor(data_nasc, nome, formação, email, sexo)
VALUES ('1980-02-16', 'Rossana Maria de Castro Andrade', 'Doutora', 'rossana@ufc.br', 'Feminino');

INSERT INTO 
Professor(data_nasc, nome, formação, email, sexo)
VALUES ('1941-02-07', 'Leslie Lamport', 'Doutor', 'lamport@ufc.br', 'Masculino');

INSERT INTO 
Professor(data_nasc, nome, formação, email, sexo)
VALUES ('1941-02-07', 'Leslie Lamport', 'Doutor', 'lamport@ufc.br', 'Masculino');


INSERT INTO 
Disciplina(nome, carga_horária, ementa)
VALUES ('Fundamento de Banco de Dados', '96', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.');

INSERT INTO 
Disciplina(nome, carga_horária, ementa)
VALUES ('Linguagens de Programação','72','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum');

INSERT INTO 
Disciplina(nome, carga_horária, ementa)
VALUES ('Compiladores','72','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum');


INSERT INTO 
Disciplina(nome, carga_horária, ementa)
VALUES ('Engenharia de Software I', '64', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.');

INSERT INTO 
Disciplina(nome, carga_horária, ementa)
VALUES ('Qualidade de Software', '64', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.');

INSERT INTO 
Disciplina(nome, carga_horária, ementa)
VALUES ('Segurança de Redes', '96', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.');



INSERT INTO 
Professor_Disciplina(id_profs, id_disciplina)
VALUES (1, 1);

INSERT INTO 
Professor_Disciplina(id_profs, id_disciplina)
VALUES (3, 4);

INSERT INTO 
Professor_Disciplina(id_profs, id_disciplina)
VALUES (3, 5);

INSERT INTO 
Professor_Disciplina(id_profs, id_disciplina)
VALUES (4,3);

INSERT INTO 
Professor_Disciplina(id_profs, id_disciplina)
VALUES (4,5);

INSERT INTO 
Professor_Disciplina(id_profs, id_disciplina)
VALUES (4, 1);


INSERT INTO 
Professor_Reitor(código_reitor, id_profs, data_admissão)
VALUES (007, 4, '1990-10-02');


INSERT INTO 
Município(nome)
VALUES ('Fortaleza');


INSERT INTO 
Campus (nome, id_município, id_reitor)
VALUES ('Pici', 1, 007);

INSERT INTO 
Campus (nome, id_município, id_reitor)
VALUES ('Benfica', 1, 007);

INSERT INTO 
Campus (nome, id_município, id_reitor)
VALUES ('Porangabussu', 1, 007);


INSERT INTO 
Centro (nome, id_profs, id_campus)
VALUES ('Ciências', 1, 1);

INSERT INTO 
Centro (nome, id_profs, id_campus)
VALUES ('Tecnologia', 2, 1);


INSERT INTO 
Curso (nome, carga_horaria, id_profs, id_centro)
VALUES ('Computação', 3200, 3, 1);

INSERT INTO 
Curso (nome, carga_horaria, id_profs, id_centro)
VALUES ('Biotecnologia', 3200, 4, 1);


INSERT INTO 
Endereço (rua, número, complemento, cep, estado, cidade)
VALUES  ('Rua 810', '542', 'Em frente à praça', '60811-530', 'CE', 'Fortaleza');

INSERT INTO 
Endereço (rua, número, complemento, cep, estado, cidade)
VALUES  ('Rua Vila Medeiros', '242', 'Em frente ao supermercado', '60015-130', 'CE', 'Fortaleza');

INSERT INTO 
Endereço (rua, número, complemento, cep, estado, cidade)
VALUES  ('Rua Primeiro de Maio', '958', 'Em frente ao supermercado', '60540-455', 'CE', 'Fortaleza');

INSERT INTO 
Endereço (rua, número, complemento, cep, estado, cidade)
VALUES  ('Rua Segundo de Maio', '957', 'Em frente ao supermercado', '60540-435', 'CE', 'Fortaleza');

INSERT INTO 
Endereço (rua, número, complemento, cep, estado, cidade)
VALUES  ('Rua Terceiro de Maio', '952', 'Em frente ao supermercado', '60540-453', 'CE', 'Fortaleza');



INSERT INTO 
Aluno (matricula, data_nasc, email, sexo, nome, id_endereço, id_curso)
VALUES ('49342', '2001-10-30', 'philip@alu.ufc.com', 'Masculino', 'Philip Moreira Silva', 1, 1);

INSERT INTO 
Aluno (matricula, data_nasc, email, sexo, nome, id_endereço, id_curso)
VALUES ('54123', '2002-10-12', 'joana@ufc,br', 'Feminino',  'Joana', 2, 1);

INSERT INTO 
Aluno (matricula, data_nasc, email, sexo, nome, id_endereço, id_curso)
VALUES ('54523', '1998-08-14', 'jason@ufc,br', 'Masculino',  'Jason', 3, 2);

INSERT INTO 
Aluno (matricula, data_nasc, email, sexo, nome, id_endereço, id_curso)
VALUES ('64231', '2003-10-02', 'martin@ufc.com', 'Masculino', 'Martin Aeroporto', 4, 1);

INSERT INTO 
Aluno (matricula, data_nasc, email, sexo, nome, id_endereço, id_curso)
VALUES ('52040', '2001-10-22', 'tiagobpires@ufc.br', 'Masculino', 'Tiago Barros Pires', 5, 1);



INSERT INTO local(
	nome, "lotação", "descrição", id_centro, tipo_local)
	VALUES ('Bloco 910', 1200, 'Bloco para alunos de ciências e engenharia da computação', 1, 'Bloco');

INSERT INTO local_bloco(
	id_local)
	VALUES (1);

INSERT INTO local(
	nome, "lotação", "descrição", id_centro, id_bloco, tipo_local)
	VALUES ('Auditório de ciências', 200, 'Auditório do bloco 910', 1, 1, 'Auditório');

INSERT INTO local_auditório(id_local)
	VALUES (2);

INSERT INTO local(
	nome, "lotação", "descrição", id_centro, id_bloco, tipo_local)
	VALUES ('LEC 1', 40, 'Laboratório de Ciências da Computação 1', 1, 1, 'Laboratório');

INSERT INTO local_laboratório(id_local)
	VALUES (3);

INSERT INTO local(
	nome, "lotação", "descrição", id_centro, id_bloco, tipo_local)
	VALUES ('LEC 2', 20, 'Laboratório de Ciências da Computação 2', 1, 1, 'Laboratório');

INSERT INTO local_laboratório(
	id_local)
	VALUES (4);

INSERT INTO local(
	nome, "lotação", "descrição", id_centro, id_bloco, tipo_local)
	VALUES ('Sala 1040', 60, 'Sala número 1040 do bloco 910', 1, 1, 'Sala');

INSERT INTO local_laboratório(id_local)
	VALUES (5);

INSERT INTO local(
	nome, "lotação", "descrição", id_centro, id_bloco, tipo_local)
	VALUES ('Biblioteca 1', 20, 'Biblioteca do bloco 910', 1, 1, 'Biblioteca');

INSERT INTO local_biblioteca(id_local)
	VALUES (6);



INSERT INTO 
Horário (horário_início, horário_término, dia_semana)
VALUES ('08:00', '10:00', 'Terça-Feira');

INSERT INTO 
Horário (horário_início, horário_término, dia_semana)
VALUES ('08:00', '10:00', 'Quinta-Feira');

INSERT INTO 
Horário (horário_início, horário_término, dia_semana)
VALUES ('08:00', '10:00', 'Segunda-Feira');

INSERT INTO 
Horário (horário_início, horário_término, dia_semana)
VALUES ('08:00', '10:00', 'Quarta-Feira');



INSERT INTO 
Turma(nome, "carga_horária", semestre_ano, estado, vagas, id_disciplina, id_local)
VALUES ('Turma de Engenharia de Software 1', 64, '2022.2', 'ABERTA', 10, 4, 5);

INSERT INTO 
Turma(nome, "carga_horária", semestre_ano, estado, vagas, id_disciplina, id_local)
VALUES ('Turma de Fundamentos de Bancos de Dados', 64, '2022.2', 'ABERTA', 10, 1, 2);


INSERT INTO 
Turma_Horário(id_turma, id_horário)
VALUES (1, 1);

INSERT INTO 
Turma_Horário(id_turma, id_horário)
VALUES (1, 2);

INSERT INTO 
Turma_Horário(id_turma, id_horário)
VALUES (2, 1);

INSERT INTO 
Turma_Horário(id_turma, id_horário)
VALUES (2, 2);


INSERT INTO
Turma_Aluno (id_aluno, id_turma)
VALUES (1, 1);

INSERT INTO
Turma_Aluno (id_aluno, id_turma)
VALUES (2, 1);

INSERT INTO
Turma_Aluno (id_aluno, id_turma)
VALUES (3, 1);

INSERT INTO
Turma_Aluno (id_aluno, id_turma)
VALUES (1, 2);

INSERT INTO
Turma_Aluno (id_aluno, id_turma)
VALUES (2, 2);


INSERT INTO Avaliação(
	nota, "tipo_avaliação", id_aluno, id_turma)
	VALUES (8, 'AP1', 1, 1);

INSERT INTO Avaliação(
	nota, "tipo_avaliação", id_aluno, id_turma)
	VALUES (10, 'AP2', 1, 1);

INSERT INTO Avaliação(
	nota, "tipo_avaliação", id_aluno, id_turma)
	VALUES (7, 'AP3', 1, 1);

INSERT INTO Avaliação(
	nota, "tipo_avaliação", id_aluno, id_turma)
	VALUES (5, 'AP1', 2, 1);

INSERT INTO Avaliação(
	nota, "tipo_avaliação", id_aluno, id_turma)
	VALUES (6, 'AP2', 2, 1);

INSERT INTO Avaliação(
	nota, "tipo_avaliação", id_aluno, id_turma)
	VALUES (8, 'AP3', 2, 1);

INSERT INTO Avaliação(
	nota, "tipo_avaliação", id_aluno, id_turma)
	VALUES (10, 'AP1', 3, 1);

INSERT INTO Avaliação(
	nota, "tipo_avaliação", id_aluno, id_turma)
	VALUES (9, 'AP2', 3, 1);

INSERT INTO Avaliação(
	nota, "tipo_avaliação", id_aluno, id_turma)
	VALUES (8, 'AP3', 3, 1);

INSERT INTO public."avaliação"(
	nota, "tipo_avaliação", id_aluno, id_turma)
	VALUES (10, 'AP1', 1, 2);

INSERT INTO public."avaliação"(
	nota, "tipo_avaliação", id_aluno, id_turma)
	VALUES (8.5, 'AP2', 1, 2);


UPDATE Turma
	SET estado='CONCLUÍDA'
	WHERE id_turma = 1;
