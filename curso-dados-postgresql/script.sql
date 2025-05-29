	create table cliente (
	idcliente integer not null, -- número inteiro ( não pode ser vazio )
	nome varchar(50) not null, -- armazena 50 valor no disco, porem usa apenas o necessario com limite de até 50
	cpf char(11), -- armazena 11 valor fixo no disco, fica reservado os 11 valores, mesmo não estando usando
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
	observacoes text, -- armazena quantos valores necessarios no disco

	-- primary key
	constraint pk_cln_idcliente primary key (idcliente)
);	

-- Adicionando valores referentes a cada coluna da tabela cliente
INSERT INTO cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
VALUES
(1, 'Manoel', '88828383821', '32323', '2001-10-10', 'M', 'Estudante', 'Brasileira', 'Rua Joaquim Nabuco', '23', 'Casa', 'Cidade Nova', 'Porto União', 'SC'),
(2, 'Geraldo', '12343299291', '56565', '1987-10-04', 'M', 'Engenheiro', 'Brasileira', 'Rua das Limas', '200', 'Ap.', 'Centro', 'P. União', 'SC'),
(3, 'Carlos', '87732323227', '55463', '1967-10-01', 'M', 'Pedreiro', 'Brasileira', 'Rua das Laranjeiras', '300', 'Apart.', 'Cto.', 'Canoinhas', 'SC'),
(4, 'Adriana', '12321222122', '98777', '1989-09-10', 'F', 'Jornalista', 'Brasileira', 'Rua das Limas', '240', 'Casa', 'São Pedro', 'Porto Vitória', 'PR'),
(5, 'Amanda', '99982838828', '28382', '1991-03-04', 'F', 'Jorn.', 'Italiana', 'Av.Central', '100', null, 'São Pedro', 'General Carneiro', 'PR'),
(6, 'Ãngelo', '99982828181', '12323', '2000-01-01', 'M', 'Professor', 'Brasileiro', 'Av. Beira Mar', '300', null, 'Ctr.', 'São Paulo', 'SP'),
(7, 'Anderson', null, null, null, 'M', 'Prof', 'Italiano', 'Av. Brasil', '100', 'Apartamento', 'Santa Rosa', 'Rio de Janeiro', 'SP'),
(8, 'Camila', '9998282828', null, '2001-10-10', 'F', 'Professora', 'Norte america', 'Rua Central', '4333', null, 'Centro', 'Porto Alegre', 'RS'),
(9, 'Cristiano', null, null, null, 'M', 'Estudante', 'Alemã', 'Rua do Centro', '877', 'Casa', 'Centro', 'Porto Alegre', 'RS'),
(10, 'Fabrício', '8828282828', '32323', null, 'M', 'Estudante', 'Brasileira', null ,null, null, null, 'PU', 'SC'),
(11, 'Fernada', null, null, null, 'F', null, 'Brasileira', null, null, null, null, 'Porto União', 'SC'),
(12, 'Gilmar', '88881818181', '888', '2000-02-10', 'M', 'Estud.', null, 'Rua das Laranjeiras', '200', null, 'C. Nova', 'Canoinhas', 'SC'),
(13, 'Diego', '1010191919', '111939', null, 'M', 'Professor', 'Alemão', 'Rua Central', '455', 'Casa', 'Cidade N.', 'São Paulo', 'SP'),
(14, 'Jeferson', null, null, '1983-07-01', 'M', null, 'Brasileiro', null, null, null, null, 'União da Vitória', 'PR'),
(15, 'Jessica', null, null, null, 'F', 'Estudante', null, null, null, null, null, 'União da Vitória', 'PR');

SELECT * FROM cliente; -- Visualiza a tabela inteira, (Select = Selecionar | * = Tudo | From = de | Cliente = Tabela do cliente)

select nome, data_nascimento from cliente;	-- Visualiza apenas o nome é data de nascimento da tabela

select nome as "Nome", data_nascimento as "Data de Nascimento" from cliente; -- Visualizando é mudando o nome da coluna (nome, para Nome) é (data_nascimento, para Data de Nascimento)

select 'CPF: ' || cpf || ' RG: ' || rg as "CPF e RG" from cliente; -- Contatenando o CPF é o RG (Juntando os dois)

select * from cliente limit 3; -- Visualiza apenas os 3 primeiros clientes da tabela

