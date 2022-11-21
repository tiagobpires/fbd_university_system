DROP TABLE aluno, avaliação, campus, centro, curso, disciplina, endereço, local, local_auditório, local_biblioteca, local_laboratório, local_sala, professor, professor_disciplina, professor_reitor, turma, turma_aluno, turma_horário, horário, local_bloco, município CASCADE;


CREATE TABLE Endereço(
	id_endereço SERIAL,
	rua TEXT NOT NULL,
	número TEXT NOT NULL,
	complemento TEXT,
	cep TEXT NOT NULL,
	estado TEXT NOT NULL,
	cidade TEXT NOT NULL,

	PRIMARY KEY (id_endereço)
);

CREATE TABLE Aluno(
	id_aluno SERIAL,
	matricula VARCHAR(5) NOT NULL,
	data_nasc DATE NOT NULL,
	email VARCHAR(120) NOT NULL,
	sexo VARCHAR(9) NOT NULL,
	nome VARCHAR(80) NOT NULL,

	id_endereço INTEGER NOT NULL UNIQUE,
    
	PRIMARY KEY (id_aluno),
	FOREIGN KEY (id_endereço) REFERENCES Endereço
);

CREATE TABLE Disciplina(
	id_disciplina SERIAL,
	nome VARCHAR(80) NOT NULL,
	carga_horária SMALLINT NOT NULL CHECK (carga_horária >= 32 AND carga_horária <= 128),
	ementa TEXT NOT NULL,

	PRIMARY KEY (id_disciplina)
);

CREATE TABLE Professor (
	id_profs SERIAL,
	data_nasc DATE NOT NULL,
	nome VARCHAR(80) NOT NULL,
	formação VARCHAR(80) NOT NULL,
	email VARCHAR(120) NOT NULL,
	sexo VARCHAR(9) NOT NULL,
    
	PRIMARY KEY(id_profs)
);

CREATE TABLE Professor_Disciplina(
	id_profs INTEGER,
	id_disciplina INTEGER,

	PRIMARY KEY (id_profs, id_disciplina),

	FOREIGN KEY (id_profs) REFERENCES Professor,
	FOREIGN KEY (id_disciplina) REFERENCES Disciplina
);

CREATE TABLE Professor_Reitor(
	código_reitor INTEGER,
	id_profs INTEGER,
	data_admissão DATE NOT NULL,

	PRIMARY KEY (código_reitor),

	FOREIGN KEY (id_profs) REFERENCES Professor
);

CREATE TABLE Local (
	id_local SERIAL,
	nome VARCHAR(80) NOT NULL,
	lotação SMALLINT NOT NULL,
	descrição TEXT NOT NULL,
	tipo_local TEXT NOT NULL,

	PRIMARY KEY(id_local)
);

CREATE TABLE Local_sala (
	id_local INTEGER NOT NULL,
	PRIMARY KEY(id_local),
	FOREIGN KEY(id_local) REFERENCES Local ON DELETE CASCADE
);

CREATE TABLE Local_laboratório (
	id_local INTEGER NOT NULL,
	PRIMARY KEY(id_local),
	FOREIGN KEY(id_local) REFERENCES Local ON DELETE CASCADE
);

CREATE TABLE Local_auditório (
	id_local INTEGER NOT NULL,
	PRIMARY KEY(id_local),
	FOREIGN KEY(id_local) REFERENCES Local ON DELETE CASCADE
);

CREATE TABLE Local_biblioteca (
	id_local INTEGER NOT NULL,
	PRIMARY KEY(id_local),
	FOREIGN KEY(id_local) REFERENCES Local ON DELETE CASCADE
);

CREATE TABLE Local_bloco (
	id_local INTEGER NOT NULL,
	PRIMARY KEY(id_local),
	FOREIGN KEY(id_local) REFERENCES Local ON DELETE CASCADE
);

CREATE TABLE Horário(
	id_horário SERIAL,
	horário_início TIME NOT NULL,
	horário_término TIME NOT NULL,
	dia_semana VARCHAR(20) NOT NULL,
    
    PRIMARY KEY(id_horário)
);

CREATE TABLE Turma(
	id_turma SERIAL,
	nome VARCHAR(80) NOT NULL,
	carga_horária SMALLINT NOT NULL,
	semestre_ano VARCHAR(6) NOT NULL CHECK (semestre_ano ~ '^[0-9]{4}[.][1|2]{1}'),
	estado VARCHAR(9) NOT NULL CHECK (estado = 'ABERTA' OR estado = 'CONCLUÍDA'),
	vagas SMALLINT NOT NULL CHECK (qntd_alunos <= vagas),
	qntd_alunos SMALLINT DEFAULT 0,

	id_disciplina INTEGER NOT NULL,
	id_local INTEGER NOT NULL,
    
	PRIMARY KEY (id_turma),
	FOREIGN KEY (id_disciplina) REFERENCES Disciplina,
	FOREIGN KEY (id_local) REFERENCES Local
);

