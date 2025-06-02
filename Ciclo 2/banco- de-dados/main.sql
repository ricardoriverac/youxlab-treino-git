create table cliente (
idcliente int not null,
nome varchar(50) not null, -- varchar: nome pode ter no máximo 50 Letras
cpf char(11), -- char: cpf tem que ter 11 algarismos
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

select nome, data_nascimento as "Data de nascimento" from cliente;

select 'CPF: ' || cpf || ' RG: ' || rg as "CPF e RG" from cliente;

select * from cliente limit 6;

select nome, data_nascimento from cliente where data_nascimento = '2001-01-01';

select nome from cliente where nome like 'C%';

select nome from cliente where nome like '%c%';

select nome, data_nascimento from cliente where data_nascimento between '1990-01-01' and '1998-01-01';

--Exercícios – consultas simples

--1
select nome, profissao, genero from cliente order by nome asc;

--2
select nome from cliente where nome like '%r%' or nome like '%R%';

--3
select nome from cliente where nome like '%c%'	

--4
select nome from cliente where nome like '&A&'

--5
select nome from cliente where bairro in ('Centro','cto.', 'ctr.')

--6
select nome from cliente where complemento like '&a&'

--7
select nome from cliente where genero in ('F')

--8
select nome from cliente where cpf is null;

--9
select nome, profissao from cliente order by profissao asc;

--10
select nome from cliente where nacionalidade in ('Brasileira', 'Brasileiro')

--11
select nome from cliente where numero is not null;

--12
select nome from cliente where uf like 'SC';

--13
select nome, data_nascimento from cliente where data_nascimento between '2000-01-01' and '2002-01-01';

--14
select 'nome: ' || nome || ' logradouro: '|| logradouro ||' numero: ' || numero ||' complemento: ' || complemento || 'bairro:' || bairro || 'municipio:' || municipio ||uf as registro from cliente;

--end

select * from cliente;

update cliente set nome = 'Teste' where idcliente = 1;

update cliente set nome = 'Adriano', genero = 'M', numero = '241' where idcliente = 4;

insert into cliente (idcliente, nome) values (16, '	João')

delete from cliente where idcliente = 16;

--Exercícios – comandos update e delete

--1
insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, municipio, uf)
values (16, 'Maicon', '12349596421', '1234', '1965-10-10', 'F', 'Empresário', 'Florianópolis', 'SC');

insert into cliente (idcliente, nome, rg, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (17, 'Getúlio', '4631', 'F', 'Estudante', 'Brasileira', 'Rua Central', '343', 'Apartamento', 'Centro', 'Curitiba', 'PR')

insert into cliente (idcliente, nome, genero, profissao, nacionalidade, numero, complemento)
values (18, 'Sandra', 'M', 'Professor', 'Italiana', '12', 'Bloco A')

--2
update cliente set cpf = '45390569432', genero = 'M', nacionalidade = 'Brasileira', UF ='SC'

--3
update cliente set data_nascimento = '01/04/1978', genero = 'M'

--4
update cliente set genero = 'F', profissao = 'Professora', numero = '123'

--5
delete from cliente where idcliente = 18;

--6
delete from cliente where idcliente = 16;
--end

create table profissao (
idprofissao integer not null,
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
idnacionalidade integer not null,
nome varchar(30) not null,

constraint pk_ncn_idnacionalidade primary key (idnacionalidade),
constraint un_ncn_nome unique (nome)

);

insert into nacionalidade (idnacionalidade, nome) values (1, 'Brasileira');

insert into nacionalidade (idnacionalidade, nome) values (2, 'Italiana');

insert into nacionalidade (idnacionalidade, nome) values (3, 'Norte-Americana');

insert into nacionalidade (idnacionalidade, nome) values (4, 'Alemã');

select * from nacionalidade

--Arrumando erro cometido--
update cliente set  data_nascimento = '2001-01-30' where idcliente = 1;

update cliente set  data_nascimento = '1987-01-04' where idcliente = 2;	

update cliente set  data_nascimento = '1967-10-01' where idcliente = 3;

update cliente set  data_nascimento = '1989-09-10' where idcliente = 4;

update cliente set  data_nascimento = '1991-03-04' where idcliente = 5;

update cliente set  data_nascimento = '2000-01-01' where idcliente = 6;

update cliente set  data_nascimento = null where idcliente = 7;

update cliente set  data_nascimento = '2001-10-10' where idcliente = 8;

update cliente set  data_nascimento = null where idcliente = 9;

update cliente set  data_nascimento = null where idcliente = 10;

update cliente set  data_nascimento = null where idcliente = 11;

update cliente set  data_nascimento = '2000-02-10' where idcliente = 12;

update cliente set  data_nascimento = null where idcliente = 13;

update cliente set  data_nascimento = '1983-07-01' where idcliente = 14;

update cliente set  data_nascimento = null where idcliente = 15;
--end

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
nome varchar (30) not null,

constraint pk_brr_idbairro primary key (idbairro),
constraint un_brr_nome unique (nome)
);

