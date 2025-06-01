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

-- 3
update cliente set data_nascimento = '1978--04-01', genero = 'M' where idcliente = 17
update cliente set idcliente = 2452;

-- 4
update cliente set genero = 'F', profissao = 'Professora', numero = '123' where idcliente = 18

-- 5
delete from cliente where idcliente = 16;

-- 6 
delete from cliente where idcliente = 18;

-------------------------------------------------
-- Aula 20
create table profissao (
	idprofissao integer not null,
	nome varchar(30) not null, 

	constraint pk_prf_idprofissao primary key (idprofissao),
	constraint un_prf_idnome unique (nome)
);

insert into profissao (idprofissao, nome) values (5, 'Estudante');
insert into profissao (idprofissao, nome) values (2, 'Engenheiro');
insert into profissao (idprofissao, nome) values (3, 'Pedreiro');
insert into profissao (idprofissao, nome) values (4, 'Jornalista');
insert into profissao (idprofissao, nome) values (1, 'Professor');

select * from profissao

create table nacionalidade (
	idnacionalidade integer not null, 
	nome varchar(30) not null,

	constraint pk_ncn_idnacionalidade primary key(idnacionalidade),
	constraint un_ncn_nome unique (nome)
);

select nacionalidade from cliente;
insert into nacionalidade (idnacionalidade, nome) values (1, 'Brasileira');
insert into nacionalidade (idnacionalidade, nome) values (2, 'Italiana');
insert into nacionalidade (idnacionalidade, nome) values (3, 'Norte-Americana');
insert into nacionalidade (idnacionalidade, nome) values (4, 'alemã');
select * from nacionalidade;

create table complemento (
	idcomplemento integer not null,
	nome varchar(30) not null,

	constraint pk_cpl_idcomplemento primary key (idcomplemento),
	constraint un_cpl_nome unique (nome)
);

insert into complemento (idcomplemento, nome) values (1, 'Casa');
insert into complemento (idcomplemento, nome) values (2, 'Apartamento');

select * from complemento;

create table bairro (
	idbairro integer not null,
	nome varchar(30) not null,

	constraint pk_brr_idbairro primary key (idbairro),
	constraint un_brr_nome unique (nome)
);

insert into bairro (idbairro, nome) values (1,'Cidade Nova');
insert into bairro (idbairro, nome) values (2,'Centro');
insert into bairro (idbairro, nome) values (3,'São Pedro');
insert into bairro (idbairro, nome) values (4, 'Santa Rosa');

select * from bairro;
--------------------------------------------------------
-- Aula 21
select * from cliente;
alter table cliente rename column profissao to idprofissao;
alter table cliente alter column idprofissao type integer;

-- Estudante -> 9, 10, 15, 1, 17
-- Engenheiro -> 2 
-- Pedreiro -> 3
-- Jornalista -> 4 
-- Professor -> 6, 13
-- Null -> 11, 14
alter table cliente drop idprofissao;
alter table cliente add idprofissao integer;
alter table cliente add constraint fk_cln_idprofissao foreign key(idprofissao) references profissao (idprofissao);

update cliente set idprofissao = 1 where idcliente in (9, 10, 15, 1, 17);
update cliente set idprofissao = 2 where idcliente = 2;
update cliente set idprofissao = 3 where idcliente = 3;
update cliente set idprofissao = 4 where idcliente = 4;
update cliente set idprofissao = 5 where idcliente in (6, 13);
update cliente set idprofissao = 5 where idcliente in (11, 14);

select * from profissao;
delete from profissao where idprofissao = 10;
insert into profissao (idprofissao, nome) values (10, 'Teste');

alter table cliente drop nacionalidade;
-- BR - 1, 17, 2, 3, 4, 11
-- IT - 5
-- NA - 
-- AA - 9
alter table cliente add idnacionalidade integer;
alter table cliente add constraint fk_cln_idnacionalidade foreign key (idnacionalidade) references nacionalidade (idnacionalidade);
update cliente set idnacionalidade = 1 where idcliente in (1, 17, 2, 3, 4, 11);
update cliente set idnacionalidade = 2 where idcliente = 5;
update cliente set idnacionalidade = 3 where idcliente = 9;

select * from cliente
alter table cliente drop complemento;
-- Apartamento - 1, 10, 11, 12 
-- Casa - 7, 6, 9, 13, 16
alter table cliente add idcomplemento integer;
alter table cliente add constraint fk_cln_idcomplemento foreign key (idcomplemento) references complemento (idcomplemento);
update cliente set idcomplemento = 1 where idcliente in (7, 6, 9, 13, 16);
update cliente set idcomplemento = 2 where idcliente in (1, 10, 11, 12);

alter table cliente drop bairro;
alter table cliente add idbairro integer;
alter table cliente add constraint fk_cln_idbairro foreign key (idbairro) references bairro (idbairro);

select * from bairro
update cliente set idbairro = 1 where idcliente in (1, 12, 13);
update cliente set idbairro = 2 where idcliente in (2, 3, 6, 8, 9);
update cliente set idbairro = 3 where idcliente in (4, 5)
update cliente set idbairro = 4 where idcliente = 7;

select * from cliente
create table uf (
	iduf integer not null,
	nome  varchar(30) not null,
	sigla char(2) not null,

	constraint pk_ufd_idunidade_federacao primary key (iduf), 
	constraint un_ufd_nome unique (nome),
	constraint un_ufd_sigla unique (sigla)
);

