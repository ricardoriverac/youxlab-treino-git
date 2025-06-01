create table editora (
	ideditora serial not null,
	nome varchar(50) not null,
	
	constraint pk_edt_ideditora primary key (ideditora),
	constraint un_edt_nome unique (nome)
);

insert into editora (nome) values ('Bookman');
insert into editora (nome) values ('Edgard Bushler');
insert into editora (nome) values ('Nova Terra');
insert into editora (nome) values ('Brasport');
select * from editora

create table categoria (
	idcategoria serial not null,
	nome varchar(50) not null,
	
	constraint pk_ctg_idecategoria primary key (idcategoria),
	constraint un_ctg_nome unique (nome)
);

insert into categoria (nome) values ('Banco de Dados');
insert into categoria (nome) values ('HTML');
insert into categoria (nome) values ('Java');
insert into categoria (nome) values ('PHP');
select * from categoria


create table autor (
	idautor serial not null,
	nome varchar(50) not null,
	
	constraint pk_atr_idautor primary key (idautor),
	constraint un_atr_nome unique (nome)
);

insert into autor (nome) values ('Waldemar Setzer');
insert into autor (nome) values ('Flávio Soares');
insert into autor (nome) values ('John Watson');
insert into autor (nome) values ('Rui Rossi dos Santos');
insert into autor (nome) values ('Antonio Pereira de Resende');
insert into autor (nome) values ('Cladiney Calixto Lima');
insert into autor (nome) values ('Evandro Carlos Teruel');
insert into autor (nome) values ('Ian Graham');
insert into autor (nome) values ('Fabrício Xavier');
insert into autor (nome) values ('Pablo Dalloglio');
select * from autor

create table livro (
	idlivro serial not null,
	ideditora integer not null,
	idcategoria integer not null,
	nome varchar(50) not null,
	
	constraint pk_lvr_idlivro primary key (idlivro),
	constraint fk_lvr_ideditora foreign key (ideditora) references editora (ideditora),
	constraint fk_lvr_idcategoria foreign key (idcategoria) references categoria (idcategoria),
	constraint un_lvr_nome unique (nome)
);

alter table livro alter column nome type varchar(70);

select * from editora
select * from categoria

insert into livro (ideditora, idcategoria, nome) values (2, 1, 'Banco de Dados - 1 Edição');
insert into livro (ideditora, idcategoria, nome) values (1, 1, 'Oracle Database 11G Adminstração');
insert into livro (ideditora, idcategoria, nome) values (3, 3, 'Programação de Computadores em Java');
insert into livro (ideditora, idcategoria, nome) values (4, 3, 'Programação Orientada a Aspectos em Java');
insert into livro (ideditora, idcategoria, nome) values (4, 2, 'HTML5 Guia Prático');
insert into livro (ideditora, idcategoria, nome) values (3, 2, 'XHTML: Guia de Referência para Desenvolvimento na Web');
insert into livro (ideditora, idcategoria, nome) values (1, 4, 'PHP para Desenvolvimento Profissional');
insert into livro (ideditora, idcategoria, nome) values (2, 4, 'PHP com Programação Orientada a Objetos');
select * from livro

drop table livro_autor
create table livro_autor (
	idlivro integer not null,
	idautor integer not null,
	
	constraint pk_ltr_idlivroautor primary key (idlivro, idautor),
	constraint fk_ltr_idlivro foreign key (idlivro) references livro (idlivro),
	constraint fk_ltr_idautor foreign key (idautor) references autor (idautor)
);


select * from livro
select * from autor
insert into livro_autor (idlivro, idautor) values (6, 1);
insert into livro_autor (idlivro, idautor) values (6, 2);
insert into livro_autor (idlivro, idautor) values (7, 3);
insert into livro_autor (idlivro, idautor) values (8, 4);
insert into livro_autor (idlivro, idautor) values (9, 5);
insert into livro_autor (idlivro, idautor) values (9, 6);
insert into livro_autor (idlivro, idautor) values (10, 7);
insert into livro_autor (idlivro, idautor) values (11, 8);
insert into livro_autor (idlivro, idautor) values (12, 9);
insert into livro_autor (idlivro, idautor) values (13, 10);
select * from livro_autor

