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