insert into uf (iduf, nome, sigla) values (1, 'Santa Catarina', 'SC');
insert into uf (iduf, nome, sigla) values (2, 'Paraná', 'PR');
insert into uf (iduf, nome, sigla) values (3, 'São Paulo', 'SP');
insert into uf (iduf, nome, sigla) values (4, 'Minas Gerais', 'MG');
insert into uf (iduf, nome, sigla) values (5, 'Rio  Grande do Sul', 'RS');
insert into uf (iduf, nome, sigla) values (6, 'Rio de Janeiro', 'RJ');

select * from uf

create table municipio(
	idmunicipio integer not null,
	nome varchar(30) not null,
	iduf integer not null,

	constraint pk_mnc_idmunicipio primary key (idmunicipio),
	constraint un_mnc_nome unique (nome),
	constraint fk_mnc_iduf foreign key (iduf) references uf (iduf)
);

insert into municipio (idmunicipio, nome, iduf) values (1, 'Porto União', 1);
insert into municipio (idmunicipio, nome, iduf) values (2, 'Canoninhas', 1);
insert into municipio (idmunicipio, nome, iduf) values (3, 'Porto Vitória', 2);
insert into municipio (idmunicipio, nome, iduf) values (4, 'General Carneiro', 2);
insert into municipio (idmunicipio, nome, iduf) values (5, 'São Paulo', 3);
insert into municipio (idmunicipio, nome, iduf) values (6, 'Rio de Janeiro', 6);
insert into municipio (idmunicipio, nome, iduf) values (7, 'Uberlândia', 4);
insert into municipio (idmunicipio, nome, iduf) values (8, 'Porto Alegre', 5);
insert into municipio (idmunicipio, nome, iduf) values (9, 'União da Vitória', 2);
select * from municipio

select * from cliente
alter table cliente drop municipio;
alter table cliente drop uf;
alter table cliente add idmunicipio integer;
alter table cliente add constraint fk_cliente_idmunicipio foreign key (idmunicipio) references municipio (idmunicipio);

update cliente set idmunicipio = 1 where idcliente in (1, 2, 10, 11);
update cliente set idmunicipio = 2 where idcliente in (3, 12);
update cliente set idmunicipio = 3 where idcliente = 4;
update cliente set idmunicipio = 4 where idcliente = 5;
update cliente set idmunicipio = 5 where idcliente in (6, 13);
update cliente set idmunicipio = 6 where idcliente = 7;
update cliente set idmunicipio = 7 where idcliente = 8;
update cliente set idmunicipio = 8 where idcliente = 9;
update cliente set idmunicipio = 9 where idcliente in (14, 15);

select * from cliente

create table fornecedor(
	id_fornecedor integer not null,
	Nome varchar(50) not null,

	constraint pk_fnr_fornecedor primary key (id_fornecedor), 
	constraint un_fnr_nome unique (Nome)
);

insert into fornecedor (id_fornecedor, Nome) values (1, 'Cap. Computadores');
insert into fornecedor (id_fornecedor, Nome) values (2, 'AA. Computadores');
insert into fornecedor (id_fornecedor, Nome) values (3, 'BB. Maquinas');

select * from fornecedor

create table vendedor(
	id_vendedor integer not null,
	Nome varchar(50) not null,

	constraint pk_vnd_vendedor primary key (id_vendedor), 
	constraint un_vnd_nome unique (Nome)
);

insert into vendedor (id_vendedor, Nome) values (1, 'André');
insert into vendedor (id_vendedor, Nome) values (2, 'Alisson');
insert into vendedor (id_vendedor, Nome) values (3, 'José');
insert into vendedor (id_vendedor, Nome) values (4, 'Ailton');
insert into vendedor (id_vendedor, Nome) values (5, 'Maria');
insert into vendedor (id_vendedor, Nome) values (6, 'Suelem');
insert into vendedor (id_vendedor, Nome) values (7, 'Aline');
insert into vendedor (id_vendedor, Nome) values (8, 'Silvania');

select * from vendedor

create table transportadora(
	id_transportadora integer not null,
	id_municipio integer,
	nome varchar(50) not null,
	logradouro varchar(50),
	numero varchar(10),

	constraint pk_tpd_transportadora primary key (id_transportadora), 
	constraint fk_mcp_municipio foreign key (id_municipio) references municipio (idmunicipio),
	constraint un_cln_nome unique (nome)
);

insert into transportadora(id_transportadora, id_municipio, nome, logradouro, numero) values (1, 9, 'BS. Transportes', 'Rua das Limas', '01');
insert into transportadora(id_transportadora, id_municipio, nome, logradouro, numero) values (2, 5, 'União Transportes', null, null);

drop table transportadora
select * from transportadora

create table produto(
	id_produto integer not null,
	id_fornecedor integer not null,
	nome varchar(50) not null,
	valor numeric(10,2) not null,

	constraint pk_pdt_produto primary key (id_produto),
	constraint fk_fnc_fornecedor foreign key (id_fornecedor) references fornecedor (id_fornecedor)	
);

insert into produto (id_produto, id_fornecedor, nome, valor) values (1, 1, 'Microcomputador', 800);
insert into produto (id_produto, id_fornecedor, nome, valor) values (2, 1, 'Monitor', 500);
insert into produto (id_produto, id_fornecedor, nome, valor) values (3, 2, 'Placa mãe', 200);
insert into produto (id_produto, id_fornecedor, nome, valor) values (4, 2, 'HD', 150);
insert into produto (id_produto, id_fornecedor, nome, valor) values (5, 2, 'Placa de vídeo', 200);
insert into produto (id_produto, id_fornecedor, nome, valor) values (6, 1, 'Memória RAM', 100);
insert into produto (id_produto, id_fornecedor, nome, valor) values (7, 2, 'Gabinete', 35);

select * from produto