create table aluno (
	idaluno serial not null,
	nome varchar(50) not null,
	
	constraint pk_aln_idaluno primary key (idaluno),
	constraint un_aln_nome unique (nome)
);

insert into aluno (nome) values ('Mario');
insert into aluno (nome) values ('João');
insert into aluno (nome) values ('Paulo');
insert into aluno (nome) values ('Pedro');
insert into aluno (nome) values ('Maria');
select * from aluno

create table emprestimo (
	idemprestimo serial not null,
	idaluno integer not null,
	data_emprestimo date not null default current_date,
	data_devolucao date not null,
	valor float default 0,
	devolvido char(1) not null,
	
	constraint pk_emp_idemprestimo primary key (idemprestimo),
	constraint fk_emp_idaluno foreign key (idaluno) references aluno (idaluno)
);

select * from aluno
insert into emprestimo (idaluno, data_emprestimo, data_devolucao, valor, devolvido) values (1, '2012-05-02', '2012-05-12', 10, 'S');
insert into emprestimo (idaluno, data_emprestimo, data_devolucao, valor, devolvido) values (1, '2012-04-23', '2012-05-03', 5, 'N');
insert into emprestimo (idaluno, data_emprestimo, data_devolucao, valor, devolvido) values (2, '2012-05-10', '2012-05-20', 12, 'N');
insert into emprestimo (idaluno, data_emprestimo, data_devolucao, valor, devolvido) values (3, '2012-05-10', '2012-05-20', 8, 'S');
insert into emprestimo (idaluno, data_emprestimo, data_devolucao, valor, devolvido) values (4, '2012-05-05', '2012-05-15', 15, 'N');
insert into emprestimo (idaluno, data_emprestimo, data_devolucao, valor, devolvido) values (4, '2012-05-07', '2012-05-17', 20, 'S');
insert into emprestimo (idaluno, data_emprestimo, data_devolucao, valor, devolvido) values (4, '2012-05-08', '2012-05-18', 5, 'S');
select * from emprestimo

create table emprestimo_livro (
	idemprestimo integer not null,
	idlivro integer not null,
	
	constraint pk_elv_idemprestimolivro primary key (idemprestimo, idlivro),
	constraint fk_elv_idemprestimo foreign key (idemprestimo) references emprestimo (idemprestimo),
	constraint fk_elv_idlivro foreign key (idlivro) references livro (idlivro)
);

select * from aluno
select * from emprestimo
select * from livro

insert into emprestimo_livro (idemprestimo, idlivro) values (1, 6);
insert into emprestimo_livro (idemprestimo, idlivro) values (2, 9);
insert into emprestimo_livro (idemprestimo, idlivro) values (2, 8);
insert into emprestimo_livro (idemprestimo, idlivro) values (3, 7);
insert into emprestimo_livro (idemprestimo, idlivro) values (3, 12);
insert into emprestimo_livro (idemprestimo, idlivro) values (4, 10);
insert into emprestimo_livro (idemprestimo, idlivro) values (5, 9);
insert into emprestimo_livro (idemprestimo, idlivro) values (6, 11);
insert into emprestimo_livro (idemprestimo, idlivro) values (6, 6);
insert into emprestimo_livro (idemprestimo, idlivro) values (7, 13);
select * from emprestimo_livro

create index idx_emp_data_emprestimo on emprestimo (data_emprestimo);
create index idx_emp_data_devolucao on emprestimo (data_devolucao);

-- CONSULTAS SIMPLES
-- O nome dos autores em ordem alfabética.
select nome from autor order by nome

