create table cliente(
	idcliente integer not null,
	nome varchar(50) not null, --campo obrigatório
	cpf char(11),
	rg varchar(15),
	data_nascimento date,
	genero char(1),
	profissao varchar(30),
	nacionalidade varchar (30),
	logradouro varchar(30),
	numero varchar(10),
	complemento varchar(30),
	bairro varchar(30),
	municipio varchar(30),
	uf varchar(30),
	observacoes text,

	-- primary key

	constraint pk_cln_idcliente primary key(idcliente)
)
insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(1, 'Igor', '23132223400', '132123', '2001-01-30', 'M', 'Programador','BR', 'Casadele', 234, 'perto do circuito', 'Nova Vida', 'Lavras', 'MG');

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(2, 'Guilherme', '34556463451', '167995', '2007-08-20', 'M', 'Músico','BR', 'Oliveira Lima', 78, 'Campo Grande', 'Vida Nova', 'Salvador', 'BA');

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(3, 'Ana', '35675674522', '17868', '2008-09-21', 'F', 'Locutora','BR', 'Oliveira Palmeira', 90, 'Goiás Campo', 'Vida Top', 'Lavras', 'MG');

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(4, 'Lucas', '56785784533', '123213', '2010-04-19', 'M', 'Engenheiro','BR', 'Oliveira Agostinho', 123, 'Vida Bela', 'Goitacases', 'Perdões', 'MG');

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(5, 'Pamela', '36757787744', '134234', '2002-12-26', 'F', 'Analista de Software','BR', 'Rua Duque Rocha', 96, 'Campo Grande', 'Lavoura Nova', 'Lavoura', 'MG');

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(6, 'Mariana', '12345678155', '456123', '1999-05-15', 'F', 'Designer Gráfico', 'BR', 'Rua das Flores', 101, 'Apt 202', 'Jardim Alegre', 'Belo Horizonte', 'MG');

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(7, 'Rafael', '98763210066', '789456', '1995-11-23', 'M', 'Administrador', 'BR', 'Av. Central', 55, 'Sala 10', 'Centro', 'Curitiba', 'PR');

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(8, 'Beatriz', '45678914577', '321789', '2000-07-09', 'F', 'Psicóloga', 'BR', 'Rua Esperança', 78, 'Casa Azul', 'Morada do Sol', 'Fortaleza', 'CE');

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(9, 'Thiago', '65432176588', '654321', '1993-03-03', 'M', 'Professor', 'BR', 'Rua Nova Era', 30, 'Fundos', 'Boa Vista', 'Campinas', 'SP');

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(10, 'Camila', '32165873299', '987654', '1998-10-12', 'F', 'Dentista', 'BR', 'Travessa Luz', 19, 'Bloco C', 'Jardim das Laranjeiras', 'Recife', 'PE');

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(11, 'Fernanda', '78945612300', '112233', '1990-02-14', 'F', 'Médica', 'BR', 'Rua Saúde', 50, 'Casa 2', 'Bela Vista', 'São Paulo', 'SP');

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(12, 'Diego', '99887766554', '445566', '1985-06-10', 'M', 'Engenheiro Civil', 'BR', 'Av. Brasil', 200, 'Cobertura', 'Centro', 'Rio de Janeiro', 'RJ');

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(13, 'Juliana', '11223344556', '778899', '1992-03-08', 'F', 'Advogada', 'BR', 'Rua da Paz', 87, 'Bloco B', 'Serra Verde', 'Contagem', 'MG');

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(14, 'Eduardo', '33445566778', '889900', '1988-12-30', 'M', 'Arquiteto', 'BR', 'Rua das Palmeiras', 12, 'Ap 101', 'Jardim das Rosas', 'Florianópolis', 'SC');

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(15, 'Patrícia', '55667788990', '998877', '1996-09-17', 'F', 'Jornalista', 'BR', 'Rua da Liberdade', 65, 'Casa Fundos', 'Vila Nova', 'Porto Alegre', 'RS');

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(16, 'ana', '55667788990', NULL, '1996-09-17', 'F', 'Jornalista', 'BR', 'Rua da Liberdade', 65, 'Casa Fundos', 'Vila Nova', 'Porto Alegre', 'RS');

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(17, 'Jessica', '55667788990', NULL, '1996-09-17', 'F', 'Confeiteira', 'BR', 'Rua Jorge', 67, 'Casa Fundos', 'Vila Nova', 'Porto Alegre', 'RS');

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(18, 'Pedro', NULL, NULL, '1995-08-16', 'F', 'Padeiro', 'BR', 'Rua Jorge', 67, NULL, NULL, NULL, NULL);

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(19, 'Miguel Lucas', NULL, NULL, '1998-07-21', 'M', 'Jardineiro', 'AR', 'Rua Madalena', NULL, NULL, NULL, NULL, NULL);

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(20, 'Maicon', '12312323', '3445345', '1955-01-21', 'F', 'Empresário', 'Brasileira', 'Rua Central', '343', 'Apartamento', 'Centro', 'Florianópolis);

select * from cliente;
select nome, data_nascimento from cliente;
select nome, data_nascimento as "Data De Nascimento" from cliente;
select 'CPF: ' || cpf || ' RG: ' || rg as "CPF e RG" from cliente;
select rg as "Identidade", bairro as "Identidade e Bairro" from cliente;
select * from cliente limit 3;

select nome, data_nascimento from cliente where data_nascimento > '2000-01-01';
select * from cliente where nome like 'C%';
select nome from cliente where nome like '%a%';
select nome, data_nascimento from cliente where data_nascimento between '1999-01-01' and '2007-01-01';
select nome, rg from cliente where rg is null;
select nome from cliente order by nome asc;
select nome from cliente order by nome desc;

--exercicios

select nome, genero, profissao from cliente order by nome desc;
select * from cliente where nome like '%r%';
select * from cliente where nome like 'C';
select * from cliente where nome like '%a';

select * from cliente where bairro like 'Centro';

select * from cliente where complemento like 'A%';
select * from cliente where genero like 'F';
select * from cliente where rg is null;
select * from cliente where cpf is null;
select nome, profissao as "Nome da profissão" from cliente order by profissao asc;
select * from cliente where nacionalidade like 'BR';
select * from cliente where numero is not null;]
select * from cliente where numero is null;
select * from cliente where uf like 'SC';
select * from cliente where data_nascimento between '2000-01-01' and '2002-01-01';
select 'Nome: ' || nome || ' Logadouro: ' || logradouro || ' Número: ' || numero || ' Complemento: ' || complemento || ' Bairro: ' || bairro || ' Municipio: ' || municipio || 'UF: ' || uf as "Todos os clientes" from cliente;