select nome, data_nascimento from cliente where data_nascimento > '2000-01-01'; -- Visualiza apenas os clientes que a data de nascimento é maior que '2000-01-01' (where = onde)

select nome from cliente where nome like 'C%'; -- Visualiza apenas os clientes que começa com a letra "C", (% = seguido de zero ou mais caracteres quaisquer) (like = como)

select nome from cliente where nome like '%c%'; -- Buscando clientes que tem a letra "C" no nome

select nome, data_nascimento from cliente where data_nascimento between '1990-01-01' and '1998-01-01'; -- Filtra todos clientes com datas entre 1990 é 1998(between = Entre)

select nome, rg	from cliente where rg is null; -- Selecionando pessoas com RG nulo(vazio)

select nome from cliente order by nome asc; -- Ordena os nomes em Ordem Alfabetica

select nome from cliente order by nome desc; -- Decrescente


-- Exercícios – consultas simples
-- 1. O nome, o gênero e a profissão de todos os clientes, ordenado pelo nome em ordem decrescente
select nome, genero, profissao from cliente order by nome desc;

-- 2. Os clientes que tenham a letra “R” no nome
select nome from cliente where nome like '%r%';

-- 3. Os clientes que o nome inicia com a letra “C”
select nome from cliente where nome like 'C%';

-- 4. Os clientes que o nome termina com a letra “A”
select nome from cliente where nome like '%a';

-- 5. Os clientes que moram no bairro “Centro”
select nome, bairro from cliente where bairro = 'Centro' or bairro = 'Cto.' or bairro = 'Ctr.';

-- 6. Os clientes que moram em complementos que iniciam com a letra “A”
select nome, complemento from cliente where complemento like 'A%'

-- 7. Somente os clientes do sexo feminino
select nome, genero from cliente where genero like 'F';

-- 8. Os clientes que não informaram o CPF
select nome, cpf from cliente where cpf is null;
 
-- 9. O nome e a profissão dos clientes, ordenado em ordem crescente pelo nome da profissão
select nome, profissao from cliente order by profissao, nome asc;

-- 10. Os clientes de nacionalidade “Brasileira”
select nome, nacionalidade from cliente where nacionalidade like 'Brasileira';

-- 11. Os clientes que informaram o número da residência
select nome, numero from cliente where numero is not null;

-- 12. Os clientes que moram em Santa Catarina
select nome, uf from cliente where uf like 'SC';

-- 13. Os clientes que nasceram entre 01/01/2000 e 01/01/2002
select nome, data_nascimento from cliente where data_nascimento between '2000-01-01' and '2002-01-01';

-- 14. O nome do cliente e o logradouro, número, complemento, bairro, município e UF concatenado de todos os clientes
select 'Nome: ' || nome || ' | Logradouro: ' || logradouro || ' | Número: ' || numero || ' | Complemento: ' || complemento || ' | Bairro: ' || bairro || ' | Município: ' || municipio || ' | UF: ' || uf as "Nome e Endereço" from cliente;

select * from cliente;
update cliente set nome = 'Teste' where idcliente = 1; -- !!COMANDO PERIGOSO!!, lembrar de indicar o ID do Cliente antes de alterar, caso contrario ira mudar de todas pessoas.

update cliente set nome = 'Adriano', genero = 'M', numero = '241' where idcliente = 4;

insert into cliente (idcliente, nome) values (16, 'João')

delete from cliente where idcliente = 16; -- !!COMANDO PERIGOSO!!, lembrar de indicar o ID do Cliente, caso contrario ira apagar todos os clientes.

-- Exercícios – comandos update e delete
-- 1. Insira os dados abaixo na tabela de clientes

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values
(16, 'Maicon', '12349596421', '1234', '1965-10-10', 'F', 'Empresário', null, null, null, null, null, 'Florianópolis', 'PR'),
(17, 'Getúlio', null, '4631', null, 'F', 'Estudante', 'Brasileira', 'Rua Central', '343', 'Apartamento', 'Centro', 'Curitiba', 'SC'),
(18, 'Sandra', null, null, null, 'M', 'Professor', 'Italiana', null, '12', 'Bloco A', null, null, null)

-- 2. Altere os dados do cliente Maicon
	-- a. O CPF para 45390569432
	-- b. O gênero para M
	-- c. A nacionalidade para Brasileira
	-- d. O UF para SC