-- O nome dos alunos que começam com a letra P.
select nome from aluno where nome like 'P%'

-- O nome dos livros da categoria Banco de Dados ou Java.
select * from categoria
select nome from categoria where idcategoria = 1 or idcategoria = 3

-- O nome dos livros da editora Bookman.
select * from editora
select nome from livro where ideditora = 1

-- Os empréstimos realizados entre 05/05/2012 e 10/05/2012.
select * from emprestimo where data_emprestimo between '2012-05-05' and '2012-05-10'

-- Os empréstimos que não foram feitos entre 05/05/2012 e 10/05/2012
select * from emprestimo where data_emprestimo not between '2012-05-05' and '2012-05-10'

-- Os empréstimos que os livros já foram devolvidos.
select * from emprestimo where devolvido = 'S'

-- CONSULTAS COM AGRUPAMENTO SIMPLES
-- A quantidade de livros.
select count(idlivro) from livro

-- 27. O somatório do valor dos empréstimos.
select sum(valor) from emprestimo

-- 28. A média do valor dos empréstimos.
select avg(valor) from emprestimo

-- 29. O maior valor dos empréstimos.
select max(valor) from emprestimo

-- 30. O menor valor dos empréstimos.
select min(valor) from emprestimo

-- 31. O somatório do valor do empréstimo que estão entre 05/05/2012 e 10/05/2012.
select sum(valor) from emprestimo where data_emprestimo between '2012-05-05' and '2012-05-10'

-- 32. A quantidade de empréstimos que estão entre 01/05/2012 e 05/05/2012.
select count(idemprestimo) from emprestimo where data_emprestimo between '2012-05-01' and '2012-05-05'

-- CONSULTAS COM JOIN
-- 33. O nome do livro, a categoria e a editora (LIVRO) – fazer uma view
create view dados_livros as
select 
	liv.nome,
	cat.nome as categoria,
	edi.nome as editora
from 
	livro as liv
left outer join
	categoria as cat on liv.idcategoria = cat.idcategoria
left outer join
	editora as edi on liv.ideditora = edi.ideditora

select * from dados_livros

-- 34. O nome do livro e o nome do autor (LIVRO_AUTOR) – fazer uma view.
create view livro_autor_view as
select 
	liv.nome as livro,
	aut.nome as autor 
from 
	livro_autor as lva
left outer join 
	livro as liv on lva.idlivro = liv.idlivro
left outer join
	autor as aut on lva.idautor = aut.idautor

select * from livro_autor_view

-- 35. O nome dos livros do autor Ian Graham (LIVRO_AUTOR).
select * from autor
select * from livro_autor where idautor = 8

-- 36. O nome do aluno, a data do empréstimo e a data de devolução (EMPRESTIMO).
select 
	alu.nome as aluno,
	emp.data_emprestimo as emprestimo,
	emp.data_devolucao as devolucao
from
	emprestimo as emp
left outer join	
	aluno as alu on emp.idaluno = alu.idaluno

-- 37. O nome de todos os livros que foram emprestados (EMPRESTIMO_LIVRO).
select
	distinct(lvr.nome) as livro
from
	emprestimo_livro elv
left outer join
	livro lvr on elv.idlivro = lvr.idlivro

-- CONSULTAS COM AGRUPAMENTO + JOIN
-- 38. O nome da editora e a quantidade de livros de cada editora (LIVRO).
select
	edt.nome as editora,
	count(lvr.idlivro) as quantidade
from
	livro lvr
left outer join
	editora edt on lvr.ideditora = edt.ideditora
group by
	edt.nome

-- 39. O nome da categoria e a quantidade de livros de cada categoria (LIVRO).
select
	cat.nome,
	count(liv.idlivro) as quantidade
from
	livro as liv
left outer join	
	categoria as cat on liv.idcategoria = cat.idcategoria
group by
	cat.nome