CREATE TABLE Turma_Horário(
	id_turma INTEGER,
	id_horário INTEGER,

	PRIMARY KEY (id_turma, id_horário),

	FOREIGN KEY (id_turma) REFERENCES Turma,
	FOREIGN KEY (id_horário) REFERENCES Horário
);

CREATE TABLE Turma_Aluno(
	id_turma INTEGER,
	id_aluno INTEGER,

	PRIMARY KEY (id_turma, id_aluno),

	FOREIGN KEY (id_turma) REFERENCES Turma,
	FOREIGN KEY (id_aluno) REFERENCES Aluno
);

CREATE TABLE Avaliação(
	id_avaliação SERIAL,
	nota SMALLINT CHECK (nota >= 0 AND nota <= 10),
	tipo_avaliação TEXT NOT NULL,
	id_aluno INTEGER NOT NULL,
	id_turma INTEGER NOT NULL,

	PRIMARY KEY (id_avaliação),

	FOREIGN KEY (id_aluno) REFERENCES Aluno,
	FOREIGN KEY (id_turma) REFERENCES Turma
);

CREATE TABLE Município(
	id_município SERIAL,
	nome TEXT NOT NULL,

	PRIMARY KEY (id_município)
);

CREATE TABLE Campus(
	id_campus SERIAL,
	nome VARCHAR(80) NOT NULL,
	id_município INTEGER NOT NULL,
	id_reitor INTEGER NOT NULL,

	PRIMARY KEY (id_campus),

	FOREIGN KEY (id_município) REFERENCES Município,
	FOREIGN KEY (id_reitor) REFERENCES Professor_Reitor
);

CREATE TABLE Centro (
	id_centro SERIAL,
	nome VARCHAR(80) NOT NULL,
	id_profs INTEGER UNIQUE NOT NULL,
       	id_campus INTEGER NOT NULL,

	PRIMARY KEY (id_centro),

	FOREIGN KEY(id_profs) REFERENCES Professor,
	FOREIGN KEY(id_campus) REFERENCES Campus
);

CREATE TABLE Curso(
	id_curso SERIAL,
	nome VARCHAR(80) NOT NULL,
	carga_horaria SMALLINT NOT NULL,
	id_profs INTEGER UNIQUE,
	id_centro INTEGER NOT NULL,
    
	PRIMARY KEY (id_curso),
	FOREIGN KEY (id_profs) REFERENCES Professor,
	FOREIGN KEY (id_centro) REFERENCES Centro
);

ALTER TABLE Aluno
	ADD COLUMN id_curso INTEGER,
	ADD FOREIGN KEY (id_curso) REFERENCES Curso;

ALTER TABLE Local
	ADD COLUMN id_centro INTEGER NOT NULL,
	ADD COLUMN id_bloco INTEGER,

	ADD FOREIGN KEY(id_centro) REFERENCES Centro ON DELETE CASCADE,
	ADD FOREIGN KEY(id_bloco) REFERENCES Local_bloco ON DELETE CASCADE;

ALTER TABLE Professor
	ADD COLUMN id_curso INTEGER,
	
	ADD FOREIGN KEY (id_curso) REFERENCES Curso;

CREATE OR REPLACE FUNCTION checagem_coord() RETURNS trigger AS 
$BODY$
    DECLARE 
	prof_eh_diretor SMALLINT;
    BEGIN
	SELECT COUNT(1) 
    INTO prof_eh_diretor
	FROM Centro C
	WHERE C.id_profs = NEW.id_profs;
	
 	IF (prof_eh_diretor = 1) THEN
		RAISE EXCEPTION 'professor já é diretor';
	END IF;
	RETURN NEW;
END
$BODY$ 
LANGUAGE plpgsql;

CREATE TRIGGER checagem_coord BEFORE INSERT OR UPDATE ON Curso
    FOR EACH ROW EXECUTE FUNCTION checagem_coord();


CREATE OR REPLACE FUNCTION checagem_diretor() RETURNS trigger AS 
$BODY$
    DECLARE 
	prof_eh_coord SMALLINT;
    BEGIN
	SELECT COUNT(1) 
    INTO prof_eh_coord
	FROM Curso C
	WHERE C.id_profs = NEW.id_profs;
	
 	IF (prof_eh_coord = 1) THEN
		RAISE EXCEPTION 'professor já é coordenador';
	END IF;
	RETURN NEW;
