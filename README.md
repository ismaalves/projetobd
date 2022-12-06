# Projeto de Banco de Dados
## Alunos:

##### Ismael Alves Lima

##### Lucas Marques Bezerra

##### Vladimir Yuri Farias de Lima Cavalcanti


## Construir um sistema para o Cinema Sauro

### Primeira etapa

Fazer o modelo e-r completo do sistema selecionado, definindo todas as entidades e relacionamentos necessários ao sistema, suas restrições de integridade e cardinalidades. Também devem especificar o modelo relacional do sistema selecionado, tomando como base o modelo conceitual e-r já previamente definido, mostrando os atributos chaves das tabelas, como também, demonstrando a normalizando de todas elas. As restrições de integridade, domínio e entidade devem ser documentadas e apresentadas nesta etapa. Também devem estar listadas quais são as possíveis consultas e quais deverão ser implementadas como stored-procedures. 

### Segunda etapa

O sistema final deverá estar implementado usando uma linguagem de programação e sgbd de sua preferência. Todas as funcionalidades básicas do sistema de compra, pesquisa, remoção e cadastro de filmes/ofertas deverão estar funcionando. Projetos sem a devida aplicação funcional serão rejeitados sumariamente. É verdade esse Bilete! 

### Requisitos

O Cinema Sauro funciona como 45 Salas Multiplex em um luxuoso Shopping Center de Sousa.

* Para cada sala do cinema existe um cronograma de filmes a serem exibidos na mesma, podendo um mesmo filme estar alocado em mais de uma sala, e podendo uma mesma sala
exibir mais de um filme, em horários diferentes.
* Existe um cadastro de próximas estreias, e um sistema de compra antecipada de ingresso para estes filmes. Obviamente que também o ingresso para o mesmo é dia é possível. Esta operação é realizada através de cartão de crédito, e é cobrada uma taxa extra de 10% em cima do valor da bilheteria.
* O valor do ingresso varia de acordo com o dia da semana, e com as seguintes categorias: adulto, estudante, infantil, idoso e flamenguista. Neste caso, o flamenguista possui entrada gratuita, o infantil paga apenas 25%, o adulto paga entrada inteira, os demais pagam meia entrada.
* Uma pessoa pode comprar mais de um ingresso. E o este conjunto de ingressos podem ser para filmes, salas e horários distintos.
* A cada sala possui sua capacidade e a venda de ingressos deve estar limitada a isso.
* Os filmes dispõem de informações sobre os atores principais, a censura, categoria (comédia, romance, ficção, ação, suspense...), sua censura e sua duração, a Empresa Produtora e se é Nacional ou não.
* O sistema tb deve dar suporte no que tange a compra de itens na lanchonete do cinema.
* Durante o processo de compra de ingresso, devem ser listadas as ofertas da lanchonete do dia. O comprador poderá incluir um ou mais ofertas a sua compra.
* Para cada ingresso ou oferta comprada, devem ser impressos vouchers ao final da compra. 

#### Observações
1. Durante a apresentação do projeto, o sistema deve estar devidamente alimentado com dados para permitir seu teste. 
2. O sistema deve possuir interface gráfica. Podendo ser uma inteface Web, desktop ou console. 
3. Para a segunda etapa, deve ser apresentado em um documento a parte o projeto físico do banco com todas as suas consultas DDL, DML e DQL.



## Construção do Projeto

## Modelagem Conceitual E-R