update cliente set nome = 'Teste' where idcliente = 1;
select * from cliente;
update cliente set nome = 'Miguel' where idcliente = 1;
update cliente set nome = 'Edudarda', genero = 'F', numero = '43' where idcliente = 14;

insert into cliente (idcliente, nome) values (20, 'João');
select nome from cliente where idcliente = 20;
delete from cliente where idcliente = 20;

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(22, 'Maicon', NULL, NULL, NULL, 'M', 'Médica', 'Brasileira', 'Rua dos Goitacases', '87', 'Ap', 'Flor nova', 'Rio preto','SP' );

insert into cliente(idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(23, 'Sandra', NULL, NULL, NULL, 'M', 'Empresário', 'Italiana', NULL, '65', 'Bloco A', NULL, NULL, NULL);

update cliente set genero = 'M', nacionalidade = 'Brasileira', uf = 'BA' where idcliente = 20;
update cliente set genero = 'M', data_nascimento = '1978-01-04' where idcliente = 21;
update cliente set genero = 'F', profissao = 'Professora', numero = '123' where idcliente = 23;

delete from cliente where nome = 'Maicon';
delete from cliente where idcliente = 23;

select * from cliente;

create table profissao(
	idprofissao integer not null,
	nome varchar not null,


	constraint pk_prf_idprofissao primary key (idprofissao),
	constraint un_prf_nome unique (nome)
);

create table profissao(
	idprofissao integer not null,
	nome varchar not null,


	constraint pk_prf_idprofissao primary key (idprofissao),
	constraint un_prf_nome unique (nome)
);

create table nacionalidade(
	idnacionalidade integer not null,
	nome varchar(30) not null, --variable character 

	constraint pk_ncn_idnacionalidade primary key (idnacionalidade),
	constraint un_unc_nome unique (nome)
);
select nacionalidade from cliente;

-- mudando a nacionalidae dos clientes
update cliente set nacionalidade = 'Italiana' where idcliente = 2;
update cliente set nacionalidade = 'Norte-Americana' where idcliente = 3;
update cliente set nacionalidade = 'Alemã' where idcliente = 4;


insert into nacionalidade (idnacionalidade, nome) values(1, 'Brasileira');
insert into nacionalidade (idnacionalidade, nome) values(2, 'Italiana');
insert into nacionalidade (idnacionalidade, nome) values(3, 'Norte-Americana');
insert into nacionalidade (idnacionalidade, nome) values(4, 'Alemã');

create table complemento(
	idcomplemento integer not null,
	nome varchar(30) not null,

	constraint pk_cpl_idcomplemento primary key (idcomplemento),
	constraint un_cpl_nome unique (nome)
);

select * from cliente;
select * from nacionalidade;

insert into complemento (idcomplemento, nome) values (1, 'Perto do circuito');
insert into complemento (idcomplemento, nome) values (2, 'Campo Grande');
insert into complemento (idcomplemento, nome) values (3, 'Goias Campo');
insert into complemento (idcomplemento, nome) values (4, 'Vida Bela');

update 
create table bairro (
	idbairro integer not null,
	nome varchar(30) not null,

	constraint pk_br_bairro primary key (idbairro),
	constraint un_bairro_nome unique (nome)
);

insert into bairro (idbairro, nome) values (1, 'Nova Vida');
insert into bairro (idbairro, nome) values (2, 'Vida Nova');
insert into bairro (idbairro, nome) values (3, 'Vida Top');
insert into bairro (idbairro, nome) values (4, 'Goitacases');

insert into profissao (idprofissao, nome) values (1, 'Programador');
insert into profissao (idprofissao, nome) values (2, 'Músico');
insert into profissao (idprofissao, nome) values (3, 'Locutora');
insert into profissao (idprofissao, nome) values (4, 'Engenheiro');
insert into profissao (idprofissao, nome) values (5, 'Jornalista');

alter table cliente rename column profissao to idprofissao;

-- estudante -> 1, 9, 10, 12, 15, 17
-- engenheiro -> 2
-- pedreiro -> 3
-- jornalista -> 4, 5
-- professor -> 6, 7, 8, 13
-- null 11, 14


select * from cliente;
select * from profissao;

select * from cliente where idprofissao is null;
update cliente set idprofissao = 'Pedreiro' where idcliente = 3;
update cliente set idprofissao = 'Jornalista' where idcliente = 4;
update cliente set idprofissao = 'Jornalista' where idcliente = 5;

update cliente set idprofissao = 'Professor' where idcliente = 6;
update cliente set idprofissao = 'Professor' where idcliente = 7;
update cliente set idprofissao = 'Professor' where idcliente = 8;
update cliente set idprofissao = 'Professor' where idcliente = 13;

update cliente set idprofissao = NULL where idcliente = 11;
update cliente set idprofissao = NULL where idcliente = 14;

-- exclui a a coluna idcliente
alter table cliente drop idprofissao;

-- cria uma nova coluna que recebe dados inteiros
alter table cliente add idprofissao integer;

-- adicionar na tabela usando a chave estrangeira da idprofissao que relaciona com profissao utilizando a chave idprofissao
alter table cliente add constraint fk_cln_idprofissao foreign key (idprofissao) references profissao (idprofissao);
update cliente set idprofissao = 1 where idcliente in (1, 9, 10, 12, 15, 17);
update cliente set idprofissao = 2 where idcliente in (2);
update cliente set idprofissao = 3 where idcliente in (3);
update cliente set idprofissao = 4 where idcliente in (4, 5);
update cliente set idprofissao = 5 where idcliente in (6, 7, 8, 13);

select * from cliente;
select * from profissao;
-- BR -> 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21
-- norte-americana -> 3
-- Alemã -> 4
-- Italiana -> 2
alter table cliente add idnacionalidade integer;
alter table cliente drop nacionalidae;
alter table cliente add constraint fk_cln_idnacionalidade foreign key (idnacionalidade) references nacionalidade (idnacionalidade);

select * from nacionalidade;
update cliente set idnacionalidade = 1 where idcliente in (1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21);
update cliente set idnacionalidade = 2 where idcliente in (2);
update cliente set idnacionalidade = 3 where idcliente in (3);
update cliente set idnacionalidade = 4 where idcliente in (4);
select * from cliente;

-- alter table de complemento
select * from cliente where complemento like 'Campo Grande';
-- Casa dos fundos = (16, 15, 17)
-- Apartamento = 21
-- Perto do circuito = 1
-- fundos = 9
-- bloco c = 10
-- cobertura = 12
-- campo grande = 5, 2
-- apt 202 = 6
-- sala 10 = 7
-- casa azul = 8
-- bloco b = 13
-- casa 2 = 11
-- ap 101 = 14
-- goias campo = 3
-- vida bela = 4

alter table cliente drop complemento;
alter table cliente add idcomplemento integer;
alter table cliente add constraint fk_cln_idcomplemento foreign key (idcomplemento) references complemento(idcomplemento);
select * from complemento;
update cliente set idcomplemento = 1 where idcliente in (1);
update cliente set idcomplemento = 2 where idcliente in (2);
update cliente set idcomplemento = 3 where idcliente in (3);
update cliente set idcomplemento = 4 where idcliente in (4);
select * from cliente;

-- fazendo alter table de bairro
-- nova vida = 1
-- vida nova = 2
-- vida top = 3
-- goitacases = 4

alter table cliente drop bairro;
alter table cliente add idbairro integer;
alter table cliente add constraint foreign key (idbairro)

alter table cliente add constraint fk_cln_idbairro foreign key (idbairro) references bairro (idbairro);
select * from cliente;

update cliente set idbairro = 1 where idcliente in (1);
update cliente set idbairro = 2 where idcliente in (2);
update cliente set idbairro = 3 where idcliente in (3);
update cliente set idbairro = 4 where idcliente in (4);

select * from bairro; 
create table uf (
	iduf integer not null,
	nome varchar(30) not null,
	sigla  varchar (2) not null, 

	constraint fk_ufd_ifunidade_federacao primary key (iduf),
	constraint un_ufd_nome unique (nome),
	constraint un_ufd_sigla unique (sigla)
);
insert into uf (iduf, nome, sigla) values (1, 'Minas Gerais', 'MG');
insert into uf (iduf, nome, sigla) values (2, 'Bahia', 'BA');
insert into uf (iduf, nome, sigla) values (3, 'Rio grande', 'RS');
insert into uf (iduf, nome, sigla) values (4, 'Rio De Janeiro', 'RJ');
insert into uf (iduf, nome, sigla) values (5, 'São Paulo', 'SP');

select * from uf;

update uf set nome = 'Bahia' where iduf = 2;
create table municipio(
	idmunicipio integer not null,
	nome varchar(30) not null,
	iduf integer not null,

	constraint pk_mnc_idmunicipio primary key (idmunicipio),
	constraint un_mnc_nome unique (nome),
	constraint un_mnc_idfuf foreign key (iduf) references uf (iduf)
);
select * from municipio;
insert into municipio (idmunicipio, nome, iduf) values (1, 'Lavras', 1);
insert into municipio (idmunicipio, nome, iduf) values (2, 'Salvador', 2);
insert into municipio (idmunicipio, nome, iduf) values (3, 'Porto Alegre', 3);
insert into municipio (idmunicipio, nome, iduf) values (4, 'Rio de Janeiro', 4);
insert into municipio (idmunicipio, nome, iduf) values (5, 'São Paulo', 5);

-- lavras - 1
-- salvador - 2
-- lavras 
-- rio 12 
-- sp - 11
-- porto alegr - 16 ana 

select * from cliente;
select idcliente from cliente where municipio like 'Ri%';
alter table cliente drop municipio;
alter table cliente drop uf;

alter table cliente add idmunicipio integer;
alter table cliente add constraint fk_cliente_idmunicipio foreign key (idmunicipio) references municipio (idmunicipio);

update cliente set idmunicipio = 1 where idcliente in (1, 3);
update cliente set idmunicipio = 2 where idcliente in (2);
update cliente set idmunicipio = 3 where idcliente in (16);
update cliente set idmunicipio = 4 where idcliente in (12);
update cliente set idmunicipio = 5 where idcliente in (11);
select * from cliente;

create table fornecedor(
	idfornecedor integer not null,
	nome varchar not null,

	constraint pk_fndr_idfornecedor primary key (idfornecedor),
	constraint un_nome unique (nome)
	
);

insert into forncedores (idfornecedor, nome)

create table vendedor(
	idvendedor integer not null,
	nome varchar (30) not null,

	constraint pk_vndr_vendedor primary key (idvendedor),
	constraint un_vndr_nome unique (nome)
	
);
insert into vendedor (idvendedor, nome) values (1, 'Matheus Silva');
insert into vendedor (idvendedor, nome) values (2, 'Thiago Gomes');
insert into vendedor (idvendedor, nome) values (3, 'Erick Gomez');
insert into vendedor (idvendedor, nome) values (4, 'Santiago Menez');
insert into vendedor (idvendedor, nome) values (5, 'João Prado');
insert into vendedor (idvendedor, nome) values (6, 'Gustavo Henrique');
insert into vendedor (idvendedor, nome) values (7, 'Hiago Souza');

create table transportadora(
	idtransportadora integer not null,
	idmunicipio integer not null,
	nome varchar (50),
	logradouro varchar (50),
	numero varchar (10),
	
	constraint pk_tptd_transportadora primary key (idtransportadora),
	constraint fk_mfcp_idmunicipio foreign key (idtransportadora) references municipio(idmunicipio),
	constraint un_tptd_nome unique (nome)
);

select * from municipio;
select * from bairro;

insert into transportadora(idtransportadora, idmunicipio, nome, logradouro, numero) values (1, 2, 'AC. Materiais','Rua dos ipês', '45' );

insert into transportadora(idtransportadora, idmunicipio, nome, logradouro, numero) values (2, 1, 'JP. Construção','Jardim Glória', '345' );

insert into transportadora(idtransportadora, idmunicipio, nome, logradouro, numero) values (3, 5, 'BK Transporte','Rua dos palmares', '23' );

insert into transportadora(idtransportadora, idmunicipio, nome, logradouro, numero) values (4, 4, 'RM. Transportadora','Ouro Preto', '67' );

insert into transportadora(idtransportadora, idmunicipio, nome, logradouro, numero) values (5, 3, 'Pedro Caminhões','Rua das lagoas', '12' );
select * from transportadora;

select * from transportadora;

create table Produto(
	idproduto integer not null,
	idfornecedor integer not null,
	nome varchar (30) not null,
	valor decimal(10, 2) not null,

	constraint pk_pdt_idproduto primary key (idproduto),
	constraint fk_frnc_idfornecedor foreign key (idfornecedor) references fornecedor (idfornecedor)
);
select * from fornecedor;

insert into Produto(idproduto, idfornecedor, nome, valor) values (1, 2, 'Ford Focus - 2008', 28.000);
insert into Produto(idproduto, idfornecedor, nome, valor) values (2, 3 ,'Corolla - 2010', 30.204);
insert into Produto(idproduto, idfornecedor, nome, valor) values (3, 1, 'Kicks - 2025', 45.000);
insert into Produto(idproduto, idfornecedor, nome, valor) values (4, 1, 'SUV compacto - 2017', 100.000);
insert into Produto(idproduto, idfornecedor, nome, valor) values (5, 2, 'Mustang GT (manual) - 2020', 350.000);
insert into Produto(idproduto, idfornecedor, nome, valor) values (6, 3, 'Carmy - 2013', 48.000);
insert into Produto(idproduto, idfornecedor, nome, valor) values (7, 3, 'Yaris Cross - 2008', 21.000);
select * from produto;

create table pedidos(
	idpedido integer not null,
	idcliente integer not null,
	idtransportadora integer not null,
	idvendedor integer not null,
	data_pedido date not null,
	valor decimal (10, 2) not null,

	constraint pk_pdd_idpedido primary key (idpedido),
	constraint fk_pdd_idcliente foreign key (idcliente) references cliente (idcliente),
	constraint fk_tpd_idtransportadora foreign key (idtransportadora) references transportadora (idtransportadora),
	constraint fk_vnd_idvendedor foreign key (idvendedor) references vendedor (idvendedor)
);
select * from cliente;
select * from transportadora;
select * from vendedor;

insert into pedidos(idpedido,data_pedido, valor, idcliente, idtransportadora, idvendedor)
values(1, '2008-04-01', 1300, 4, 2, 3);

insert into pedidos(idpedido,data_pedido, valor, idcliente, idtransportadora, idvendedor)
values(2, '2008-04-01', 500, 4, 2, 3);

insert into pedidos(idpedido,data_pedido, valor, idcliente, idtransportadora, idvendedor)
values(3, '2008-07-12', 700, 1, 3, 2);

insert into pedidos(idpedido,data_pedido, valor, idcliente, idtransportadora, idvendedor)
values(4, '2008-10-23', 450, 5, 1, 1);

insert into pedidos(idpedido,data_pedido, valor, idcliente, idtransportadora, idvendedor)
values(5, '2008-05-05', 1000, 3, 3, 3);

insert into pedidos(idpedido,data_pedido, valor, idcliente, idtransportadora, idvendedor)
values(6, '2008-05-05', 100, 3, 3, 3);

insert into pedidos(idpedido,data_pedido, valor, idcliente, idtransportadora, idvendedor)
values(7, '2008-09-03', 20.000, 5, 1, 1);

create table pedido_produto(
	idpedido integer not null,
	idproduto integer not null,
	quantidade integer not null,
	valor_unitario decimal(10,2) not null,

	constraint pk_pdp_idpedidoproduto primary key (idpedido, idproduto),
	constraint fk_pdp_idpedido foreign key (idpedido) references pedidos(idpedido),
	constraint fk_pdp_idproduto foreign key (idproduto) references produto(idproduto)
	
);

select * from produto;
select * from pedidos;
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (1, 1, 1, 28.000);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (2, 1, 1, 28.000);
update pedidos set valor = 350.000 where idpedido = 7;

insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (3, 4, 1, 21.000);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (4, 5, 1, 45.000);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (5, 3, 1, 30.000);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (6, 3, 1, 21.000);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (7, 5, 1, 350.000);

select * from pedido_produto;

-- exercicio aula(29)
-- ex 01:
select nome from vendedor order by nome;

-- ex 02
select nome, valor from produto where valor > 100.000 order by valor asc;

-- ex 03
select nome, valor, valor + (valor * 10) / 100 from produto;

-- ex 04;
select * from uf;
select * from municipio;
select nome from municipio where idmunicipio = 3 and iduf = 3; 

-- ex 05;
select * from pedidos;
select data_pedido, valor from pedidos where data_pedido between '2008-04-01' and '2008-05-05' order by valor;

--ex 06
select * from pedidos where valor between '10.000' and '50.000';

-- ex 07
select * from pedidos where valor not between '10.000' and '50.000';

-- ex 08
select * from vendedor;
select * from pedidos where idvendedor = 3 order by valor desc;

-- ex 09
select * from pedidos;
select * from pedidos where idcliente = 3 order by valor;

-- ex 10
select * from pedidos;
select * from pedidos where idcliente = 4 and idvendedor = 3;

-- ex 11
select * from pedidos where idtransportadora = 3;

-- ex 12
select * from pedidos where idvendedor = 2 or idvendedor = 1;

-- ex 13
select * from cliente where idmunicipio = 1 or idmunicipio = 4;

-- ex 14
select * from cliente where idmunicipio <> 1 and idmunicipio <> 4;
-- ex 15
select * from cliente where logradouro is null;
select * from cliente;

-- ex 16
select * from cliente where logradouro like 'Av%';

-- ex 17
select * from vendedor where nome like 'S%';

-- ex 18
select * from vendedor where nome like '%a';

-- ex 19
select * from vendedor where nome not like 'A%'

-- ex 20
select * from municipio where nome like 'P%' and iduf = 3;

-- ex 21
select * from transportadora;
select * from transportadora where logradouro is not null;

-- ex 22
select * from pedido_produto where idpedido = 1;

-- ex 23
select * from pedido_produto where idpedido = 3 or idpedido = 5;


------ funções agragarias
-- comando avg tira a media dos valores da coluna

select avg(valor) from pedidos;

select count(idmunicipio) from municipio;

-- conta tudo independende se o campo estiver null
select count(*) from municipio;

select count(idtransportadora) from transportadora;

select * from municipio;
-- filtrando contando o numero de idmunicipio onde os id uf é igual a 2
select count(idmunicipio) from municipio where iduf = 2;

select max(valor ) from pedidos;
select min(valor ) from pedidos;

select sum(valor ) from pedidos;

-- agrupando os id dos clientes e somando os pedidos deles para aprecer uma unica vez 
select idcliente, sum(valor) from pedidos group by idcliente;

-- impondo condições para que filtrar o valor da soma apenas para os maiores que 60.000
select idcliente, sum(valor) from pedidos group by idcliente having sum(valor) > 60.000;

------ exercicios das funções----------

-- ex 01
select * from pedidos;
select idvendedor, sum(valor) from pedidos group by idvendedor having sum(valor) > 60.000;

-- ex 02
select idvendedor, valor from pedidos where valor > 50.000; 

-- ex 03
select idvendedor, sum(valor) from pedidos group by idvendedor having sum(valor) > 50.000;

-- ex 04
select count(idmunicipio) from municipio;

-- ex 05
select count(idmunicipio) from municipio where iduf = 1 or iduf = 3;

-- ex 06

select iduf, count(idmunicipio) from municipio group by iduf;

-- ex 07

select * from cliente where logradouro is not null;

-- ex 08

select idmunicipio, count(idcliente) from cliente group by idmunicipio;
select * from cliente;
select * from pedido;
select * from municipio;

-- ex 09

select idfornecedor, count(idfornecedor) from fornecedor;

-- ex 10
select * from produto;
select idfornecedor, count(idproduto) from produto group by idfornecedor;

-- ex 11

select avg(valor) from produto where idfornecedor = 2;

-- ex 12
select sum(valor) from produto;

-- ex 13
select max(valor) from produto;
select nome, valor from produto order by valor desc limit 1

-- ex 14

select nome, valor from produto order by valor asc limit 1

-- ex 15

select avg(valor) from produto;

-- ex 16
select count(idtransportadora) from transportadora;

-- ex 17
select sum(valor) from pedidos;

-- ex 18
select idcliente, sum(valor) from pedidos group by idcliente;

-- ex 19

select idvendedor, sum(valor) from pedidos group by idvendedor;

-- 20
select idtransportadora, sum(valor) from pedidos group by idtransportadora;

-- 21
select data_pedido, sum(valor) from pedidos group by data_pedido;

-- 22
select idcliente, idvendedor, idtransportadora, sum(valor) from pedidos group by idcliente, idvendedor, idtransportadora;

-- 23 
select sum(valor) from pedidos where data_pedido between '2008-04-01' and '2008-05-05' and valor > 50.000;

--24
select sum(valor) from pedidos where idvendedor = 2;

-- 25
select sum(valor) from pedidos where idcliente = 3;

-- 26
select * from pedidos;
select * from transportadora;
select count(idtransportadora) from pedidos where idtransportadora = 2;

-- 27
select idvendedor, count(idvendedor) from pedidos group by idvendedor

-- 28
select idcliente, count(idcliente) from pedidos group by idcliente;	

-- 29 
select count(idpedido) from pedidos where data_pedido between '2008-04-15' and '2008-05-05';

-- 30 
select count(idpedido) from pedidos where valor > 50.000;

--31
select * from pedidos;
select * from produto;
select count (idproduto) from produto where idproduto = 2;

--32
select idproduto, count(idpedido) from pedido_produto group by idproduto;

--33
select * from pedido_produto;
select idpedido, sum(valor) from pedidos group by idpedido;
select idpedido, sum(valor_unitario) from pedidos group by idpedido

--34 quantidade de produtos agrupados por pedido
select idpedido, count(quantidade) from pedido_produto group by idpedido;

-- 35 
select sum(valor_unitario) from pedido_produto;

--36 
select avg(valor_unitario) from pedido_produto where idpedido = 6;

--37
select max(valor_unitario) from pedido_produto;

--38
select min(valor_unitario) from pedido_produto;

--39
select * from pedidos;
select idpedido, sum(idproduto) from pedido_produto group by idpedido;

--40
select sum(valor_unitario) from pedido_produto;

-------- relacionamento com joins --------------

select * from cliente;
select * from profissao;
update cliente set idprofissao = 1 where idcliente = 2;
update cliente set idprofissao = 3 where idcliente = 1;
update cliente set idprofissao = 2 where idcliente = 4;
update cliente set idprofissao = 4 where idcliente = 3;
update cliente set idprofissao = 2 where idcliente = 5;
update cliente set idprofissao = 1 where idcliente = 6;
update cliente set idprofissao = 4 where idcliente = 7;
update cliente set idprofissao = 1 where idcliente = 8;
update cliente set idprofissao = 3 where idcliente = 9;
update cliente set idprofissao = 3 where idcliente = 10;
update cliente set idprofissao = 2 where idcliente = 11;
update cliente set idprofissao = 4 where idcliente = 12;
update cliente set idprofissao = 1 where idcliente = 13;
update cliente set idprofissao = 1 where idcliente = 14;
update cliente set idprofissao = 3 where idcliente = 15;
update cliente set idprofissao = 2 where idcliente = 16;
update cliente set idprofissao = 1 where idcliente = 17;
update cliente set idprofissao = 3 where idcliente = 18;
update cliente set idprofissao = 4 where idcliente = 19;
update cliente set idprofissao = 2 where idcliente = 20;



-- left outer join retorna tudo até o null (melhor opcção)
-- inner join apenas os cliente que informaram os dados

-- seleciona nome dos clientes e as profissões da tabela de profissão 
select cliente.nome as cliente, profissao.nome as profissao from cliente inner join profissao on cliente.idprofissao = profissao.idprofissao;

---- Exercicios --------

select
	cliente.nome as cliente,
	profissao.nome as profissao,
	nacionalidade.nome as nacionalidade,
	cliente.logradouro,
	cliente.numero,
	complemento.nome as complemento,
	bairro.nome as bairro,
	municipio.nome as municipio
	
from
	cliente 
left outer join 
	profissao on cliente.idprofissao = profissao.idprofissao
left outer join 
	nacionalidade on cliente.idnacionalidade = nacionalidade.idnacionalidade
left outer join 
	complemento on cliente.idcomplemento = complemento.idcomplemento
left outer join 
	bairro on cliente.idbairro = bairro.idbairro
left outer join 
	municipio on cliente.idmunicipio = municipio.idmunicipio

-- ex 02 nome do produto, valor e o nome do fornecedor
select
	produto.nome as produto,
	produto.valor
	fornecedor.nome as fornecedor

from
	produto 
left outer join 
	fornecedor on produto.idfornecedor = fornecedor.idfornecedor

-- ex 03
select
	transportadora.nome as transportadora,
	municipio.nome as municipio

from
	transportadora
	
left outer join 
	municipio on transportadora.idmunicipio = municipio.idmunicipio
	
-- ex 04
select
	pedidos.data_pedido as data_pedido,
	pedidos.valor as valor_do_pedido,
	cliente.nome as cliente,
	transportadora.nome as transportadora,
	vendedor.nome as vendedor
	

from
	pedidos
left outer join 
	cliente on pedidos.idcliente = cliente.idcliente
left outer join 
	vendedor on pedidos.idvendedor = vendedor.idvendedor
left outer join 
	transportadora on pedidos.idtransportadora = transportadora.idtransportadora

-- ex 05
select
	produto.nome as produto,
	pedido_produto.quantidade,
	pedido_produto.valor_unitario
	

from
	pedido_produto
left outer join 
	produto on pedido_produto.idproduto = produto.idproduto

-- ex 06
select
	cliente.nome as cliente,
	pedidos.data_pedido
	
	

from
	cliente
inner join 
	pedidos on cliente.idcliente = pedidos.idcliente
order by cliente.nome

-- ex 07
select
	cliente.nome as cliente,
	pedidos.data_pedido
	
	

from
	cliente
left outer join 
	pedidos on cliente.idcliente = pedidos.idcliente
order by cliente.nome

-- ex 08 quantidade 
select
	cliente.idmunicipio,
	count(cliente.idcliente)
	
	
from
	cliente
left outer join 
	municipio on cliente.idmunicipio = municipio.idmunicipio

group by cliente.idmunicipio