update cliente set cpf = '45390569432' where idcliente = 16;
update cliente set genero = 'M' where idcliente = 16;
update cliente set nacionalidade = 'Brasileira' where idcliente = 16;
update cliente set UF = 'SC' where idcliente = 16;

select * from cliente;

-- 3. Altere os dados do cliente Getúlio
	-- a. A data de nascimento para 01/04/1978
	-- b. O gênero para M

update cliente set data_nascimento = '1978-04-01' where idcliente = 17;
update cliente set genero = 'M' where idcliente = 17;

-- 4. Altere os dados da cliente Sandra
	-- a. O gênero para F
	-- b. A profissão para Professora
	-- c. O número para 123

update cliente set genero = 'F' where idcliente = 18;
update cliente set profissao = 'Professora' where idcliente = 18;
update cliente set numero = '123' where idcliente = 18;

select * from cliente;

delete from cliente where idcliente = 16;
delete from cliente where idcliente = 18;
	
select * from cliente;

-- Criando tabela profissao

create table profissao (
	idprofissao integer not null,
	nome varchar(30) not null,

	constraint pk_prf_idprofissao primary key (idprofissao),
	constraint un_prf_nome unique (nome)
);

-- Adicionando valores na tabela profissao

insert into profissao (idprofissao, nome)
values
(1, 'Estudante'),
(2, 'Engenheiro'),
(3, 'Pedreiro'),
(4, 'Jornalista'),
(5, 'Professor');

select * from profissao
select profissao from cliente

-- Criando tabela nacionalidade

create table nacionalidade (
	idnacionalidade integer not null,
	nome varchar(30) not null,

	constraint pk_ncn_idnacionalidade primary key (idnacionalidade),
	constraint un_ncn_nome unique (nome)
);

select nacionalidade from cliente;

-- Adicionando valores na tabela nacionalidade

insert into nacionalidade (idnacionalidade, nome)
values
(1, 'Brasileira'),
(2, 'Italiana'),
(3, 'Norte-americana'),
(4, 'Alemã');

select * from nacionalidade;

-- Criando a tabela complemento

create table complemento (
	idcomplemento integer not null,
	nome varchar(30) not null,

	constraint pk_cpl_idcomplemento primary key (idcomplemento),
	constraint un_cpl_nome unique (nome)
);

-- Adicionando valores na tabela complemento

insert into complemento (idcomplemento, nome)
values
(1, 'Casa'),
(2, 'Apartamento');

select * from complemento;

-- Criando a tabela bairro

create table bairro (
	idbairro integer not null,
	nome varchar(30) not null,

	constraint pk_brr_idbairro primary key (idbairro),
	constraint un_brr_nome unique (nome)
);

insert into bairro (idbairro, nome)
values
(1, 'Cidade Nova'),
(2, 'Centro'),
(3, 'São Pedro'),
(4, 'Santa Rosa');

select * from bairro;

select * from cliente;

-- Altera a estrutura de uma tabela em um banco de dados

alter table cliente rename column profissao to idprofissao;

alter table cliente rename column idprofissao type integer;
-- Estudante -> 1, 9, 10, 12, 15
-- Engenheiro -> 2
-- Pedreiro -> 3
--Jornalista -> 4, 5
-- Professor -> 6, 7, 8, 13
-- Null -> 11,14
alter table cliente drop idprofissao;
alter table cliente add idprofissao integer;
alter table cliente add constraint fk_cln_idprofissao foreign key (idprofissao) references profissao (idprofissao);

-- Definindo o que cada ID de profissao será

update cliente set idprofissao = 1 where idcliente in (1, 9, 10, 12, 15, 17);
update cliente set idprofissao = 2 where idcliente = 2;
update cliente set idprofissao = 3 where idcliente = 3;
update cliente set idprofissao = 4 where idcliente in (4, 5);
update cliente set idprofissao = 5 where idcliente in (6, 7, 8, 13);

select * from cliente;

select * from profissao;

-- Deletando a profissao 01
	--Obs: não da pra excluir quando tem algum cliente vinculado a profissao

delete from profissao where idprofissao = 1;

-- Adicionando uma profissao de Teste

insert into profissao (idprofissao, nome)
values
(10, 'Teste');

-- Deletando a profissao de Teste
	--Obs: funciona pois nenhum cliente está vinculado a ela

delete from profissao where idprofissao = 10;
