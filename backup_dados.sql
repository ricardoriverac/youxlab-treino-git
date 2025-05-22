-- Abaixo temos a casinha dos dados :)
create table cliente (
	idcliente integer not null,
	nome varchar(50) not null,
	cpf char(11),
	rg varchar(15),
	data_nascimento date,
	genero char(1),
	profissao varchar(30),
	nacionalidade varchar(30),
	logradouro varchar(30),
	numero varchar(10),
	complemento varchar(30),
	bairro varchar(30),
	municipio varchar(30),
	uf varchar(30),
	obseracoes text,

	constraint pk_cln_idcliente primary key (idcliente)
);

-- Abaixo temos nosso banco de dados
insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(1, 'Garcia', '11122233344', '12345', '2007-08-05', 'M', 'Estudante', 'Brasileira', '25 de março', '23', 'Casa', 'Cidade Nova', 'Porto união', 'SP');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (2, 'Geraldo', '12343299291', '56565', '1987-01-04', 'M', 'Engenheiro', 'Brasileira', 'Rua das Limas', '200', 'Ap.', 'Centro', 'P. União', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (3, 'Carlos', '87732323227', '55463', '1967-10-01', 'M', 'Pedreiro', 'Brasileira', 'Rua das Laranjeiras', '300', 'Apart.', 'Cto.', 'Canoinhas', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (4, 'Adriana', '12321222122', '98777', '1989-09-10', 'F', 'Jornalista', 'Brasileira', 'Rua das Limas', '240', 'Casa', 'São Pedro', 'Porto Vitória', 'PR');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (5, 'Amanda', '99982838828', '28382', '1991-03-04', 'F', 'Jorn.', 'Italiana', 'Av. Central', '100', null, 'São Pedro', 'General Carneiro', 'PR');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (6, 'Angelo', '99982828181', '12323', '2000-01-01', 'M', 'Professor', 'Brasileiro', 'Av. Beira Mar', '300', 'Ctr.', 'São Paulo', 'São Paulo', 'SP');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (7, 'Anderson', null, null, null, 'M', 'Prof.', 'Italiano', 'Av. Brasil', '100', 'Apartamento', 'Santa Rosa', 'Rio de Janeiro', 'SP');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (8, 'Camila', '09998282828', null, '2001-10-10', 'F', 'Professora', 'Norte americana', 'Rua Central', '4333', null, 'Centro', 'Uberlândia', 'MG');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (9, 'Cristiano', null, null, null, 'M', 'Estudante', 'Alemã', 'Rua do Centro', '877', 'Casa', 'Centro', 'Porto Alegre', 'RS');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (10, 'Fabrício', '8828282828', '32323', null, 'M', 'Estudante', 'Brasileiro', null, null, null, 'Centro', 'Porto União', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (11, 'Fernanda', null, null, null, 'F', null, 'Brasileira', null, null, null, 'Porto', 'União', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (12, 'Gilmar', '88881818181', '888', '2000-02-10', 'M', 'Estud.', null, 'Rua das Laranjeiras', '200', null, 'C. Nova', 'Canoinhas', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (13, 'Diego', '01010191919', '111939', null, 'M', 'Professor', 'Alemão', 'Rua Central', '455', 'Casa', 'Cidade N.', 'São Paulo', 'SP');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (14, 'Jeferson', null, null, '1983-07-01', 'M', null, 'Brasileiro', null, null, null, 'União da Vitória', 'União da Vitória', 'PR');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (15, 'Jessica', null, null, null, 'F', 'Estudante', null, null, null, null, null, 'União da Vitória', 'PR');






