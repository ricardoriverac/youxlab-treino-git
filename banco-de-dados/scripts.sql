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

select * from cliente;

alter table cliente drop nacionalidade;
alter table cliente add idnacionalidade int;
alter table cliente add constraint fk_cln_idnacionalidade foreign key (idnacionalidade) references nacionalidade;
update cliente set idnacionalidade = 1 where idcliente in (1, 2, 3, 4, 6, 10, 11, 14);
update cliente set idnacionalidade = 2 where idcliente in (5, 7);
update cliente set idnacionalidade = 3 where idcliente = 8;
update cliente set idnacionalidade = 4 where idcliente in (9, 13);

select * from cliente;
alter table cliente drop complemento;
alter table cliente add idcomplemento int;
alter table cliente add constraint fk_cln_idcomplemento foreign key (idcomplemento) references complemento (idcomplemento);
update cliente set idcomplemento = 1 where idcliente in (1, 4, 9, 13);
update cliente set idcomplemento = 2 where idcliente in (2, 3, 7);

select * from cliente;
alter table cliente drop bairro;
alter table cliente add idbairro int;
alter table cliente add constraint fk_cln_idbairro foreign key (idbairro) references bairro (idbairro);

select * from bairro
update cliente set idbairro = 1 where idcliente in (1, 12, 13);
update cliente set idbairro = 2 where idcliente in (2, 3, 6, 8, 9);
update cliente set idbairro = 3 where idcliente in (4, 5);
update cliente set idbairro = 4 where idcliente = 7;

select * from cliente;
create table uf (
	iduf int not null,
	nome varchar(30) not null,
	sigla char(2) not null,
	
	constraint pk_ufd_idunidade_federacao primary key (iduf),
	constraint un_ufd_nome unique (nome),
	constraint un_ufd_sigla unique (sigla)
);

insert into uf (iduf, nome, sigla) values (1, 'Santa Catarina', 'SC');
insert into uf (iduf, nome, sigla) values (2, 'Paraná', 'PR');
insert into uf (iduf, nome, sigla) values (3, 'São Paulo', 'SP');
insert into uf (iduf, nome, sigla) values (4, 'Minas Gerais', 'MG');
insert into uf (iduf, nome, sigla) values (5, 'Rio Grande do Sul', 'RS');
insert into uf (iduf, nome, sigla) values (6, 'Rio de Janeiro', 'RJ');
select * from uf

create table municipio (
	idmunicipio int not null,
	nome varchar(30) not null,
	iduf int not null,

	constraint pk_mnc_idmunicipio primary key (idmunicipio),
	constraint un_mnc_nome unique (nome),
	constraint fk_mnc_iduf foreign key (iduf) references uf (iduf)
);

insert into municipio (idmunicipio, nome, iduf) values(1, 'Porto União', 1);
insert into municipio (idmunicipio, nome, iduf) values(2, 'Canoinhas', 1);
insert into municipio (idmunicipio, nome, iduf) values(3, 'Porto Vitória', 2);
insert into municipio (idmunicipio, nome, iduf) values(4, 'General Carneiro', 2);
insert into municipio (idmunicipio, nome, iduf) values(5, 'São Paulo', 3);
insert into municipio (idmunicipio, nome, iduf) values(6, 'Rio de Janeiro', 6);
insert into municipio (idmunicipio, nome, iduf) values(7, 'Uberlândia', 4);
insert into municipio (idmunicipio, nome, iduf) values(8, 'Porto Alegre', 5);
insert into municipio (idmunicipio, nome, iduf) values(9, 'União da Vitória', 2);
select * from municipio;

select * from cliente;

alter table cliente drop municipio;
alter table cliente drop uf;
alter table cliente add idmunicipio int;
alter table cliente add constraint fk_cln_idmunicipio foreign key (idmunicipio) references municipio (idmunicipio);

