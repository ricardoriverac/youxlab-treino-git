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