-- 40. O nome do autor e a quantidade de livros de cada autor (LIVRO_AUTOR).
select 	
	aut.nome,
	count(lva.idlivro) as quantidade
from
	livro_autor as lva
left outer join
	autor as aut on lva.idautor = aut.idautor
group by
	aut.nome
	
-- 41. O nome do aluno e a quantidade de empréstimo de cada aluno (EMPRESTIMO_LIVRO).
select 
	aln.nome,
	count(emp.idemprestimo)
from emprestimo as emp
left outer join
	aluno as aln on emp.idaluno = aln.idaluno
group by
	aln.nome

-- 42. O nome do aluno e o somatório do valor total dos empréstimos de cada aluno (EMPRESTIMO).
select 
	aln.nome,
	sum(valor)
from emprestimo as emp
left outer join
	aluno as aln on emp.idaluno = aln.idaluno
group by 
	aln.nome

-- 43. O nome do aluno e o somatório do valor total dos empréstimos de cada aluno somente daqueles que o somatório for maior do que 7,00 (EMPRESTIMO).
select 
	aln.nome,
	sum(valor)
from emprestimo as emp
left outer join
	aluno as aln on emp.idaluno = aln.idaluno
group by 
	aln.nome
having
	sum(emp.valor) > 7 

-- CONSULTAS COMANDOS DIVERSOS
-- 44. O nome de todos os alunos em ordem decrescente e em letra maiúscula.
select upper(nome) from aluno order by nome desc	

-- 45. Os empréstimos que foram feitos no mês 04 de 2012.
select 
	data_emprestimo,
	extract(month from data_emprestimo),
	extract(year from data_emprestimo)
from 
	emprestimo
group by
	data_emprestimo
having 
	extract(month from data_emprestimo) = 04
-- Correção da 45
select * from emprestimo where extract(year from data_emprestimo) = 2012 and extract(month from data_emprestimo) = 4

-- 46. Todos os campos do empréstimo. Caso já tenha sido devolvido, mostrar a mensagem “Devolução completa”, senão “Em atraso”.
select 
	*,
	case devolvido
		when 'S' then 'Devolução completa'
		when 'N' then 'Em atraso'
	end as status
from
	emprestimo

-- 47. Somente o caractere 5 até o caractere 10 do nome dos autores.
select 
	nome,
	substring(nome from 5 for 10)
from 
	autor

-- 48. O valor do empréstimo e somente o mês da data de empréstimo. Escreva “Janeiro”, “Fevereiro”, etc
select
	valor,
	data_emprestimo,
	case extract(month from data_emprestimo)
		when 1 then 'Janeiro'
		when 2 then 'Fevereiro'
		when 3 then 'Março'
		when 4 then 'Abril'
		when 5 then 'Maio'
	end as mes
from
	emprestimo

-- SUBCONSULTAS
-- 49. A data do empréstimo e o valor dos empréstimos que o valor seja maior que a média de todos os empréstimos.
select
	data_emprestimo,
	valor
from
	emprestimo
where
	valor > (select avg(valor) from emprestimo)

-- 50. A data do empréstimo e o valor dos empréstimos que possuem mais de um livro.
select
	emp.data_emprestimo,
	emp.valor,
	(select count(elv.idemprestimo) from emprestimo_livro elv where elv.idemprestimo = emp.idemprestimo)
from
	emprestimo as emp
where
	(select 
	 	count(elv.idemprestimo) 
	 from 
	 	emprestimo_livro elv 
	  where elv.idemprestimo = emp.idemprestimo) >= 1

-- 51. A data do empréstimo e o valor dos empréstimos que o valor seja menor que a soma de todos os empréstimos.
select
	emp.data_emprestimo,
	emp.valor
from
	emprestimo as emp
where
	valor < (select sum(valor) from emprestimo)


select * from emprestimo_livro






select * from categoria
select * from emprestimo
select * from emprestimo_livro
select * from autor
select * from livro_autor
select * from livro