create table pedido(
	id_pedido integer not null,
	idcliente integer not null,
	id_transportadora integer,
	id_vendedor integer not null,
	date_pedido date not null, 
	valor float not null,

	constraint pk_pdd_idpedido primary key (id_pedido),
	constraint fk_pdd_idcliente foreign key (idcliente) references cliente (idcliente),
	constraint fk_pdd_idtransportadora foreign key (id_transportadora) references transportadora (id_transportadora),
	constraint fk_pdd_idvendedor foreign key (id_vendedor) references vendedor (id_vendedor) 
);

select * from pedido

insert into pedido (id_pedido, date_pedido, valor, idcliente, id_transportadora, id_vendedor) values (1, '2008-04-01', 1300, 1, 1, 1);
insert into pedido (id_pedido, date_pedido, valor, idcliente, id_transportadora, id_vendedor) values (2, '2008-04-01', 500, 1, 1, 1);
insert into pedido (id_pedido, date_pedido, valor, idcliente, id_transportadora, id_vendedor) values (3, '2008-04-02', 300, 11, 2, 5);
insert into pedido (id_pedido, date_pedido, valor, idcliente, id_transportadora, id_vendedor) values (4, '2008-04-05', 1000, 8, 1, 7);
insert into pedido (id_pedido, date_pedido, valor, idcliente, id_transportadora, id_vendedor) values (5, '2008-04-06', 200, 9, 2, 6);
insert into pedido (id_pedido, date_pedido, valor, idcliente, id_transportadora, id_vendedor) values (6, '2008-04-06', 1985, 10, 1, 6);
insert into pedido (id_pedido, date_pedido, valor, idcliente, id_transportadora, id_vendedor) values (7, '2008-04-06', 800, 3, 1, 7);
insert into pedido (id_pedido, date_pedido, valor, idcliente, id_transportadora, id_vendedor) values (8, '2008-04-06', 175, 3, null, 7);
insert into pedido (id_pedido, date_pedido, valor, idcliente, id_transportadora, id_vendedor) values (9, '2008-04-07', 1300, 12, null, 8);
insert into pedido (id_pedido, date_pedido, valor, idcliente, id_transportadora, id_vendedor) values (10, '2008-04-10', 200, 6, 1, 8);
insert into pedido (id_pedido, date_pedido, valor, idcliente, id_transportadora, id_vendedor) values (11, '2008-04-15', 300, 15, 2, 1);
insert into pedido (id_pedido, date_pedido, valor, idcliente, id_transportadora, id_vendedor) values (12, '2008-04-15', 300, 15, 2, 5);
insert into pedido (id_pedido, date_pedido, valor, idcliente, id_transportadora, id_vendedor) values (13, '2008-04-20', 350, 9, 1, 7);
insert into pedido (id_pedido, date_pedido, valor, idcliente, id_transportadora, id_vendedor) values (14, '2008-04-23', 300, 2, 1, 5);
insert into pedido (id_pedido, date_pedido, valor, idcliente, id_transportadora, id_vendedor) values (15, '2008-04-25', 200, 11, null, 5);
select * from pedido

create table pedido_produto (
	id_pedido integer not null, 
	id_produto integer not null,
	quantidade integer not null,
	valor_unitario float not null, 

	constraint pk_pdp_idpedidoproduto primary key (id_pedido, id_produto), 
	constraint fk_pdp_idpedido foreign key (id_pedido) references pedido (id_pedido),
	constraint fk_pdp_idproduto foreign key (id_produto) references  produto (id_produto)
);

insert into pedido_produto (id_pedido, id_produto, quantidade,  valor_unitario) values (1, 1, 1, 800);
insert into pedido_produto (id_pedido, id_produto, quantidade,  valor_unitario) values (1, 2, 1, 500);
insert into pedido_produto (id_pedido, id_produto, quantidade,  valor_unitario) values (2, 2, 1, 500);
insert into pedido_produto (id_pedido, id_produto, quantidade,  valor_unitario) values (3, 4, 2, 150);
insert into pedido_produto (id_pedido, id_produto, quantidade,  valor_unitario) values (4, 1, 1, 800);
insert into pedido_produto (id_pedido, id_produto, quantidade,  valor_unitario) values (4, 3, 1, 200);
insert into pedido_produto (id_pedido, id_produto, quantidade,  valor_unitario) values (5, 3, 1, 200);
insert into pedido_produto (id_pedido, id_produto, quantidade,  valor_unitario) values (6, 1, 2, 800);
insert into pedido_produto (id_pedido, id_produto, quantidade,  valor_unitario) values (6, 7, 1, 35);
insert into pedido_produto (id_pedido, id_produto, quantidade,  valor_unitario) values (6, 5, 1, 200);
insert into pedido_produto (id_pedido, id_produto, quantidade,  valor_unitario) values (6, 4, 1, 150);
insert into pedido_produto (id_pedido, id_produto, quantidade,  valor_unitario) values (7, 1, 1, 800);
insert into pedido_produto (id_pedido, id_produto, quantidade,  valor_unitario) values (8, 1, 5, 35);
insert into pedido_produto (id_pedido, id_produto, quantidade,  valor_unitario) values (9, 1, 1, 800);
insert into pedido_produto (id_pedido, id_produto, quantidade,  valor_unitario) values (9, 2, 1, 500);
insert into pedido_produto (id_pedido, id_produto, quantidade,  valor_unitario) values (10, 5, 1, 200);
insert into pedido_produto (id_pedido, id_produto, quantidade,  valor_unitario) values (11, 5, 1, 200);
insert into pedido_produto (id_pedido, id_produto, quantidade,  valor_unitario) values (11, 6, 1, 100);
insert into pedido_produto (id_pedido, id_produto, quantidade,  valor_unitario) values (12, 2, 1, 500);
insert into pedido_produto (id_pedido, id_produto, quantidade,  valor_unitario) values (13, 3, 1, 200);
insert into pedido_produto (id_pedido, id_produto, quantidade,  valor_unitario) values (13, 4, 1, 150);
insert into pedido_produto (id_pedido, id_produto, quantidade,  valor_unitario) values (14, 6, 3, 100);
insert into pedido_produto (id_pedido, id_produto, quantidade,  valor_unitario) values (15, 3, 1, 200);