insert into bairro (idbairro, nome) values (1, 'Cidade Nova');

insert into bairro (idbairro, nome) values (2, 'Centro');

insert into bairro (idbairro, nome) values (3, 'São Pedro');

insert into bairro (idbairro, nome) values (4, 'Santa Rosa');

select * from bairro

select * from cliente;

alter table cliente rename column profissao to idprofissao;

alter table cliente alter column idprofissao type integer; 

--Estudantes -> 1, 9, 10, 12, 15, 17
--Engenheiro -> 2
--Pedreiro -> 3
--Jornalista -> 4, 5
--Professor -> 6, 7, 8, 13
--Null -> 11,14

alter table cliente drop idprofissao;

select * from cliente

alter table cliente add idprofissao integer;

select * from cliente

alter table cliente add constraint fk_cln_idprofissao foreign key (idprofissao) references profissao (idprofissao);

update cliente set idprofissao = 1 where idcliente in (1, 9, 10, 12, 15, 17)

update cliente set idprofissao = 2 where idcliente = 2;

update cliente set idprofissao = 3 where idcliente = 3;

update cliente set idprofissao = 4 where idcliente in (4, 5);

update cliente set idprofissao = 5 where idcliente in (6, 7, 8, 13);

select * from cliente;

select * from profissao;

delete from profissao where idprofissao = 10;

insert into profissao (idprofissao, nome) values (10, 'Teste')

select * from cliente 

alter table cliente drop nacionalidade;

alter table cliente add idnacionalidade integer;

alter table cliente add constraint fk_cln_idnacionalidade foreign key (idnacionalidade) references nacionalidade;

update cliente set idnacionalidade = 1 where idcliente in (1, 2, 3, 4, 6, 10, 11, 14);

update cliente set idnacionalidade = 2 where idcliente in (5, 7);

update cliente set idnacionalidade = 3 where idcliente = 8;

update cliente set idnacionalidade = 4 where idcliente in (9, 13)	

select * from cliente 

alter table cliente drop complemento;

alter table cliente add idcomplemento int;

alter table cliente add constraint fk_cln_idcomplemento foreign key (idcomplemento) references complemento (idcomplemento);

select * from cliente
	
update cliente set idcomplemento = 1 where idcliente in (1, 4, 9, 13);

update cliente set idcomplemento = 2 where idcliente in (2, 3, 7);

select * from cliente

alter table cliente drop bairro;

alter table cliente add idbairro integer;

alter table cliente add constraint fk_cln_idbairro foreign key (idbairro) references bairro (idbairro);

select * from cliente

update cliente set idbairro = 1 where idcliente in (1, 12, 13);

update cliente set idbairro = 2 where idcliente in (2, 3, 6, 8, 9);

update cliente set idbairro = 3 where idcliente in (4, 5);