END
$BODY$ 
LANGUAGE plpgsql;

CREATE TRIGGER checagem_diretor BEFORE INSERT OR UPDATE ON Centro
    FOR EACH ROW EXECUTE FUNCTION checagem_diretor();


CREATE OR REPLACE FUNCTION checagem_matricula_disciplina() RETURNS trigger AS 
$BODY$
    DECLARE 
	aluno_esta_matriculado SMALLINT;
    BEGIN
	SELECT COUNT(1) 
    INTO aluno_esta_matriculado
    FROM Turma_Aluno TA
    JOIN Turma T
    ON T.id_turma = TA.id_turma
    JOIN Disciplina D
    ON T.id_disciplina = D.id_disciplina
    WHERE TA.id_aluno = NEW.id_aluno AND D.id_disciplina = (
        SELECT D.id_disciplina
        FROM Disciplina D
        JOIN Turma T
        ON D.id_disciplina = T.id_disciplina
        WHERE T.id_turma = NEW.id_turma
    );
	
 	IF (aluno_esta_matriculado = 1) THEN
		RAISE EXCEPTION 'aluno já está matriculado em turma dessa disciplina';
	END IF;
	RETURN NEW;
END
$BODY$ 
LANGUAGE plpgsql;

CREATE TRIGGER checagem_matricula_disciplina BEFORE INSERT OR UPDATE ON TURMA_ALUNO
    FOR EACH ROW EXECUTE FUNCTION checagem_matricula_disciplina();

CREATE OR REPLACE FUNCTION adicionar_curso_coordenador() RETURNS trigger AS 
$BODY$
    BEGIN
	
    UPDATE Professor
    SET id_curso = NEW.id_curso
    WHERE id_profs = NEW.id_profs;
    
	RETURN NEW;
END
$BODY$ 
LANGUAGE plpgsql;

CREATE TRIGGER adicionar_curso_coordenador AFTER INSERT OR UPDATE ON Curso
    FOR EACH ROW EXECUTE FUNCTION adicionar_curso_coordenador();


CREATE OR REPLACE FUNCTION checar_diretor_faz_parte_curso() RETURNS trigger AS 
$BODY$
    DECLARE 
	professor_faz_parte_curso SMALLINT;
    BEGIN
	SELECT COUNT(1) 
    INTO professor_faz_parte_curso
    FROM Professor
    WHERE id_curso IN (
        SELECT id_curso
        FROM Curso
        WHERE id_centro = OLD.id_centro
    ) AND id_profs = NEW.id_profs;
    
    IF (professor_faz_parte_curso = 0) THEN
		RAISE EXCEPTION 'professor não faz parte de algum curso que pertence ao centro';
    END IF;
    
	RETURN NEW;
END
$BODY$ 
LANGUAGE plpgsql;

CREATE TRIGGER checar_diretor_faz_parte_curso BEFORE UPDATE ON Centro
    FOR EACH ROW EXECUTE FUNCTION checar_diretor_faz_parte_curso();


CREATE OR REPLACE FUNCTION limiteLeciona() RETURNS trigger AS
$BODY$
	DECLARE
    qnt_disciplinas SMALLINT;
    
	BEGIN
    select count (id_disciplina) into qnt_disciplinas from professor_disciplina where id_profs = NEW.id_profs GROUP BY id_profs  ;
   	 
 	IF (qnt_disciplinas > 4) THEN
    	RAISE EXCEPTION 'limite de cadeiras excedida';
	END IF;
	RETURN NEW;
END
$BODY$
LANGUAGE plpgsql;

CREATE TRIGGER limiteLeciona BEFORE INSERT ON professor_disciplina
	FOR EACH ROW EXECUTE FUNCTION limiteLeciona();


CREATE OR REPLACE FUNCTION incrementarTurma() RETURNS trigger AS
$BODY$

BEGIN

	UPDATE turma SET qntd_alunos = qntd_alunos + 1;
	RETURN NEW;

END;

$BODY$
LANGUAGE plpgsql;

CREATE TRIGGER incrementarTurma AFTER INSERT ON turma_aluno
FOR EACH ROW EXECUTE FUNCTION incrementarTurma();


CREATE OR REPLACE FUNCTION decrementarTurma() RETURNS trigger AS
$BODY$

BEGIN

           UPDATE turma SET qntd_alunos = qntd_alunos - 1;
	RETURN NEW;

END;

$BODY$
LANGUAGE plpgsql;

CREATE TRIGGER decrementarTurma AFTER DELETE ON turma_aluno
FOR EACH ROW EXECUTE FUNCTION decrementarTurma();