--------------------------------------------------------------------------------------
-- exercicios pt 3

-- 1
select * from vendedor order by nome;

-- 2
select * from pedido where valor > 200 order by valor;

-- 3
select nome, valor, (valor * 1.1) as Acrescimo, (valor * 0.90) as Reducao from produto;

-- 4
select * from uf
select * from municipio where iduf = 5;

-- 5
select * from pedido;
select * from pedido where date_pedido between '2008-04-10' and '2008-04-25' order by valor;

-- 6 
select * from pedido where valor between 1000 and 1500 order by valor;

-- 7 
select * from pedido where valor not between 100 and 500 order by valor;

-- 8 
select * from vendedor
select * from pedido where id_vendedor = 1 order by valor desc;

-- 9 
select * from cliente
select * from pedido
select * from pedido where idcliente = 1 order by valor;

-- 10
select * from cliente
select * from pedido
select * from pedido where (id_vendedor = 1) and (idcliente = 15) order by valor desc;

-- 11
select * from transportadora
select * from pedido where (id_transportadora = 2);

-- 12
select * from vendedor
select * from pedido where id_vendedor in (5, 7) order by id_vendedor;

-- 13
select * from cliente
select * from municipio
select * from cliente where idmunicipio in (9, 1) order by idmunicipio;

-- 14
select * from cliente where idmunicipio not in (9, 1) order by idmunicipio;

-- 15
select * from cliente
select * from cliente where logradouro is null;

-- 16
select * from cliente where logradouro like ('Av%');

-- 17
select * from vendedor where nome like ('S%');

-- 18
select * from vendedor where nome like ('%a');

-- 19
select * from vendedor where nome not like ('%a');

-- 20
select * from uf
select * from municipio where nome like ('P%') and iduf = 1;

-- 21
select * from transportadora 
select * from transportadora where logradouro is null;

-- 22
select * from pedido_produto where id_pedido = 1;
select * from produto where id_produto in (1,2);
select * from produto

-- 23
select * from pedido_produto where id_pedido in (6,10);
-------------------------------------------------------------------------------------------------

-- Funçoes agregradas
select avg(valor) from pedido;

select count(idmunicipio) from municipio;

select count(*) from municipio;

select * from transportadora;
select count(logradouro) from transportadora;
select count(id_transportadora) from transportadora;

select * from municipio;
select count(idmunicipio) from municipio where iduf = 2;

select max(valor) from pedido;

select min(valor), max(valor) from pedido;

select sum(valor) from pedido 

select idcliente, valor from pedido;

select idcliente, sum(valor) from pedido group by idcliente;

select idcliente, sum(valor) from pedido group by idcliente having sum(valor) > 500;

-----------------------------------------------------------------------------------
-- 1
select avg(valor) from pedido group by id_vendedor having avg(valor) > 200;
select * from pedido;

-- 2
select id_vendedor, sum(valor) from pedido group by id_vendedor having sum(valor) > 1500;
 
-- 3
select id_vendedor, sum(valor) as soma from pedido group by id_vendedor;

-- 4
select count(municipio) from municipio;

-- 5
select count(idmunicipio) from municipio where iduf in (1,2);

-- 6 
select iduf from municipio group by iduf;
select * from uf;

-- 7
select logradouro from cliente group by logradouro having logradouro is not null;

-- 8
select count(idcliente) from cliente group by idmunicipio;
select * from cliente;

-- 9 
select count(id_fornecedor) from fornecedor;

-- 10
select * from produto where id_fornecedor = 1;    -- A tabela inteira do fornecedor especifico
select count(id_produto) from produto group by id_fornecedor; -- Ela mostra a contagem que foi pedida no exercicio

-- 11
select round(avg(valor), 2)  from produto group by id_fornecedor having id_fornecedor = 1;
select avg(valor) from produto group by id_fornecedor having id_fornecedor = 1;

select * from produto;

-- 12
select sum(valor) from pedido;

-- 13
select nome, valor from produto group by nome, valor order by valor desc limit 1;

-- 14
select nome, valor from produto group by nome, valor order by valor limit 1;

-- 15
select avg(valor) from produto;

-- 16
select count(id_transportadora) from transportadora;

-- 17
select avg(valor) from pedido;

-- 18
select idcliente, sum(valor) from pedido group by idcliente order by idcliente;
select * from pedido;

-- 19
select id_vendedor, sum(valor) from pedido group by id_vendedor order by id_vendedor;

-- 20 
select sum(valor) from pedido  group by id_transportadora;

-- 21
select * from pedido;
select sum(valor), date_pedido from pedido  group by date_pedido;

-- 22
select sum(valor) from pedido group by  idcliente, id_vendedor, id_transportadora;


-- 23
select sum(valor) from pedido group by date_pedido between '2008-04-01' and '2009-12-10' having sum(valor) > 200;

-- 24
select * from vendedor;
select * from pedido;
select avg(valor) from pedido group by id_vendedor = 1;

-- 25
select * from cliente 15
select avg(valor) from pedido group by idcliente = 15;

-- 26 
select count(id_transportadora = 1) from pedido;
select * from transportadora;

-- 27
select count(id_pedido) from pedido group by id_vendedor;

-- 28
select count(id_pedido) from pedido group by idcliente;

