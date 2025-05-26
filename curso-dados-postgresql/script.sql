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

SELECT * FROM cliente;