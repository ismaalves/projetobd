# Projeto de Banco de Dados
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
