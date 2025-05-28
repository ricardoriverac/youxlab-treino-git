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

update cliente set idmunicipio = 9 where idcliente in (14, 15);

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