-- 29
select count(id_pedido) from pedido group by date_pedido between '2008-04-15' and '2008-04-25';

-- 30
select count(id_pedido) from pedido group by id_pedido having valor > 1000;

-- 31
select count(id_produto) from pedido_produto group by id_produto having id_produto = 1;
select * from produto

-- 32
select count(id_produto) from pedido_produto group by id_produto;

-- 33
select sum(valor_unitario) from pedido_produto group by id_pedido;

-- 34
select id_pedido, count(id_produto) from pedido_produto group by id_pedido order by id_pedido;
select * from pedido_produto

-- 35
select id_produto, sum(valor_unitario) from pedido_produto group by id_produto

-- 36
select avg(valor_unitario) from pedido_produto group by id_pedido having id_pedido = 6;

-- 37
select max(valor_unitario) from pedido_produto 

-- 38
select min(valor_unitario) from pedido_produto 

-- 39
select id_pedido, sum(id_produto) from pedido_produto group by id_pedido

-- 40
select sum(id_produto) from pedido_produto

-- Relacionamento com join
select 
	cln.nome,
	prf.nome
from 
	cliente as cln
left outer join 
	profissao as prf on cln.idprofissao = prf.idprofissao
------------
select 
	cln.nome as cliente,
	prf.nome as profissao
from 
	cliente as cln
inner join -- So mostra o que foi informado 
	profissao as prf on cln.idprofissao = prf.idprofissao
---------
select 
	cln.nome as cliente,
	prf.nome as profissao
from 
	cliente as cln
right outer join -- So mostra o que foi informado começando pela profissao
	profissao as prf on cln.idprofissao = prf.idprofissao
-------------------------------------------------
-- Exercicios 

-- 1. O nome do cliente, a profissão, a nacionalidade, o logradouro, o número, o complemento, o bairro, o município e a unidade de federação.
select
	cln.nome,
	prf.nome as profissao,
	ncd.nome as nacionalidade,
	cln.logradouro,
	cln.numero,
	cpt.nome as complemento,
	bro.nome as bairro,
	mnc.nome as municipio,
	uf.nome as uf
from
	cliente as cln
left outer join 
	profissao as prf on cln.idprofissao = prf.idprofissao
left outer join
	nacionalidade as ncd on cln.idnacionalidade = ncd.idnacionalidade
left outer join
	complemento as cpt on cln.idcomplemento = cpt.idcomplemento
left outer join
	bairro as bro on cln.idbairro = bro.idbairro
left outer join
	municipio as mnc on cln.idmunicipio = mnc.idmunicipio
left outer join
	uf on mnc.iduf = uf.iduf;

-- 2. O nome do produto, o valor e o nome do fornecedor.
select 
	pdd.nome as produto,
	pdd.valor as valor,
	fnr.nome as fornecedor

from 
produto as pdd
left outer join
	fornecedor as fnr on fnr.id_fornecedor = pdd.id_fornecedor
	
-- 3. O nome da transportadora e o município.
select
	tpa.nome as transportadora,
	mnc.nome as municipio
from
pedido as pdd
left outer join
	transportadora as tpa on pdd.id_transportadora = tpa.id_transportadora
left outer join 
	municipio as mnc on tpa.id_municipio = mnc.idmunicipio
group by tpa.nome, mnc.nome

-- 4. A data do pedido, o valor, o nome do cliente, o nome da transportadora e o nome do vendedor.
select 
	pdd.date_pedido as data_pedido,
	pdd.valor,
	tpa.nome as transportadora,
	nmv.nome as vendedor
from
	pedido as pdd
left outer join 
	transportadora as tpa on pdd.id_transportadora = tpa.id_transportadora
left outer join
	vendedor as nmv on pdd.id_vendedor = nmv.id_vendedor
-- 5. O nome do produto, a quantidade e o valor unitário dos produtos do pedido.
select 
	pdp.id_pedido,
	ndp.nome,
	pdp.quantidade,
	pdp.valor_unitario
from 
pedido_produto as pdp
left outer join
	produto as ndp on pdp.id_produto = ndp.id_produto

-- 6. O nome dos clientes e a data do pedido dos clientes que fizeram algum pedido (ordenado pelo nome do cliente).
select 
	cln.nome,
	pdd.date_pedido
from pedido as pdd
left outer join
	cliente as cln on pdd.idcliente = cln.idcliente
order by cln.nome

-- 7. O nome dos clientes e a data do pedido de todos os clientes, independente se tenham feito pedido (ordenado pelo nome do cliente).
select 
	cln.nome,
	pdd.date_pedido
from pedido as pdd
left outer join
	cliente as cln on pdd.idcliente = cln.idcliente
order by cln.nome

-- 8. O nome da cidade e a quantidade de clientes que moram naquela cidade.
select 
	count(idcliente),
	mnc.nome as cidade
from cliente as cln
left outer join 
	municipio as mnc on cln.idmunicipio = mnc.idmunicipio
group by mnc.idmunicipio

-- 9. O nome do fornecedor e a quantidade de produtos de cada fornecedor.
select 
	fnr.nome,
	count(id_produto)
from produto as pdt
left outer join
	fornecedor as fnr on pdt.id_fornecedor = fnr.id_fornecedor
group by fnr.id_fornecedor
	
-- 10. O nome do cliente e o somatório do valor do pedido (agrupado por cliente).
select 
	cln.nome,
	sum(valor) as soma
from pedido as pdd
left outer join
	cliente as cln on pdd.idcliente = cln.idcliente
group by cln.idcliente

-- 11.O nome do vendedor e o somatório do valor do pedido (agrupado por vendedor).
select 
	vdr.nome as vendedor,
	sum(valor) as soma
