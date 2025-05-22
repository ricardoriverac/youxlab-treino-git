CREATE TABLE IF NOT EXISTS cliente (
    idcliente INTEGER NOT NULL,
    nome VARCHAR(50) NOT NULL,
    cpf CHAR(11),
    rg VARCHAR(15),
    data_nascimento DATE,
    genero CHAR(1),
    profissao VARCHAR(30),
    nacionalidade VARCHAR(30),
    logradouro VARCHAR(30),
    numero VARCHAR(10),
    complemento VARCHAR(30),
    bairro VARCHAR(30),
    municipio VARCHAR(30),
    uf CHAR(2),
    observacoes TEXT,
    CONSTRAINT pk_cliente PRIMARY KEY (idcliente)
);
ALTER TABLE cliente ADD COLUMN nacionalidade VARCHAR(30);

select * from cliente
 insert into cliente (idcliente, nome, cpf, rg, data_nascimento,genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio,uf )
 values (1, 'Manoel','88823478910', '45673', '2001-01-19', 'M', 'estudante', 'Brasileira',' rua joaquim','23', 'casa', 'cidade nova','Porto uniao','sc')
DELETE FROM cliente WHERE idcliente = 2;

insert into cliente (idcliente, nome, cpf, rg, data_nascimento,genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio,uf )
 values (2, 'Geraldo','1234299929', '56565', '1987-01-04', 'M', 'engenheiro', 'Brasileira',' rua jardins lima','200', 'ap', 'centro','P.Uniao','SC')
 
insert into cliente (idcliente, nome, cpf, rg, data_nascimento,genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio,uf )
 values (3, 'Carlos','88823478910', '55463', '1967-10-01', 'M', 'pedreiro', 'Brasileira',' rua das larangeiras','300', 'Apart.', 'Cto','Canoinhas','sc')
 
 insert into cliente (idcliente, nome, cpf, rg, data_nascimento,genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio,uf )
 values (4, 'Adriana','1232122122', '98777', '1989-09-10', 'F', 'jornalista', 'Brasileira',' rua das lima','240', 'casa.', 'Sao Pedro','Porto Vitoria','PR')

insert into cliente (idcliente, nome, cpf, rg, data_nascimento,genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio,uf )
 values (5, 'Amanda','99982838828', '28382', '1991-03-04', 'F', 'jor', 'Italiana','Av. Central','100', null, 'Sao Pedro','General Carneiro','PR')

insert into cliente (idcliente, nome, cpf, rg, data_nascimento,genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio,uf )
 values (6, 'Angelo','99982828181', '12323', '2000-01-01', 'M', 'Professor', 'Norte americana','Rua central','4333', null, 'ctr.','Sao Paulo','SP')

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (7, 'Anderson', null, null, null, 'M', 'Prof.', 'Italiano', 'Av. Brasil', '100', 'Apartamento', 'Santa Rosa', 'Rio de Janeiro', 'SP');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (8, 'Camila', '09998282828', null, '2001-10-10', 'F', 'Professora', 'Norte americana', 'Rua Central', '4333', null, 'Centro', 'Uberlândia', 'MG');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (9, 'Cristiano', null, null, null, 'M', 'Estudante', 'Alemã', 'Rua do Centro', '877', 'Casa', 'Centro', 'Porto Alegre', 'RS');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (10, 'Fabrício', '8828282828', '32323', null, 'M', 'Estudante', 'Brasileiro', null, null, null, 'Centro', 'Porto União', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (11, 'Fernanda', null, null, null, 'F', null, 'Brasileira', null, null, null, 'Porto', 'União', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (12, 'Gilmar', '88881818181', '888', '2000-02-10', 'M', 'Estud.', null, 'Rua das Laranjeiras', '200', null, 'C. Nova', 'Canoinhas', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (13, 'Diego', '01010191919', '111939', null, 'M', 'Professor', 'Alemão', 'Rua Central', '455', 'Casa', 'Cidade N.', 'São Paulo', 'SP');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (14, 'Jeferson', null, null, '1983-07-01', 'M', null, 'Brasileiro', null, null, null, 'União da Vitória', 'União da Vitória', 'PR');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (15, 'Jessica', null, null, null, 'F', 'Estudante', null, null, null, null, null, 'União da Vitória', 'PR');








 