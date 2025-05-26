create table cliente (
    idcliente integer not null,
    nome varchar(50) not null, -- Pedro, 45
    cpf char(11),
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
);    

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nascionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (1, "Manoel", "88828383821", "32323", "2001-01-30", "M", "Estudante", "Brasileira", "Rua Joaquim Nabuco", "23", "Casa", "Cidade Nova", "Porto União", "SC");