![Modelo E-R](https://i.imgur.com/OIlo8xX.jpg)

Link para total visualização: [Modelagem conceitual](https://i.imgur.com/OIlo8xX.jpg)

    A tabela filme é onde está armazenada as informações de filmes, foi normalizada usando a primeira regra normal em gênero por seus dados serem multi-valorados, tendo relacionamento N,N, pois um filme pode ser comedia e ação, por exemplo.

    O mesmo para a tabela sessão, onde sala e hora possuem cardinalidade 0,1 e sessão possui cardinalidade 1,1 em ambas, pois sessão pode ter apenas 1 sala ou 1 hora, está tabela é onde está armazenada informações das sessões disponíveis em exibição.

    Ingresso possui normalização de sua tabela desconto por ser multi-valorada e é a tabela de maior movimentação no banco de dados.

    Produto é a tabela da lanchonete, onde se encontra todos os dados de produtos referente a consumo no cinema e suas ofertas

    Cliente possui os dados cadastrais e é dela que é retida informações para uma venda.

    Venda é a tabela que constitui todos os dados de vendas de produtos e ingressos, possui relacionamento N,N com ambas já que um produto ou ingresso pode está em várias vendas, e vendas pode ter vários ingressos e produtos.

## Modelagem Lógica

<img src="https://i.imgur.com/yFWCJhX.jpg" title="" alt="Modelagem" data-align="center">

Link para total visualização: [Modelagem Lógica](https://i.imgur.com/yFWCJhX.jpg)



## Views

![View](https://i.imgur.com/bFkYmsy.png)

Criação de views para consultas mais utilizadas no banco de dados do cinema, com estes select trazem informações para serem expostas no front end e back end do cinema.

## Modelagem Física para criação do banco de dados em Postgresql



CREATE TABLE Filme
(
  idFilme SERIAL PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  classificacao INT,
  anoProducao INT,
  sinopse TEXT,
  nacionalidade VARCHAR(11),  
  produtora VARCHAR(50),
  duracao INT,
  img TEXT,
  diretor TEXT,
  atores TEXT
);

CREATE TABLE Sessao 
(
  idSessao SERIAL PRIMARY KEY,
  experiencia VARCHAR(8), 
  formato VARCHAR(2),
  idioma VARCHAR(9),
  dia DATE,
  valor FLOAT, 
  disponibilidade INT,
  fkSala INT,
  fkHora INT,
  fkFilme INT
);

CREATE TABLE Sala 
(
  idSala SERIAL PRIMARY KEY,
  numero INT UNIQUE NOT NULL,
  capacidade INT NOT NULL
);

CREATE TABLE Hora 
(
  idHorario SERIAL PRIMARY KEY,
  horario TIME UNIQUE NOT NULL
);

CREATE TABLE Ingresso
(
  idIngresso SERIAL PRIMARY KEY,
  preco FLOAT,
  fkCategoria INT,
  fkSessao INT
);

CREATE TABLE Categoria_Ingresso
(
  idCategoria SERIAL PRIMARY KEY,
  nome VARCHAR(50) UNIQUE,
  desconto FLOAT
);

CREATE TABLE Filme_Genero
(
  idFilme INT,
  idGenero INT
);

CREATE TABLE Genero
(
  idGenero SERIAL PRIMARY KEY,
  genero VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE Cliente
(
  idCliente SERIAL PRIMARY KEY,
  nome VARCHAR(50),
  cpf VARCHAR(20),
  telefone TELEFONE(20)
);

CREATE TABLE Venda
(
  idVenda SERIAL PRIMARY KEY,
  fkCliente INT,
  tipoPagamento VARCHAR(15),
  estado VARCHAR(20),
  total FLOAT,
  data_venda DATE
);

CREATE TABLE Produto
(
  idProduto SERIAL PRIMARY KEY,
  nome VARCHAR(50),
  preco FLOAT,
  categoria VARCHAR(15),
  quantidade INT,
  fkOferta INT
);

CREATE TABLE Oferta
(
  idOferta SERIAL PRIMARY KEY,
  nome VARCHAR(50),
  desconto FLOAT,
  inicio DATE,
  fim DATE
);

CREATE TABLE Venda_Produto
(
  idVenda INT,
  idProduto INT,
  quantidadevendida INT,
  valortotal FLOAT,
  PRIMARY KEY(idVenda, idProduto)
);

CREATE TABLE Venda_Ingresso
(
  idVenda INT,
  idIngresso INT,
  PRIMARY KEY (idVenda, idIngresso)
);



ALTER TABLE "Filme_Genero" ADD CONSTRAINT idFilme FOREIGN KEY(idFilme) REFERENCES "Filme" (idFilme) ON DELETE CASCADE ON UPDATE CASCADE;



ALTER TABLE "Filme_Genero" ADD CONSTRAINT idGenero FOREIGN KEY (idGenero) REFERENCES "Genero" (idGenero) ON DELETE CASCADE ON UPDATE CASCADE;



ALTER TABLE "Ingresso" ADD CONSTRAINT fkCategoria FOREIGN KEY (fkCategoria) REFERENCES "Categoria_Ingresso" (idCategoria) ON DELETE CASCADE ON UPDATE CASCADE;



ALTER TABLE "Ingresso" ADD CONSTRAINT fkSessao FOREIGN KEY (fkSessao) REFERENCES "Sessao" (idSessao) ON DELETE CASCADE ON UPDATE CASCADE;



ALTER TABLE "Sessao" ADD CONSTRAINT fkSala FOREIGN KEY (fkSala) REFERENCES "Sala" (idSala) ON DELETE CASCADE ON UPDATE CASCADE;



ALTER TABLE "Sessao" ADD CONSTRAINT fkHora FOREIGN KEY (fkHora) REFERENCES "Hora" (idHorario) ON DELETE CASCADE ON UPDATE CASCADE;



ALTER TABLE "Sessao" ADD CONSTRAINT fkFilme FOREIGN KEY (fkFilme) REFERENCES "Filme" (idFilme) ON DELETE CASCADE ON UPDATE CASCADE;



ALTER TABLE "Venda" ADD CONSTRAINT fkCliente FOREIGN KEY (fkCliente) REFERENCES "Cliente" (idCliente) ON DELETE CASCADE ON UPDATE CASCADE;



ALTER TABLE "Produto" ADD CONSTRAINT fkOferta FOREIGN KEY (fkOferta) REFERENCES "Oferta" (idOferta) ON DELETE CASCADE ON UPDATE CASCADE;



ALTER TABLE "Venda_Produto" ADD CONSTRAINT idVenda FOREIGN KEY (idVenda) REFERENCES "Venda" (idVenda) ON DELETE CASCADE ON UPDATE CASCADE;



ALTER TABLE "Venda_Produto" ADD CONSTRAINT idProduto FOREIGN KEY (idProduto) REFERENCES "Produto" (idProduto) ON DELETE CASCADE ON UPDATE CASCADE;



ALTER TABLE "Venda_Ingresso" ADD CONSTRAINT idVenda FOREIGN KEY (idVenda) REFERENCES "Venda" (idVenda) ON DELETE CASCADE ON UPDATE CASCADE;



ALTER TABLE "Venda_Ingresso" ADD CONSTRAINT idIngresso FOREIGN KEY (idIngresso) REFERENCES "Ingresso" (idIngresso) ON DELETE CASCADE ON UPDATE CASCADE;



## Criação de Views


View para ver dados de sessão junto a filme:

CREATE OR REPLACE VIEW versessao AS
    SELECT SE."idSessao", FI."idFilme",
    FI.nome AS Nome,
    SA.numero AS Numero_Da_Sala, 
    SE.experiencia AS Experiencia, SE.formato AS Formato, SE.idioma AS Idioma, SE.dia AS Dia, SE.disponibilidade AS Disponibilidade, SE.valor AS Preco,
    H.horario AS Horario
    FROM "Sessao" SE
    JOIN "Hora" H 
        ON SE."fkHora" = H."idHorario"
    JOIN "Sala" SA 
        ON SE."fkSala" = SA."idSala"
    JOIN "Filme" FI 
        ON SE."fkFilme" = FI."idFilme"
    ORDER BY SE."idSessao";


View para ver as principais colunas de filme:

CREATE OR REPLACE VIEW verfilme AS
    SELECT FI."idFilme", FI.nome, FI."anoProducao", FI.img
    FROM "Filme" FI
    ORDER BY "idFilme";


View com informações completas de uma venda e os dados do cliente comprador:

CREATE OR REPLACE VIEW venda_cliente
AS SELECT v."idVenda",
    v."fkCliente",
    v."tipoPagamento",
    v.estado,
    v.total,
    v.data_venda,
    c."idCliente",
    c.nome,
    c.cpf,
    c.telefone
   FROM "Venda" v
     LEFT JOIN "Cliente" c ON v."fkCliente" = c."idCliente";


View para mostrar os N gêneros do filme:

CREATE OR REPLACE VIEW genero_filme
AS SELECT fg."idFilme",
    g.genero
   FROM "Filme_Genero" fg
     JOIN "Genero" g ON fg."idGenero" = g."idGenero";


View para produtos que ainda estão em comercialização:

CREATE OR REPLACE VIEW ver_produtos
AS SELECT p."idProduto",
    p.nome,
    p.preco,
    p.categoria,
    p."fkOferta",
    p.quantidade
   FROM "Produto" p
  WHERE p.quantidade > 0;


View para hora do filme:

CREATE OR REPLACE VIEW ver_hora
AS SELECT "Hora"."idHorario",
    "Hora".horario
   FROM "Hora";


View para informações da sala:

CREATE OR REPLACE VIEW ver_sala
AS SELECT "Sala"."idSala",
    "Sala".numero,
    "Sala".capacidade
   FROM "Sala";



## Exemplos de inserts



INSERT INTO "Sala" (numero, capacidade)
VALUES (12, 12);



INSERT INTO "Hora" (horario)
VALUES ('16:00');



INSERT INTO "Sessao" (experiencia, formato, idioma, "fkSala", "fkFilme", "fkHora", dia, valor, disponibilidade)
VALUES ('VIP', '3D', 'LEGENDADO', 3, 3, 1, '2022-12-13', 40, 30);



INSERT INTO "Filme" (nome, classificacao, duracao, "anoProducao", sinopse, nacionalidade, produtora, img, diretor, atores)
VALUES ('Avatar: O Caminho da Água', 0, 300, 2022, 'Após formar uma família, Jake Sully e Neytiri fazem de tudo para ficarem juntos. No entanto, eles devem sair de casa e explorar as regiões de Pandora quando uma antiga ameaça ressurge, e Jake deve travar uma guerra difícil contra os humanos.', 'Estrangeiro', 'Century Studios', 'https://www.claquete.com.br/fotos/filmes/poster/11971_medio.jpg', 'James Cameron', 'Zoe Saldana, Kate Winslet, Sigourney Weaver, David Thewlis, Giovanni Ribisi');



INSERT INTO "Genero" (genero)
VALUES ('Ficção cientifica');



INSERT INTO "Filme_Genero" 
VALUES (18, 7);



INSERT INTO "Ingresso" (preco, "fkCategoria", "fkSessao")
VALUES (3, 5, 7);



INSERT INTO "Categoria_Ingresso" (nome, desconto)
VALUES ('FLAMENGUISTA', 1);



INSERT INTO "Cliente" (nome, cpf, telefone)
VALUES ('Lucas', '993293921', '(83) 999319239');



INSERT INTO "Venda" ("fkCliente", "tipoPagamento", estado, total, data_venda)
VALUES (8, 'Credito', 'Aguardando', 34, '2022-12-06');



INSERT INTO "Venda_Ingresso"
VALUES (3, 3);



INSERT INTO "Oferta" (nome, desconto, inicio, fim)
VALUES ('refrigerante', 10, '2022-12-06', '2022-12-10');



INSERT "Produto" (nome, preco, categoria, "fkOferta", quantidade)
VALUES ('Chocolate', 8, 'Comida', 2, 30);



INSERT INTO "Venda_Produto" ("idVenda", idproduto, quantidadevendida, valortotal)
VALUES (1, 7, 2, 16);
