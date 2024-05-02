
DROP DATABASE IF EXISTS FILMES;
GO

CREATE DATABASE FILMES;
GO

USE FILMES;
GO

-- DB FILMES
CREATE TABLE GENERO
(
ID_GENERO INT NOT NULL PRIMARY KEY,
NOME_GENERO VARCHAR(500) NOT NULL
);
GO

CREATE TABLE FILME
(
ID_FILME INT NOT NULL PRIMARY KEY,
NOME_TITULO VARCHAR(500) NOT NULL,
ID_GENERO INT NOT NULL FOREIGN KEY REFERENCES GENERO(ID_GENERO)
);
GO

INSERT INTO GENERO (ID_GENERO, NOME_GENERO)
VALUES
(1, 'Animação'),
(2, 'Aventura'),
(3, 'Drama'),
(4, 'Ficção'),
(5, 'Guerra'),
(6, 'Musical'),
(7, 'Policial'),
(8, 'Terror');
GO

INSERT INTO FILME (ID_FILME, NOME_TITULO, ID_GENERO)
VALUES
(1,'Rede de ódio',3),
(2,'1917',5),
(3,'Ad Astra',4),
(4,'Coringa',4),
(5,'Dois Papas',3),
(6,'Ford vs Ferrari',2),
(7,'Klaus',1),
(8,'O Irlandês',3),
(9,'Parasita',3),
(10,'Retrato de uma Jovem em Chamas',3),
(11,'Vingadores: ultimato',4),
(12,'Assassinato às Cegas',7),
(13,'Bird box',4),
(14,'Bohemian Rhapsody',3),
(15,'Cafarnaum',3),
(16,'Desejo de matar 2018',7),
(17,'Green book: o guia',3),
(18,'Homem-Aranha no Aranhaverso',1),
(19,'Vingadores Guerra infinita',4),
(20,'A forma da água',3),
(21,'Corra!',8),
(22,'Dunkirk',5),
(23,'Logan',2),
(24,'Neve Negra',3),
(25,'O destino de uma nação',5),
(26,'O outro irmão',3),
(27,'Órbita 9',4),
(28,'Roma',3),
(29,'Shimmer Lake',7),
(30,'The post',3),
(31,'Três anúncios para um crime',3),
(32,'Vikram Vedha',2),
(33,'Viva: A Vida é uma Festa',1),
(34,'A chegada',3),
(35,'A criada',3),
(36,'A voz do silêncio',1),
(37,'Até o Último Homem',3),
(38,'Dangal',3),
(39,'Dinheiro em jogo',7),
(40,'La La Land: Cantando Estações',6),
(41,'Moonlight: Sob a Luz do Luar',3),
(42,'No fim do túnel',3),
(43,'Um contratempo',7),
(44,'Um dia perfeito',5),
(45,'Your name',1),
(46,'Zootopia',1);
GO