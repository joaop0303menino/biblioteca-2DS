use [dados da biblioteca ]

CREATE TABLE administrador(
	id int primary key,
	login varchar(50) not null,
	senha varchar(20) not null
)

CREATE TABLE usuario(
	id int primary key,
	id_administrador int foreign key references administrador(id),
	nome varchar(50) not null,
	sobrenome varchar(50) not null
)

CREATE TABLE livro(
	codigo int primary key,
	id_usuario int foreign key references usuario(id),
	nome varchar(150) not null,
	quantidade int not null 
)


CREATE TABLE aluno(
	RA varchar(50) primary key ,
	id_usuario int foreign key references usuario(id),
	nome varchar(50) not null,
	sobrenome varchar(50) not null,
	serie varchar(50) not null
)

CREATE TABLE historico(
	RA_aluno varchar(50) primary key foreign key references aluno(RA),
	codigo_livro int foreign key references livro(codigo),
	dataRetirada datetime not null,
	dataDevolucao datetime not null, 
	estado varchar(10) not null,
	check (estado in ('pendente', 'entregue'))
)