from pedido as pdd
left outer join
	vendedor as vdr on pdd.id_vendedor = vdr.id_vendedor
group by vdr.id_vendedor
order by vdr.nome

-- 12.O nome da transportadora e o somatório do valor do pedido (agrupado por transportadora).
select 
	tpa.nome,
	sum(valor)
from 
pedido as pdd
left outer join 
	transportadora as tpa on pdd.id_transportadora  = tpa.id_transportadora
group by tpa.nome

-- 13.O nome do cliente e a quantidade de pedidos de cada um (agrupado por cliente).
select 
	cln.nome,
	sum(valor)
from 
pedido as pdd
left outer join 
	cliente as cln on pdd.idcliente  = cln.idcliente
group by cln.nome

-- 14.O nome do produto e a quantidade vendida (agrupado por produto).
select 
	pdt.nome,
	count(id_pedido)
from pedido_produto as pdd
left outer join
	produto as pdt on pdd.id_produto = pdt.id_produto
group by 
	pdt.nome

-- 15.A data do pedido e o somatório do valor dos produtos do pedido (agrupado pela data do pedido).
select 
	date_pedido,
	sum(valor)
from pedido
group by
	date_pedido
order by 
	date_pedido

-- 16.A data do pedido e a quantidade de produtos do pedido (agrupado pela data do pedido).
select 
	pdd.date_pedido,
	count(pdp.id_produto)
from 
	pedido_produto as pdp
left outer join
	pedido as pdd on pdd.id_pedido = pdp.id_pedido
group by
	pdd.date_pedido

-------------------------------------------------------------------------------------------------------------
-- Comandos adicionais --
select * from pedido
select 
	date_pedido,
	extract(day from date_pedido),
	extract(month from date_pedido),
	extract(year from date_pedido)
from
	pedido

----
select
	nome,
	substring(nome from 1 for 5), substring(nome , 2)
from 
	cliente

----
select
	nome, 
	upper(nome)
from
	cliente
----
select nome, coalesce (cpf, 'Não foi informado') as cpf from cliente

----
select 
	case sigla
		when 'PR' then 'Paraná'
		when 'SC' then 'Santa Catarina'
	else
		'Outros'
	end as uf
from uf
---------------------------------------------------------------------------------------
-- 1. O nome do cliente e somente o mês de nascimento.
-- 1. Caso a data de nascimento não esteja preenchida mostrar a mensagem “Não informado”.
select 
	nome,
	data_nascimento,
	extract(month from data_nascimento) as mes,
	coalesce(cast(extract(month from data_nascimento)as text),'Não informado')
from 
	cliente

-- 2. O nome do cliente e somente o nome do mês de nascimento (Janeiro, Fevereiro etc). Caso a data de nascimento não esteja preenchida mostrar a mensagem “Não informado”.
select 
	nome,
	case(extract(month from data_nascimento))
		when 01 then 'Janeiro'
		when 02 then 'Fevereiro'
		when 03 then 'Março'
		when 04 then 'Abril'
		when 05 then 'Maio'
		when 06 then 'Junho'
		when 07 then 'Julho'
		when 08 then 'Agosto'
		when 09 then 'Setembro'
		when 10 then 'Otubro'
		when 11 then 'Novembro'
		when 12 then 'Dezembro'
	else 'Não informado'
		end as "Mes de nascimento"
from 
	cliente;
-- 4. O caractere 5 até o caractere 10 de todos os municípios.
select
	nome,
	substring(nome from 5 for 10)
from 
	municipio
	
-- 5. O nome de todos os municípios em letras maiúsculas.
select
	nome, 
	upper(nome)
from
	municipio

-- 6. O nome do cliente e o gênero. Caso seja M mostrar “Masculino”, senão mostrar “Feminino”.
select
	nome,
	case genero
		when 'M' then 'Masculino'
		when 'F' then 'Feminino'
	end as genero
from
	cliente

-- 7. O nome do produto e o valor. Caso o valor seja maior do que R$ 500,00 mostrar a mensagem “Acima de 500”, caso contrário, mostrar a mensagem “Abaixo de 500”.
select 
	nome,
	valor,
	case 
		when valor > 500 then 'Acima de 500'
	else 'Abaixo de 500'
	end as valor
from
	produto;
	
	
select * from pedido_produto
select * from produto

----------------------------------------------------------------------------------------------------------
-- Subconsultas
select 
	date_pedido,
	valor
from
	pedido
where
	valor > (select avg(valor) from pedido)

-----------
select 
	pdd.date_pedido,
	pdd.valor,
	(select sum(quantidade) from pedido_produto as pdp where pdp.id_pedido = pdd.id_pedido)
from 
	pedido as pdd
-----------
select * from pedido

update pedido set valor = valor + ((valor * 5) / 100)
where valor > (select avg(valor) from pedido)
----------
-- 1. O nome dos clientes que moram na mesma cidade do Manoel. Não deve ser mostrado o Manoel.
select 
	nome,
	idmunicipio
from
	cliente
where
	idmunicipio = (select idmunicipio from cliente where nome = 'Garcia2')
and 
	idcliente <> 1
-- 2. A data e o valor dos pedidos que o valor do pedido seja menor que a média de todos os pedidos.
select
	date_pedido,
	valor
from pedido 
where
	valor < (select avg(valor) from pedido)

-- 3. A data,o valor, o cliente e o vendedor dos pedidos que possuem 2 ou mais produtos.
SELECT
	DATE_PEDIDO,
	VALOR,
	CLN.NOME AS CLIENTE,
	VDD.NOME AS VENDEDOR,
	(
		SELECT
			SUM(QUANTIDADE)
		FROM
			PEDIDO_PRODUTO AS PDP
		WHERE
			PDP.ID_PEDIDO = PDD.ID_PEDIDO
	)