update cliente set idbairro = 4 where idcliente = 7;

select * from cliente

create table uf (
	iduf integer not null,
	
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
	
	iduf integer not null,

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

select * from cliente

alter table cliente drop municipio;

alter table cliente drop uf;

alter table cliente add idmunicipio int;

alter table cliente add constraint fk_cln_idmunicipio foreign key (idmunicipio) references municipio (idmunicipio);

select * from cliente

update cliente set idmunicipio = 1 where idcliente in (1, 2, 10, 11);

update cliente set idmunicipio = 2 where idcliente in (3, 12);

update cliente set idmunicipio = 3 where idcliente = 4;

update cliente set idmunicipio = 4 where idcliente = 5;

update cliente set idmunicipio = 5 where idcliente in (6,13);

update cliente set idmunicipio = 6 where idcliente = 7;

update cliente set idmunicipio = 7 where idcliente = 8;

update cliente set idmunicipio = 8 where idcliente = 9;

left outer join

select * from cliente

--exercícios propostos:

--Começo do exercício 1
create table fornecedor (

idfornecedor integer not null,

nome varchar(50) not null,

constraint pk_fnc_idfornecedor primary key (idfornecedor),

constraint un_fnc_nome unique (nome)

);

insert into fornecedor (idfornecedor, nome) values (1, 'Cap. Computadores');

insert into fornecedor (idfornecedor, nome) values (2, 'AA. Computadores');

insert into fornecedor (idfornecedor, nome) values (3, 'BB. Máquinas');

select * from fornecedor
--Fim do exercício 1

--Exercício 2
create table vendedor (
idvendedor integer not null,
	
nome varchar(50) not null,

constraint pk_vdr_idvendedor primary key (idvendedor),
	
constraint un_vdr_nome unique (nome)

);

insert into vendedor (idvendedor, nome) values (1, 'André');

insert into vendedor (idvendedor, nome) values (2, 'Alisson');

insert into vendedor (idvendedor, nome) values (3, 'José');

insert into vendedor (idvendedor, nome) values (4, 'Ailton');

insert into vendedor (idvendedor, nome) values (5, 'Maria');

insert into vendedor (idvendedor, nome) values (6, 'Suelem');

insert into vendedor (idvendedor, nome) values (7, 'Aline');

insert into vendedor (idvendedor, nome) values (8, 'Silvana');

select * from vendedor;
--Fim do exercício 2

--Exercício 3
create table transportadora (

idtransportadora integer not null,
	
idmunicipio integer,
	
nome varchar(50) not null,
	
logradouro varchar(50),
	
numero varchar(10),

constraint pk_tpd_idtransportadora primary key (idtransportadora),
	
constraint fk_tpd_idmunicipio foreign key (idmunicipio) references municipio (idmunicipio),
	
constraint un_tpf_nome unique (nome)

);

insert into transportadora (idtransportadora, idmunicipio, nome, logradouro, numero) values (1, 1, 'BS. Transportes', 'Rua das Limas', 01);

insert into transportadora (idtransportadora, idmunicipio, nome, logradouro, numero) values (2, 5, 'União Transportes', null, null);

select * from transportadora;
--Fim do exercício 3

--Exercício 4
create table produto (

	idproduto integer not null,
	
	idfornecedor integer not null,
	
	nome varchar(50) not null,
	
	valor numeric(10,2) not null,

	constraint pk_pdt_idproduto primary key (idproduto),
	
	constraint fk_pdt_idfornecedor foreign key (idfornecedor) references fornecedor (idfornecedor)
	
);

insert into produto (idproduto, idfornecedor, nome, valor) values (1, 1, 'Microcomputador', 800);

insert into produto (idproduto, idfornecedor, nome, valor) values (2, 1, 'Monitor', 500);

insert into produto (idproduto, idfornecedor, nome, valor) values (3, 2, 'Placa mãe', 200);

insert into produto (idproduto, idfornecedor, nome, valor) values (4, 2, 'HD', 150);

insert into produto (idproduto, idfornecedor, nome, valor) values (5, 2, 'Placa de vídeo', 200);

insert into produto (idproduto, idfornecedor, nome, valor) values (6, 3, 'Memória RAM', 100);

insert into produto (idproduto, idfornecedor, nome, valor) values (7, 1, 'Gabinete', 35);

select * from produto
--Fim dos Exercícios

create table pedido (

idpedido integer not null,

idcliente integer not null,

idtransportadora integer,

idvendedor integer not null,

data_pedido date not null,

valor float not null,

constraint pk_pdd_idpedido primary key (idpedido),

constraint fd_pdd_idcliente foreign key (idcliente) references cliente (idcliente),

constraint fd_pdd_idtransportadora foreign key (idtransportadora) references transportadora (idtransportadora),

constraint fd_pdd_idvendedor foreign key (idvendedor) references vendedor (idvendedor)

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

select * from pedido

create table pedido_produto (

	idpedido int not null,
	
	idproduto int not null,
	
	quantidade int not null,
	
	valor_unitario numeric(10,2) not null,

	constraint pk_pdp_idpedidoproduto primary key (idpedido, idproduto),
	
	constraint fk_pdp_idpedido foreign key (idpedido) references pedido (idpedido),
	
	constraint fk_pdp_idproduto foreign key (idproduto) references produto (idproduto)
	
);

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

select * from produto

select * from pedido_produto
--Exercício

--Exercício 1: 
select * from vendedor order by nome;
--fim

--Exercicio 2:
select * from pedido where valor > 200 order by valor;
--fim

--Exercício 3:
select nome, valor, valor * 1.1 as "produto" from produto order by nome;
--fim

--Exercício 4:
select * from uf;
select * from municipio where iduf = 5
--fim

--Exercício 5:
select * from pedido;
select * from pedido where data_pedido between '2008-04-10' and '2008-04-25' order by valor;
--fim

--Exercício 6:
select * from pedido where valor between 1000 and 1500;
--fim

--Exercício 7:
select * from pedido where valor not between 100 and 500;
--fim

--Exercício 8:
select * from vendedor;
select * from pedido;
select * from pedido where idvendedor = 1 order by valor desc;
--fim

--Exercício 9:
select * from cliente;
select * from pedido where idcliente = 1 order by valor asc;
--fim

--Exercício 10:
select * from vendedor;
select * from pedido where idcliente = 15 and idvendedor = 1;
--fim

--Exercício 11:
select * from transportadora;
select * from pedido where pedido.idtransportadora = 2;
--fim

--Exercício 12:
select * from vendedor
select * from pedido where idvendedor - 5 or idvendedor = 7
--fim

--Exercício 13:
select * from municipio	
select * from cliente where idmunicipio - 1 or idmunicipio - 9
--fim

--Exercício 14:
SELECT * FROM cliente where idmunicipio <> 1 and idmunicipio <> 9
--fim

--Exercício 15:
select * from cliente where logradouro is null
--fim

--Exercício 16:
select * from cliente where logradouro like 'Av%'
--fim

--Exercício 17:
select * from vendedor where nome like 'S%'
--fim

--Exercício 18:
select * from vendedor where nome like '%a'
--fim

--Exercício 19:
select * from vendedor where nome like 'A%'
--fim

--Exercício 20:
select * from uf
select * from municipio where nome like '%P' and iduf = 1
--fim

--Exercício 21:
select * from idtransportadora where logradouro is not null;
--fim

--Exercício 22:
select * from pedido_produto where idpedido = 1
--fim

--Exercício 23:
select * from pedido_produto where idpedido = 6 or idpedido = 10;
--fim dos desafios.

--Funções agregadas
--Select idpedido, sum (valor_unitario) from pedido_produto group by idpedido

select avg(valor) from pedido

select count(idmunicipio) from municipio

select count (*) from municipio

select * from transportadora

select count(logradouro) from transportadora

select count(idtransportadora) from transportadora

select * from municipio

select count (idmunicipio) from municipio where iduf = 2

select min(valor) from pedido

select max(valor) from pedido

select  sum (valor) from pedido

select idcliente, sum (valor) from pedido group by idcliente

select idcliente, min (valor) from pedido group by idcliente

select idcliente, max (valor) from pedido group by idcliente

select idcliente, sum (valor) from pedido group by idcliente having sum (valor) > 500


--inicio Exercícios   -   funções agregadas

--Exercício 1:
select idvendedor, avg(valor) from pedido group by idvendedor having avg(valor) > 200;
--fim

--Exercício 2:
select min(valor) from pedido group by idcliente > 1500;
--fim

--Exercício 3:
select sum (valor) from 
--fim

--Exercício 4:
select * from municipio
--fim

--Exercício 5:
select * from uf
select count(idmunicipio) from municipio where iduf = 1 or iduf = 2
--fim

--Exercício 6:
select iduf, count(idmunicipio) from municipio group by iduf
--fim

--Exercício 7:
select count(idcliente) from cliente where logradouro is not null
--fim

--Exercício 8:
select idmunicipio, count(idcliente) from cliente group by idmunicipio
--fim

--Exercício 9:
select count(idfornecedor) from fornecedor
--fim

--Exercício 10:
select idfornecedor, count(idproduto) from produto group by idfornecedor
--fim

--Exercício 11:
select * from fornecedor
select avg(valor) from produto where idfornecedor = 1
--fim

--Exercício 12:
select sum(valor) from produto
--fim

--Exercício 13:
select nome, max(valor) from produto group by nome
--fim

--Exercício 14:
select nome, valor from produto order by valor asc limit 1
--fim

--Exercício 15:
select avg(valor) from produto
--fim

--Exercício 16:
select count(idtransportadora) from transportadora
--fim

--Exercício 17:
select avg(valor) from pedido
--fim

--Exercício 18:
select idcliente, sum(valor) from pedido group by idcliente
--fim

--Exercício 19:
select idvendedor, sum(valor) from pedido group by idvendedor
--fim

--Exercício 20:
select idtransportadora, sum(valor) from pedido group by idtransportadora
--fim

--Exercício 21:
select data_pedido, sum(valor) from pedido group by data_pedido
--fim

--Exercício 22:
select idcliente, idvendedor, idtransportadora, sum(valor) from pedido group by idcliente, idvendedor, idtransportadora
--fim

--Exercício 23:
select sum(valor) from pedido group by date_pedido between '2008-04-01' and '2009-12-10' having sum(valor) > 200;

--Exercício 24
select * from vendedor;
select * from pedido;
select avg(valor) from pedido group by id_vendedor = 1;

--Exercício 25
select * from cliente 15
select avg(valor) from pedido group by idcliente = 15;

--Exercício 26 
select count(id_transportadora = 1) from pedido;
select * from transportadora;

--Exercício 27
select count(id_pedido) from pedido group by id_vendedor;

--Exercício 28
select count(id_pedido) from pedido group by idcliente;

--Exercício 29
select count(id_pedido) from pedido group by date_pedido between '2008-04-15' and '2008-04-25';

--Exercício 30
select count(id_pedido) from pedido group by id_pedido having valor > 1000;

--Exercício 31
select count(id_produto) from pedido_produto group by id_produto having id_produto = 1;
select * from produto

--Exercício 32
select count(id_produto) from pedido_produto group by id_produto;

--Exercício 33
select sum(valor_unitario) from pedido_produto group by id_pedido;

--Exercício 34
select id_pedido, count(id_produto) from pedido_produto group by id_pedido order by id_pedido;
select * from pedido_produto

--Exercício 35
select id_produto, sum(valor_unitario) from pedido_produto group by id_produto

--Exercício 36
select avg(valor_unitario) from pedido_produto group by id_pedido having id_pedido = 6;

--Exercício 37
select max(valor_unitario) from pedido_produto 

--Exercício 38
select min(valor_unitario) from pedido_produto 

--Exercício 39
select id_pedido, sum(id_produto) from pedido_produto group by id_pedido

--Exercício 40
select sum(id_produto) from pedido_produt
--fim dos desafios

-- Relacionamentos com joins
select 
	cln.nome,
	prf.nome
from 
	cliente as cln
left outer join 
	profissao as prf on cln.idprofissao = prf.idprofissao
	----------------------
select 
	cln.nome as cliente,
	prf.nome as profissao
from 
	cliente as cln
inner join 
	profissao as prf on cln.idprofissao = prf.idprofissao
	-------------------------
select 
	cln.nome as cliente,
	prf.nome as profissao
from 
	cliente as cln
right outer join
	profissao as prf on cln.idprofissao = prf.idprofissao
	
select * from profissao

select * from cliente order by cliente

select * from nacionalidade

update cliente set idnacionalidade = 1 where idcliente in (1, 4, 7);

update cliente set idnacionalidade = 2 where idcliente in (3, 8);

update cliente set idnacionalidade = 3 where idcliente in (9, 5);

update cliente set idnacionalidade = 4 where idcliente in (2, 6);

update cliente set idmunicipio = 8 where idcliente = 9;

	------------------
	--Exercícios:

--Exercício 1:nome do cliente, a profissão, a nacionalidade, 
--o logradouro, o número, o complemento, o bairro, o município
--e a unidade de federação.

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
--fim

-- 2.nome do produto, valor e nome do fornecedor.
select 
	pdt.nome as produto,
	pdt.valor as valorProduto,
	pdt.idproduto as produtoid,
	pdd.idpedido as pedidoid,
	pdd.valor as valorPedido

from 
produto as pdt
join 
pedido_produto as pdpr on pdt.idproduto = pdpr.idproduto
join
pedido as pdd on pdd.idpedido = pdpr.idpedido
where pdd.idpedido = 6                     
select * from fornecedor
select produto.nome, produto.valor, fornecedor.nome from produto
join
fornecedor on fornecedor.idfornecedor = produto.idfornecedor
--fim

--Exercício 3:
select
	tpa.nome as transportadora,
	mnc.nome as municipio
from
pedido as pdd
left outer join
	transportadora as tpa on pdd.idtransportadora = tpa.idtransportadora
left outer join 
	municipio as mnc on tpa.idmunicipio = mnc.idmunicipio
group by tpa.nome, mnc.nome
--fim

--Exercício 4:
select
	pdd.data_pedido as data_pedido,
	pdd.valor,
	tpa.nome as transportadora,
	nmv.nome as vendedor
from
	pedido as pdd
left outer join 
	transportadora as tpa on pdd.idtransportadora = tpa.idtransportadora
left outer join
	vendedor as nmv on pdd.idvendedor = nmv.idvendedor
--fim

--Exercício 5:
select 
	pdp.idpedido,
	ndp.nome,
	pdp.quantidade
from 
pedido_produto as pdp
left outer join
	produto as ndp on pdp.idproduto = ndp.idproduto
--fim

--Exercício 6:
select 
	cln.nome,
	pdd.data_pedido
from pedido as pdd
left outer join
	cliente as cln on pdd.idcliente = cln.idcliente
order by cln.nome
--fim

--Exercício 7:
select 
	cln.nome,
	pdd.data_pedido
from pedido as pdd
left outer join
	cliente as cln on pdd.idcliente = cln.idcliente
order by cln.nome
--fim

--Exercício 8:
select 
	count(idcliente),
	mnc.nome as cidade
from cliente as cln
left outer join 
	municipio as mnc on cln.idmunicipio = mnc.idmunicipio
group by mnc.idmunicipio
--fim

--Exercício 9:
select 
	fnr.nome,
	count(idproduto)
from produto as pdt
join
	fornecedor as fnr on pdt.idfornecedor = fnr.idfornecedor
group by fnr.idfornecedor
--fim

--Exercício 10:
select 
	cln.nome,
	sum(valor) as soma
from pedido as pdd
left outer join
	cliente as cln on pdd.idcliente = cln.idcliente
group by cln.idcliente
--fim

--Exercício 11:
select 
	vdr.nome as vendedor,
	sum(valor) as soma
from pedido as pdd
left outer join
	vendedor as vdr on pdd.idvendedor = vdr.idvendedor
group by vdr.idvendedor
order by vdr.nome
--fim

--Exercício 12:
select 
	tpa.nome,
	sum(valor)
from 
pedido as pdd
left outer join 
	transportadora as tpa on pdd.idtransportadora  = tpa.idtransportadora
group by tpa.nome
--fim

--Exercício 13:
select 
	cln.nome,
	sum(valor)
from 
pedido as pdd
left outer join 
	cliente as cln on pdd.idcliente  = cln.idcliente
group by cln.nome
--fim

--Exercício 14:
select 
	pdt.nome,
	count(idpedido)
from pedido_produto as pdd
left outer join
	produto as pdt on pdd.idproduto = pdt.idproduto
group by 
	pdt.nome
--fim

--Exercício 15:
select 
	data_pedido,
	sum(valor)
from pedido
group by
	data_pedido
order by 
	data_pedido

--Exercício 16:
select 
	pdd.data_pedido,
	count(pdp.idproduto)
from 
	pedido_produto as pdp
left outer join
	pedido as pdd on pdd.idpedido = pdp.idpedido
group by
	pdd.data_pedido
--fim dos desafios.

-- Comandos adicionais
select * from pedido
select 
	data_pedido,
	extract(day from data_pedido),
	extract(month from data_pedido),
	extract(year from data_pedido)
from pedido

select
	nome,
	substring(nome from 1 for 5), substring(nome , 2)
from  cliente

select
	nome, 
	upper(nome)
from cliente
	
select nome, coalesce (cpf, 'Não foi informado') as cpf from cliente

select 
	case sigla
		when 'PR' then 'Paraná'
		when 'SC' then 'Santa Catarina'
	else
		'Outros'
	end as uf
from uf
--Exercícios comandos adicionais

--Exercício 1:
select nome, data_nascimento as data_nascimento from cliente
--fim

--Exercício 2:	
select nome,
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
	when 10 then 'Outubro'
	when 11 then 'Novembro'
	when 12 then 'Dezembro'
	else 'Não Informado'
	end as "Mês De Nascimento"
from cliente
--fim

--Exercício 3:
select nome,
	case(extract(year from data_nascimento))
	when 01 then '2010'
	when 02 then '2009'
	when 03 then '2008'
	when 04 then '2007'
	when 05 then '2006'
	when 06 then '2005'
	when 07 then '2004'
	else 'Não Informado'
	end as "Ano de nascimento"
from cliente
--fim

--Exercício 4:
select	
	nome,
	substring(nome from 5 for 10), substring(nome , 2)
from  cliente
--fim

--Exercício 5:
select
	idmunicipio, 
	upper(nome)
from cliente
--fim

--Exercício 6:
select nome, coalesce (genero, 'Não foi informado') as genero from cliente
--fim

--Exercício 7:
select 
	nome,
	valor,
	case 
		when valor > 500 then 'mais de 500'
	else 'menos de 500'
	end as valor
from
	produto
--fim dos desafios

-- Subconsultas
select 
	date_pedido,
	valor
from
	pedido
where
	valor > (select avg(valor) from pedido)
	
select 
	pdd.date_pedido,
	pdd.valor,
	(select sum(quantidade) from pedido_produto as pdp where pdp.id_pedido = pdd.id_pedido)
from 
	pedido as pdd
	
select * from pedido

update pedido set valor = valor + ((valor * 5) / 100)
where valor > (select avg(valor) from pedido)