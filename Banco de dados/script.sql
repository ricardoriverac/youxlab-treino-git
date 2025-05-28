create table cliente (
    idcliente integer not null, -- número único que identifica o cliente (tipo um código)
    nome varchar(50) not null, -- nome da pessoa (até 50 letras)
    cpf char(11), -- CPF com 11 caracteres.
    rg varchar(15), --número do RG.
    data_nascimento date, -- inserir a data de nascimento no formato date
    genero char(1), -- genero com um unico caracter
    profissao varchar(30), -- profissao (até 30 letras)
    nascionalidade varchar(30), -- nacionalidade (até 30 letras)
    logradouro varchar(30), -- logradouro ate ( ate 30 letras)
    numero varchar(10), -- numero (ate 10 caracter)
    complemento varchar(30), -- ()
    bairro varchar(30),
    municipio varchar(30),
    uf varchar(30),
    observacoes text,
   --char é usado para armazenar uma string com um comprimento fixo
   -- varchar é usado para armazenar cordas com um comprimento variável
    -- primary key
    constraint pk_cln_idcliente primary key (idcliente) -- chave primária, ou seja, não pode repetir.
);    

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nascionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values(1, 'Manoel', '88828383821', '32323', '2001-10-10', 'M', 'Estudante', 'Brasileira', 'Rua Joaquim Nabuco', '23', 'Casa', 'Cidade Nova', 'Porto União', 'SC'),
(2, 'Geraldo', '12343299291', '56565', '1987-10-04', 'M', 'Engenheiro', 'Brasileira', 'Rua das Limas', '200', 'Ap.', 'Centro', 'P. União', 'SC'),
(3, 'Carlos', '87732323227', '55463', '1967-10-01', 'M', 'Pedreiro', 'Brasileira', 'Rua das Laranjeiras', '300', 'Apart.', 'Cto.', 'Canoinhas', 'SC'),
(4, 'Adriana', '12321222122', '98777', '1989-09-10', 'F', 'Jornalista', 'Brasileira', 'Rua das Limas', '240', 'Casa', 'São Pedro', 'Porto Vitória', 'PR'),
(5, 'Amanda', '99982838828', '28382', '1991-03-04', 'F', 'Jorn.', 'Italiana', 'Av.Central', '100', null, 'São Pedro', 'General Carneiro', 'PR'),
(6, 'Ãngelo', '99982828181', '12323', '2000-01-01', 'M', 'Professor', 'Brasileiro', 'Av. Beira Mar', '300', null, 'Ctr.', 'São Paulo', 'SP'),
(7, 'Anderson', null, null, null, 'M', 'Prof', 'Italiano', 'Av. Brasil', '100', 'Apartamento', 'Santa Rosa', 'Rio de Janeiro', 'SP'),
(8, 'Camila', '9998282828', null, '2001-10-10', 'F', 'Professora', 'Norte america', 'Rua Central', '4333', null, 'Centro', 'Porto Alegre', 'RS'),
(9, 'Cristiano', null, null, null, 'M', 'Estudante', 'Alemã', 'Rua do Centro', '877', 'Casa', 'Centro', 'Porto Alegre', 'RS'),
(10, 'Fabrício', '8828282828', '32323', null, 'M', 'Estudante', 'Brasileira', null, null, null, null, 'PU', 'SC'),
(11, 'Fernada', null, null, null, 'F', null, 'Brasileira', null, null, null, null, 'Porto União', 'SC'),
(12, 'Gilmar', '88881818181', '888', '2000-02-10', 'M', 'Estud.', null, 'Rua das Laranjeiras', '200', null, 'C. Nova', 'Canoinhas', 'SC'),
(13, 'Diego', '1010191919', '111939', null, 'M', 'Professor', 'Alemão', 'Rua Central', '455', 'Casa', 'Cidade N.', 'São Paulo', 'SP'),
(14, 'Jeferson', null, null, '1983-07-01', 'M', null, 'Brasileiro', null, null, null, null, 'União da Vitória', 'PR'),
(15, 'Jessica', null, null, null, 'F', 'Estudante', null, null, null, null, null, 'União da Vitória', 'PR'); 	
select * from cliente;