update cliente set idmunicipio = 1 where idcliente in (1, 2, 10, 11);
update cliente set idmunicipio = 2 where idcliente in (3, 12);
update cliente set idmunicipio = 3 where idcliente = 4;
update cliente set idmunicipio = 4 where idcliente = 5;
update cliente set idmunicipio = 5 where idcliente in (6,13);
update cliente set idmunicipio = 6 where idcliente = 7;
update cliente set idmunicipio = 7 where idcliente = 8;
update cliente set idmunicipio = 8 where idcliente = 9;
update cliente set idmunicipio = 9 where idcliente in (14, 15);

select * from cliente

-- EXERCICIOS
-- Criação de outras tabelas 2

-- Fornecedor
create table fornecedor (
	idfornecedor int not null,
	nome varchar(50) not null,

	constraint pk_fnc_idfornecedor primary key (idfornecedor),
	constraint un_fnc_nome unique (nome)
);

select * from fornecedor;

insert into fornecedor (idfornecedor, nome) values (1, 'Cap. Computadores');
insert into fornecedor (idfornecedor, nome) values (2, 'AA. Computadores');
insert into fornecedor (idfornecedor, nome) values (3, 'BB. Máquinas');

-- Vendedor
create table vendedor (
	idvendedor int not null,
	nome varchar(50) not null,

	constraint pk_vdr_idvendedor primary key (idvendedor),
	constraint un_vdr_nome unique (nome)
);
select * from vendedor;

insert into vendedor (idvendedor, nome) values (1, 'André');
insert into vendedor (idvendedor, nome) values (2, 'Alisson');
insert into vendedor (idvendedor, nome) values (3, 'José');
insert into vendedor (idvendedor, nome) values (4, 'Ailton');
insert into vendedor (idvendedor, nome) values (5, 'Maria');
insert into vendedor (idvendedor, nome) values (6, 'Suelem');
insert into vendedor (idvendedor, nome) values (7, 'Aline');
insert into vendedor (idvendedor, nome) values (8, 'Silvana');

-- Transportadora
create table transportadora (
	idtransportadora int not null,
	idmunicipio int,
	nome varchar(50) not null,
	logradouro varchar(50),
	numero varchar(10),

	constraint pk_tpd_idtransportadora primary key (idtransportadora),
	constraint fk_tpd_idmunicipio foreign key (idmunicipio) references municipio (idmunicipio),
	constraint un_tpf_nome unique (nome)
);
select * from transportadora;

select * from municipio;
insert into transportadora (idtransportadora, idmunicipio, nome, logradouro, numero) values (1, 1, 'BS. Transportes', 'Rua das Limas', 01);
insert into transportadora (idtransportadora, idmunicipio, nome, logradouro, numero) values (2, 5, 'União Transportes', null, null);

-- Produto
create table produto (
	idproduto int not null,
	idfornecedor int not null,
	nome varchar(50) not null,
	valor numeric(10,2) not null,

	constraint pk_pdt_idproduto primary key (idproduto),
	constraint fk_pdt_idfornecedor foreign key (idfornecedor) references fornecedor (idfornecedor)
);
select * from fornecedor;
select * from produto;
insert into produto (idproduto, idfornecedor, nome, valor) values (1, 1, 'Microcomputador', 800);
insert into produto (idproduto, idfornecedor, nome, valor) values (2, 1, 'Monitor', 500);
insert into produto (idproduto, idfornecedor, nome, valor) values (3, 2, 'Placa mãe', 200);
insert into produto (idproduto, idfornecedor, nome, valor) values (4, 2, 'HD', 150);
insert into produto (idproduto, idfornecedor, nome, valor) values (5, 2, 'Placa de vídeo', 200);
insert into produto (idproduto, idfornecedor, nome, valor) values (6, 3, 'Memória RAM', 100);
insert into produto (idproduto, idfornecedor, nome, valor) values (7, 1, 'Gabinete', 35);

