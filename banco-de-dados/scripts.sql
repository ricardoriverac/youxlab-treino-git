create table cliente (
	idcliente int not null,
	nome varchar(50) not null, -- varchar: nome pode receber até 50 caracteres
	cpf char(11), -- char: cpf tem que receber obrigatoriamente 11 caracteres
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
	observacoes text,

	-- primary key
	constraint pk_cln_idcliente primary key (idcliente)
)

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (1, 'Manoel', '88828383821', '32323', '2001-01-30', 'M', 'Estudante', 'Brasileira', 'Rua Joaquim Nabuco', '23', 'Casa', 'Cidade Nova', 'Porto União', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (2, 'Geraldo', '12343299929', '56565', '1987-01-04', 'M', 'Engenheiro', 'Brasileiro', 'Rua das Limas', '200', 'Ap', 'Centro', 'Poro Uniao', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (3, 'Carlos', '87732323227', '55463', '1967-10-01', 'M', 'Pedreiro', 'Brasileiro', 'Rua das Laranjeiras', '300', 'Apart.', 'Cto.', 'Canoinhas', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (4, 'Adriana', '12321222122', '98777', '1989-09-10', 'F', 'Jornalista', 'Brasileira', 'Rua das Limas', '240', 'Casa', 'São Pedro', 'Porto Vitória', 'PR');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (5, 'Amanda', '99982838828', '28382', '1991-03-04', 'F', 'Jorn.', 'Italiana', 'Av. Central', '100', null, 'São Pedro', 'General Carneiro', 'PR');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (6, 'Ângelo', '99982828181', '12323', '2000-01-01', 'M', 'Professor', 'Brasileiro', 'Av. Beira Mar', '300', null, 'Ctr.', 'São Paulo', 'SP');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (7, 'Anderson', null, null, null, 'M', 'Prof.', 'Italiano', 'Av. Brasil', '100', 'Apartamento', 'Santa Rosa', 'Rio de Janeiro', 'SP');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (8, 'Camila', '9998282828', null, '2001-01-01', 'F', 'Professora', 'Norte Americana', 'Rua Central', '4333', null, 'Centro', 'Uberlândia', 'MG');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (9, 'Cristiano', null, null, null, 'M', 'Estudante', 'Alemã', 'Rua do Centro', '877', 'Casa', 'Centro', 'Porto Alegre', 'RS');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (10, 'Fabricío', '8828282828', '32323', null, 'M', 'Estudante', 'Brasileiro', null, null, null, null, 'PU', 'SC');

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, UF)
values (11,'Fernanda',null,null,null,'F',null,'Brasileira',null,null,null,null,'Porto União','SC');

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, UF)
values (12,'Gilmar','88881818181','888','2000-02-10','M','Estud.',null,'Rua das Laranjeiras','200',null,'C. Nova','Canoinhas','SC');

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, UF)
values (13,'Diego','1010191919','111939',null,'M','Professor','Alemão','Rua Central','455','Casa','Cidade N.','São Paulo','SP');

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, UF)
values (14,'Jeferson',null,null,'1983-07-01','M',null,'Brasileiro',null,null, null,null,'União da Vitória','PR');

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, UF)
values (15,'Jessica',null,null,null,'F','Estudante', null, null, null, null, null, 'União da Vitória','PR');

select * from cliente;

select nome, data_nascimento from cliente;

select nome, data_nascimento as "Data de Nascimento" from cliente;

select 'CPF: ' || cpf || ' RG: ' || rg as "CPF e RG" from cliente;

select * from cliente limit 3;

select nome, data_nascimento from cliente where data_nascimento > '2000-01-01';

select nome from cliente where nome like 'C%';

select nome from cliente where nome like '%c%';

select nome, data_nascimento from cliente where data_nascimento between '1990-01-01' and '1998-01-01';

select nome, rg from cliente where rg is null;

select nome from cliente order by nome desc; -- asc ou desc: filtrar por crescente ou decrescente

-- EXERCICIOS
-- 1 
select nome, genero, profissao from cliente order by nome asc;

-- 2
select * from cliente where nome like '%r%' or nome like 'R%';

-- 3
select * from cliente where nome like 'C%';

-- 4
select * from cliente where nome like '%a';

-- 5 
select * from cliente where bairro in ('Centro', 'Cto.', 'Ctr.')

-- 6
select * from cliente where complemento like 'A%';

-- 7 
select * from cliente where genero = 'F';

-- 8
select * from cliente where cpf is null;

-- 9
select nome, profissao from cliente order by profissao asc;

-- 10
select * from cliente where nacionalidade like 'Brasileira' or  nacionalidade like 'Brasileiro';

-- 11 
select * from cliente where numero is not null;

-- 12
select * from cliente where uf like 'SC';

