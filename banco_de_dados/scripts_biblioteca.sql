create table editora (
	id_editora serial not null,
	nome varchar(50) not null,

	constraint pk_id_editora primary key (id_editora),
	constraint un_id_editora_nome unique (nome)
);

insert into editora (nome) values ('Bookman');
insert into editora (nome) values ('Edgard Blusher');
insert into editora (nome) values ('Nova Terra');
insert into editora (nome) values ('Brasport');

SELECT * FROM editora

create table categoria (
	id_categoria serial not null,
	nome varchar(50) not null,

	constraint pk_idcategoria_id primary key (id_categoria),
	constraint un_categoria_nome unique (nome)
);

select * from categoria

insert into categoria (nome) values('Banco de Dados');
insert into categoria (nome) values('HTML');
insert into categoria (nome) values('Java');
insert into categoria (nome) values('PHP');

create table autor (
	id_autor serial not null,
	nome varchar(50) not null,
	
	constraint pk_idautor_id primary key (id_autor)
);

insert into autor (nome) values 
('Waldemar Setzer');
insert into autor (nome) values 
('Flávio Soares');
insert into autor (nome) values 
('John Watson');
insert into autor (nome) values
('Rui Rossi dos Santos');
insert into autor (nome) values
('Antonio Pereira de Resende');
insert into autor (nome) values
('Claudiney Calixto Lima');
insert into autor (nome) values
('Evandro Carlos Teruel');
insert into autor (nome) values
('Ian Graham');
insert into autor (nome) values
('Fabrício Xavier');
insert into autor (nome) values
('Pablo Dalloglio');

select * from autor

create table livro (
	id_livro serial not null,
	id_editora integer not null,
	id_categoria integer not null,
	nome varchar(50) not null,

	constraint pk_idlivro_id primary key (id_livro),
	constraint fk_ideditora_id foreign key (id_editora) references editora (id_editora),
	constraint fk_idcategoria_id foreign key (id_categoria) references categoria (id_categoria),
	constraint un_idlivro_nome unique (nome)
);