FROM
	PEDIDO AS PDD
	LEFT OUTER JOIN CLIENTE AS CLN ON PDD.IDCLIENTE = CLN.IDCLIENTE
	LEFT OUTER JOIN VENDEDOR AS VDD ON PDD.ID_VENDEDOR = VDD.ID_VENDEDOR
WHERE
	(
		SELECT
			SUM(QUANTIDADE)
		FROM
			PEDIDO_PRODUTO AS PDP
		WHERE
			PDP.ID_PEDIDO = PDD.ID_PEDIDO
	) >= 2

-- 4. O nome dos clientes que moram na mesma cidade da transportadora BSTransportes.
select 
	nome
from
	cliente
where
	cliente.idmunicipio = (
	select 
		id_municipio 
	from 
		transportadora as tpa
	where 
		tpa.nome = 'BS. Transportes'
	);
	
-- 5. O nome do cliente e o município dos clientes que estão localizados no mesmo município de qualquer uma das transportadoras.
select 
	cln.nome,
	mnc.nome as municipio
from cliente as cln
left outer join 
	municipio as mnc on cln.idmunicipio = mnc.idmunicipio
where
	cln.idmunicipio = (
	select 
		id_municipio 
	from 
		transportadora as tpa
	where 
		cln.idmunicipio = tpa.id_municipio);


select * from transportadora
select count(idmunicipio = 9 ) from cliente where idmunicipio = 9 


-- 6. Atualizar o valor do pedido em 5% para os pedidos que o somatório do valor total dos produtos daquele pedido seja maior que a média do valor total

	-- Não consegui fazer pq o cara do video fez uma bagunça la

-- 7. O nome do cliente e a quantidade de pedidos feitos pelo cliente.
select
	cln.nome,
	(select
		count(id_pedido)
	from 
		pedido as pdd
	where pdd.idcliente = cln.idcliente) as total
from 
	cliente as cln
	
select * from pedido

-- 8. Para revisar, refaça o exercício anterior (número 07) utilizando group by e mostrando somente os clientes que fizeram pelo menos um pedido.
select
	cln.nome as cliente,
	count(pdd.id_pedido) as total
from 
	pedido as pdd
left outer join 
	cliente as cln on pdd.idcliente = cln.idcliente
group by 
	cln.nome
----------------------------------------------------------------------------------------------------------------------------
-- Viewes 
drop view cliente_profissao;


create view cliente_profissao as
select 
	cln.nome as cliente,
	cln.cpf,  
	prf.nome as profissao
from
	cliente as cln
left outer join
	profissao as prf on cln.idprofissao = prf.idprofissao
 
select cpf from cliente_profissao where profissao = 'Professor'

----------------------------------------------
-- 1. O nome, a profissão, a nacionalidade, o complemento, o município, a unidade de federação, o bairro, o CPF,o RG, a data de nascimento, o gênero (mostrar “Masculino” ou “Feminino”), o logradouro, o número e as observações dos clientes.
create view dados_completos as
select 
	cln.nome as nome,
	prf.nome as profissao,
	ncd.nome as nacionalidade,
	mnc.nome as municipio,
	uf.nome as uf,
	brr.nome as bairro,
	cln.cpf as cpf,
	cln.rg as rg,
	cln.data_nascimento,
	case genero
		when 'M' then 'Masculino'
		when 'F' then 'Feminino'
	end as genero,
	cln.logradouro,
	cln.numero,
	cln.obseracoes
from 
	cliente as cln
left outer join 
	profissao as prf on cln.idprofissao = prf.idprofissao
left outer join
	nacionalidade as ncd on cln.idnacionalidade = ncd.idnacionalidade
left outer join
	municipio as mnc on cln.idmunicipio = mnc.idmunicipio
left outer join
	uf as uf on mnc.iduf = uf.iduf
left outer join
	bairro as brr on cln.idbairro = brr.idbairro
----
-- 2. O nome do município e o nome e a sigla da unidade da federação.
create view dados_localizacao as
select 
	mnc.nome as municipio,
	cln.nome as cliente,
	uf.nome as uf
from cliente as cln
left outer join
	municipio as mnc on cln.idmunicipio = mnc.idmunicipio
left outer join
	uf on mnc.iduf = uf.iduff
	
----
-- 3. O nome do produto, o valor e o nome do fornecedor dos produtos.
create view dados_produto as
select 
	pdt.nome as produto,
	pdt.valor as valor,
	fnc.nome as fornecedor
from 
	produto as pdt
left outer join
	fornecedor as fnc on pdt.id_fornecedor = fnc.id_fornecedor
----
-- 4. O nome da transportadora, o logradouro, o número, o nome da unidade de federação e a sigla da unidade de federação das transportadoras.
create view dados_transportadora as
select 
	tpa.nome as transportadora,
	tpa.logradouro,
	tpa.numero,
	uf.nome as federacao,
	uf.sigla as sigla
from 
	transportadora as tpa
left outer join
	municipio as mnc on tpa.id_municipio = mnc.idmunicipio
left outer join
	uf on mnc.iduf = uf.iduf
----
-- 5. A data do pedido, o valor, o nome da transportadora, o nome do cliente e o nome do vendedor dos pedidos.
create view dados_pedido as
select
	pdd.date_pedido as data_pedido,
	pdd.valor as valor,
	cln.nome as cliente,
	vdd.nome as vendedor
from 
	pedido as pdd
left outer join 
	cliente as cln on pdd.idcliente = cln.idcliente
left outer join
	vendedor as vdd on pdd.id_vendedor = vdd.id_vendedor