-- 13 
select * from cliente where data_nascimento between '2000-01-01' and '2002-01-01';

-- 14
select 'Nome: ' || nome || ' Logradouro: ' || logradouro || ' Número: ' || numero || ' Complemento: ' || complemento || ' Bairro: ' ||  bairro || ' Município:' || municipio || ' Estado: ' || uf as "Registro" from cliente

-- FIM

select * from cliente;

update cliente set nome = 'Teste' where idcliente = 1;

update cliente set nome = 'Adriano', genero = 'M', numero = '241' where idcliente = 4;

insert into cliente (idcliente, nome) values (16, 'João');

delete from cliente where idcliente = 16;

-- EXERCICIOS 
-- 1 
insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, municipio, uf)
values (16, 'Maicon', '12349596421', '1234', '1965-10-10', 'F', 'Empresário', 'Florianópolis', 'SC');

insert into cliente (idcliente, nome, rg, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (17, 'Getúlio', '4631', 'F', 'Estudante', 'Brasileira', 'Rua Central', '343', 'Apartamento', 'Centro', 'Curitiba', 'PR')

insert into cliente (idcliente, nome, genero, profissao, nacionalidade, numero, complemento)
values (18, 'Sandra', 'M', 'Professor', 'Italiana', '12', 'Bloco A')

-- 2

update cliente set cpf = '45390569432', genero = 'M', nacionalidade = 'Brasileiro', uf = 'SC' where idcliente = 16;

-- 3
update cliente set data_nascimento = '1978-04-01', genero = 'M' where idcliente = 17;

-- 4
update cliente set genero = 'F', profissao = 'Professora', numero = '123' where idcliente = 18;

-- 5
delete from cliente where idcliente = 16;

-- 6 
delete from cliente where idcliente = 18;
select * from cliente;

-- FIM

create table profissao (
	idprofissao int not null,
	nome varchar(30) not null,

	constraint pk_prf_idprofissao primary key (idprofissao),
	constraint un_prf_nome unique (nome)
);

insert into profissao (idprofissao, nome) values (1, 'Estudante');
insert into profissao (idprofissao, nome) values (2, 'Engenheiro');
insert into profissao (idprofissao, nome) values (3, 'Pedreiro');
insert into profissao (idprofissao, nome) values (4, 'Jornalista');
insert into profissao (idprofissao, nome) values (5, 'Professor');

select * from profissao;

create table nacionalidade (
	idnacionalidade int not null,
	nome varchar(30) not null,

	constraint pk_ncn_idnacionalidade primary key (idnacionalidade),
	constraint un_ncn_nome unique (nome)
);

insert into nacionalidade (idnacionalidade, nome) values (1, 'Brasileira');
insert into nacionalidade (idnacionalidade, nome) values (2, 'Italiana');
insert into nacionalidade (idnacionalidade, nome) values (3, 'Norte-Americana');
insert into nacionalidade (idnacionalidade, nome) values (4, 'Alemã');

select * from nacionalidade

create table complemento (
	idcomplemento int not null,
	nome varchar(30) not null,

	constraint pk_cmp_idcomplemento primary key (idcomplemento),
	constraint un_cmp_nome unique (nome)
)

insert into complemento (idcomplemento, nome) values (1, 'Casa');
insert into complemento (idcomplemento, nome) values (2, 'Apartamento');

select * from complemento

create table bairro (
	idbairro int not null,
	nome varchar(30) not null,

	constraint pk_brr_idbairro primary key (idbairro),
	constraint un_brr_nome unique (nome)
]

insert into bairro (idbairro, nome) values (1, 'Cidade Nova');
insert into bairro (idbairro, nome) values (2, 'Centro');
insert into bairro (idbairro, nome) values (3, 'São Pedro');
insert into bairro (idbairro, nome) values (4, 'Santa Rosa');

select * from bairro

select * from cliente;

alter table cliente rename column profissao to idprofissao;
alter table cliente alter column idprofissao type int; 

-- Estudante -> 1, 9, 10, 12, 15, 17
-- Engenheiro -> 2
-- Pedreiro -> 3
-- Jornalista -> 4, 5
-- Professor -> 6, 7, 8, 13
-- Null -> 11, 14

alter table cliente drop idprofissao;
alter table cliente add idprofissao int;
alter table cliente add constraint fk_cln_idprofissao foreign key (idprofissao) references profissao (idprofissao);

update cliente set idprofissao = 1 where idcliente in (1, 9, 10, 12, 15, 17);
update cliente set idprofissao = 2 where idcliente = 2;
update cliente set idprofissao = 3 where idcliente = 3;
update cliente set idprofissao = 4 where idcliente in (4, 5);
update cliente set idprofissao = 5 where idcliente in (6, 7, 8, 13);

 