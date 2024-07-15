use [dados da biblioteca ]

CREATE TABLE administrador(
	id int primary key,
	login varchar(max) not null,
	senha varchar(max) not null
)

CREATE TABLE usuario(
	id int primary key,
	id_administrador int foreign key references administrador(id),
	nome varchar(max) not null,
	sobrenome varchar(max) not null
)

CREATE TABLE livro(
	codigo int primary key,
	id_usuario int foreign key references usuario(id),
	nome varchar(max) not null,
	quantidade int not null 
)


CREATE TABLE aluno(
	RA varchar(max) primary key ,
	id_usuario int foreign key references usuario(id),
	nome varchar(max) not null,
	sobrenome varchar(max) not null,
	serie varchar(max) not null
)

CREATE TABLE historico(
	RA_aluno varchar(max) primary key foreign key references aluno(RA),
	codigo_livro int foreign key references livro(codigo),
	dataRetirada datetime not null,
	dataDevolucao datetime not null, 
	observacao varchar(max),
	estado varchar(max) not null,
	check (estado in ('pendente', 'entregue'))
	)