----
-- 6. O nome do produto, a quantidade, o valor unitário e o valor total dos produtos do pedido.
create view dados_pedido_produto as 
select 
	prd.nome as produto,
	pdp.quantidade,
	pdp.valor_unitario
from
	pedido_produto as pdp
left outer join
	produto prd on pdp.id_produto = prd.id_produto
-------------------------------------------------------------------------------------------------------------------
-- Campos autoincriemento
select * from cliente

create table exemplo (
	idexemplo serial not null,
	nome varchar(50) not null,

	constraint pk_exemplo_idexemplo primary key (idexemplo)
);

insert into exemplo (nome) values
	('Exemplo 1'),
	('Exemplo 2'),
	('Exemplo 3'),
	('Exemplo 4'),
	('Exemplo 5');

select * from exemplo
----
select * from bairro
select max(idbairro) +1 from bairro 
create sequence bairro_id_seq minvalue 5
alter table bairro alter idbairro set default nextval('bairro_id_seq')
alter sequence bairro_id_seq owned by bairro.idbairro

insert into bairro (nome) values
	('Teste 1'),
	('Teste 2');

select * from bairro
----
-- 1. Criar sequências para todas as outras tabelas da base de dados
-- Cliente
select * from cliente
select max(idcliente) +1 from cliente
create sequence cliente_id_seq minvalue 18
alter table cliente alter idcliente set default nextval('cliente_id_seq')
alter sequence cliente_id_seq owned by cliente.idcliente

----
-- Complemento
select * from complemento
select max(idcomplemento) +1 from complemento
create sequence complemento_id_seq minvalue 3
alter table complemento alter idcomplemento set default nextval('complemento_id_seq')
alter sequence complemento_id_seq owned by complemento.idcomplemento

----
-- Fornecedor
select * from fornecedor
select max(id_fornecedor) +1 from fornecedor
create sequence fornecedor_id_seq minvalue 4
alter table fornecedor alter id_fornecedor set default nextval('fornecedor_id_seq')
alter sequence fornecedor_id_seq owned by fornecedor.id_fornecedor

----
-- Município
select * from municipio
select max(idmunicipio) +1 from municipio
create sequence municipio_id_seq minvalue 10
alter table municipio alter idmunicipio set default nextval('municipio_id_seq')
alter sequence municipio_id_seq owned by municipio.idmunicipio

----
-- Nacionalidade
select * from nacionalidade
select max(idnacionalidade) +1 from nacionalidade
create sequence nacionalidade_id_seq minvalue 5
alter table nacionalidade alter idnacionalidade set default nextval('nacionalidade_id_seq')
alter sequence nacionalidade_id_seq owned by nacionalidade.idnacionalidade

----
-- Pedido
select * from pedido
select max(id_pedido) +1 from pedido
create sequence pedido_id_seq minvalue 16
alter table pedido alter id_pedido set default nextval('pedido_id_seq')
alter sequence pedido_id_seq owned by pedido.id_pedido

----
-- g. Pedido produto (verificar se é necessário)
-
-
-
-
-

----
-- Profissão
select * from profissao
select max(idprofissao) +1 from profissao
create sequence profissao_id_seq minvalue 6
alter table profissao alter idprofissao set default nextval('profissao_id_seq')
alter sequence profissao_id_seq owned by profissao.idprofissao

----
-- Transportadora
select * from transportadora
select max(id_transportadora) +1 from transportadora
create sequence transportadora_id_seq minvalue 3
alter table transportadora alter id_transportadora set default nextval('transportadora_id_seq')
alter sequence transportadora_id_seq owned by transportadora.id_transportadora

----
-- UF
select * from uf
select max(iduf) +1 from uf
create sequence uf_id_seq minvalue 7
alter table uf alter iduf set default nextval('uf_id_seq')
alter sequence uf_id_seq owned by uf.iduf

----
-- Vendedor
select * from vendedor
select max(id_vendedor) +1 from vendedor
create sequence vendedor_id_seq minvalue 9
alter table vendedor alter id_vendedor set default nextval('vendedor_id_seq')
alter sequence vendedor_id_seq owned by vendedor.id_vendedor

----
-- Produto
select * from produto
select max(id_produto) +1 from produto
create sequence produto_id_seq minvalue 8
alter table produto alter id_produto set default nextval('produto_id_seq')
alter sequence produto_id_seq owned by produto.id_produto
--------------------------------------------------------------------------------------------------
-- Campos Default
alter table pedido alter column date_pedido set default current_date;
alter table pedido alter column valor set default 0;
insert into pedido (idcliente, id_vendedor) values (1,1)
insert into pedido (idcliente, id_vendedor,date_pedido, valor)
values (1, 1, '2022-10-10', 234);
select * from pedido
--------
--- 1. Adicione valores default na tabela de produtos do pedido
-- Quantidade com o valor 1
-- Valor unitário com o valor 0
alter table pedido_produto alter column quantidade set default 1;
alter table pedido_produto alter column valor_unitario set default 0;

insert into pedido_produto (id_pedido, id_produto) values (1, 3)
insert into pedido_produto (id_pedido, id_produto, quantidade, valor_unitario)
values (1, 4, 5, 100)
select * from pedido_produto

---- 2. Adicione valor default na tabela de produtos
--- a. Valor com o valor 0 
alter table produto alter column valor set default 0;
insert into produto (nome, id_fornecedor, valor) values ('Teste default 1', 1, 50)

select * from produto
----------------------------------------------------------------------------------------------------------------
-- Índices
create index idx_cln_nome on cliente (nome);

----
--- 1. Adicione índices nas seguintes tabelas e campos
-- a. Pedido – data do pedido
-- b. Produto – nome
create index idx_pdd_date_pedido on pedido (date_pedido)
create index idx_pdr_nome on produto (nome)






















































































