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

-- Testes de consultas

select * from cliente;
-- Puxa os selecionados ( Abaixo )
select nome, data_nascimento from cliente;

-- Abaixo ele puxa renomeando visualmente
select nome as "Nome", data_nascimento as "Data de Nascimento" from cliente;

-- Selecionar e mostrar em linhas
select 'CPF:' || cpf || ' RG ' || rg as "CPF e RG" from cliente;

-- Abaixo temos tipo um head()
select * from cliente limit 5;

-----------------------------------------------
-- Abaixo temos um comando que puxa apenas nascidos depois de 2000-01-01
select nome, cpf, data_nascimento from cliente where data_nascimento > '2000-01-01';

-- Abaixo temos um comando que vai selecionar os nomes que começam com C
select nome from cliente where nome like 'C%';

-- Abaixo temos um comando que seleciona nomes com c no meio
select nome from cliente where nome like '%c%';

-- Abaixo temos um filtro que comeca em um ano e acaba em outro
select nome, cpf, data_nascimento from cliente where data_nascimento between '1990-01-01' and '1998-01-01'

-- Busca apenas os rg 'null'
select nome, rg from cliente where rg is null;

-- Abaixo temos um comando pra deixar em abc..
select nome from cliente order by nome;

-- Decressente
select nome from cliente order by nome desc;

-- Abaixo os primeiros exercicios

-- 1
select nome, genero, profissao from cliente order by nome desc;

-- 2
select nome from cliente where nome like '%r%';

-- 3
select nome from cliente where nome like 'C%';

-- 4
select nome from cliente where nome like '%a';

-- 5
select * from cliente where bairro like 'Centro';

-- 6 
select * from cliente where bairro like 'C%';

-- 7
select * from cliente where genero like 'F';

-- 8 
select * from cliente where cpf is null;

-- 9
select nome, profissao from cliente order by profissao;

-- 10
select * from cliente where nacionalidade like 'Brasileira';

-- 11
select * from cliente where numero is not null;

-- 12
select * from cliente where municipio like 'Porto União';

-- 13
select * from cliente where data_nascimento between '2000-01-01' and '2002-01-01'

-- 14
select 'Nome:' || nome || ' logradouro ' || logradouro || ' número ' || numero || ' complemento ' || complemento || ' bairro ' || bairro || ' município ' || municipio || ' UF '
|| uf as "14" from cliente;

----------------------------------------------------------------------
-- AUla 17
select * from cliente;

-- Abaixo ele substitui na lista o nome indicado pela sua key
update cliente set nome = 'Garcia2' where idcliente = 1;

-- Abaixo ele substitui diveros valores do cliente
update cliente set nome = 'Adriano', genero = 'M', numero = '241' where idcliente = 4;

-- Inserir um cliete no banco de dados
insert into cliente (idcliente, nome) values (16, 'João');

-- Abaixo o comando pra deletar um cliente
delete from cliente where idcliente = 16;

---------------------------------------------------------------------
-- Exercicios 2
select * from cliente;

-- 1 
insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(16, 'Maicon', '12349598421', '1234', '1965-10-10', 'F', 'Empresario', null, null, null, null, null, 'Florianopolis', 'PR');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(17, 'Getulio', null, '4631', null, 'F', 'Estudante', 'Brasileira', 'Rua Central', '343', 'Apartamento', 'Centro', 'Curitiba', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(18, 'Sandra', null, null, null, 'M', 'Professor', 'Italiana', null, '12', 'Bloco A.', null, null, null);

-- 2
update cliente set cpf = '45390569432', genero = 'M', nacionalidade = 'Brasileira', uf = 'SC' where idcliente = 16;

