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
























































































