-- FIM

create table pedido (
	idpedido int not null,
	idcliente int not null,
	idtransportadora int,
	idvendedor int not null,
	data_pedido date not null,
	valor numeric (10,2) not null,

	constraint pk_pdd_idpedido primary key (idpedido),
	constraint fk_pdd_idcliente foreign key (idcliente) references cliente (idcliente),
	constraint fk_pdd_idtransportadora foreign key (idtransportadora) references transportadora (idtransportadora),
	constraint fk_pdd_idvendedor foreign key (idvendedor) references vendedor (idvendedor)
);
select * from cliente
select * from transportadora
select * from vendedor

insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (1, '2008-04-01', 1300, 1, 1, 1);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (2, '2008-04-01', 500, 1, 1, 1);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (3, '2008-04-02', 300, 11, 2, 5);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (4, '2008-04-05', 1000, 8, 1, 7);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (5, '2008-04-06', 200, 9, 2, 6);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (6, '2008-04-06', 1985, 10, 1, 6);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (7, '2008-04-06', 800, 3, 1, 7);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (8, '2008-04-06', 175, 3, null, 7);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (9, '2008-04-07', 1300, 12, null, 8);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (10, '2008-04-10', 200, 6, 1, 8);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (11, '2008-04-15', 300, 15, 2, 1);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (12, '2008-04-20', 500, 15, 2, 5);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (13, '2008-04-20', 350, 9, 1, 7);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (14, '2008-04-23', 300, 2, 1, 5);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (15, '2008-04-25', 200, 11, null, 5);

select * from pedido;

create table pedido_produto (
	idpedido int not null,
	idproduto int not null,
	quantidade int not null,
	valor_unitario numeric(10,2) not null,

	constraint pk_pdp_idpedidoproduto primary key (idpedido, idproduto),
	constraint fk_pdp_idpedido foreign key (idpedido) references pedido (idpedido),
	constraint fk_pdp_idproduto foreign key (idproduto) references produto (idproduto)
);

select * from produto;
select * from pedido_produto;

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(1, 1, 1 , 800);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(1, 2, 1 , 500);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(2, 2, 1 , 500);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(3, 4, 2, 150);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(4, 1, 1 , 800);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(4, 3, 1 , 200);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(5, 3, 1 , 200);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(6, 1, 2, 800);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(6, 7, 1, 35);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(6, 5, 1, 200);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(6, 4, 1, 150);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(7, 1, 1, 800);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(8, 7, 5, 35);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(9, 1, 1, 800);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(9, 2, 1, 500);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(10, 5, 1, 200);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(11, 5, 1, 200);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(11, 6, 1, 100);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(12, 2, 1, 500);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(13, 3, 1, 200);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(13, 4, 1, 150);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(14, 6, 3, 100);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(15, 3, 1, 200);

-- EXERCICIOS
-- Consulta simples

-- 1
select nome from vendedor order by nome asc;

-- 2
select * from produto where valor > 200 order by valor asc; 

-- 3
select nome, valor, valor * 1.1 as "Valor Reajustado" from produto order by nome;

-- 4
select * from uf;
select * from municipio where iduf = 5; 

-- 5
select * from pedido;
select * from pedido where data_pedido between '2008-04-10' and '2008-04-25' order by valor;

-- 6
select * from pedido where valor between 1000 and 1500;

-- 7
select * from pedido where valor not between 100 and 500;

-- 8
select * from vendedor;
select * from pedido;
select * from pedido where idvendedor = 1 order by valor desc;

-- 9
select * from cliente;
select * from pedido where idcliente = 1 order by valor asc;

-- 10
select * from vendedor;
select * from pedido where idcliente = 15 and idvendedor = 1;

-- 11
select * from pedido where idtransportadora = 2;

-- 12
select * from vendedor;
select * from pedido where idvendedor in (5, 7);

-- 13
select * from cliente;
select 