select nome, data_nascimento from cliente;  --selecionar a coluna nome e data de nascmento  da tabela cliente e ira mostrar somente essas colunas
select nome, data_nascimento  as "Data de nascimento" from cliente; -- renomeiar uma coluna
select  'CPF: ' || cpf || 'RG: ' || rg as "CPF e RG" from cliente; -- aqui vemos dois || que serve para fazer a concateçao sao chamadas de pipe um exemplo e que esta concatenando o a string CPF com o campo cpf, tornando se apenas uma cpo
select * from  cliente  limit 3; -- indica que  vai selecionar  somente 3/1 clientes da base de dados na ordem que eles aparecem 
select nome, data_nascimento from cliente where data_nascimento  > '2000_01_21'; -- nesse comando tmeos um filtro "where" traduzido 'onde' que faz com que vc consiga filtrar oque vc quer mostrar, neste codigo como exemplo foi a data de nascimento
select nome from cliente where nome like 'C%' ; -- basicamente o mesmo esquema de filtro so que o "like" traduzido "como" faz com que todo nome que comça com a letra C apareça, e o "%" e para retornar tudo que estiver depois da letra C 
select nome , data_nascimento from cliente where data_nascimento between '1990-01-01' and '1998-01-01'; -- isso indica que nos queremos filtrar todos os clientes que nasceram a data '1990-01-01' entre 1998-01-01
select nome from cliente where nome like '%c%'; --significa que começa com qualquer caracter e termina com qualquer caracter e no meio C
select nome , rg from cliente where rg  is nul; -- vaai mostar todos rgs que estao sem nada 'null']
select nome from cliente order by nome asc ; -- vaimostrar em ordem alfabetica 'asc' significa ordem crescente
select nome from cliente order by nome desc; --vai mostrar order decrescente 

--1. O nome, o gênero e a profissão de todos os clientes, ordenado pelo nome em ordem decrescente

--2. Os clientes que tenham a letra “R” no nome

--3. Os clientes que o nome inicia com a letra “C”

--4. Os clientes que o nome termina com a letra “A”

--5. Os clientes que moram no bairro “Centro”

--6. Os clientes que moram em complementos que iniciam com a letra “A”

--7. Somente os clientes do sexo feminino

--8. Os clientes que não informaram o CPF

--9. O nome e a profissão dos clientes, ordenado em ordem crescente pelo nome da profissão

--10. Os clientes de nacionalidade “Brasileira”

--11. Os clientes que informaram o número da residência

--12. Os clientes que moram em Santa Catarina

--13. Os clientes que nasceram entre 01/01/2000 e 01/01/2002

--14. O nome do cliente e o logradouro, número, complemento, bairro, município e UF concatenado de todos os clientes
 -- 1 EXERCICIO
select nome, genero ,profissao from cliente order by nome desc;
 -- 2 EXERCICIO
select nome from cliente where nome like '%r%';
 -- 3 EXERCICIO
select nome from cliente where nome like 'C%';
-- 4 EXERCICIO
select nome from cliente where nome like '%a';
-- 5 EXERCICIO
select nome , bairro from cliente where bairro like 'Centro';
-- 6 EXERCICIO
select nome , complemento from cliente where complemento  like 'A%';
-- 7 EXERCICIO
select nome from cliente where genero like 'F';
-- 8 EXERCICIO
select nome , cpf from cliente where cpf  is  null;
-- 9 EXERCICIO
select nome , profissao from cliente order by nome , profissao desc;
-- 10 EXERCICIO
select nome , nascionalidade from cliente where nascionalidade like 'B%';
-- 11 EXERCICIO
select nome , numero from cliente where numero like'%';
-- 12 EXERCICIO
select nome , bairro from cliente where uf like 'SC';
-- 13 EXERCICIO
select nome , data_nascimento from cliente where data_nascimento between '2000-01-01' and '2002-01-01';
-- 14 EXERCICIO
select 'NOME: '|| nome || ' LOGRADOURO: ' || logradouro || ' NUMERO: ' || numero || ' COMPLEMENTO: ' || complemento || ' BAIRRO: ' || bairro || ' MUNICIPIO: ' || municipio|| 'UF: ' || Uf as "NOME E ENDEREÇO" from cliente;

select * from cliente; 
update cliente  set nome = 'Teste' where idcliente = 1; --atulize a tabela de cliente mudando o nome que esta no  idcliente 1 
update cliente set nome = 'Adriano', genero = 'M', numero =  '241' where idcliente = 4; 
insert  into cliente (idcliente, nome ) values (16, 'João');
delete from cliente where  idclente = 16; 