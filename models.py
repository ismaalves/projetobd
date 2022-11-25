from app import db

'''
filme_ator = db.Table(
    "filme_ator",
    db.Base.metadata,
    db.Column("pk_filme", db.ForeignKey("Filme.pk_filme"), primary_key=True),
    db.Column("pk_ator", db.ForeignKey("Atore.pk_ator"), primary_key=True),
)


filme_genero = db.Table(
    "filme_genero",
    db.Base.metadata,
    db.Column("pk_filme", db.ForeignKey("Filme.pk_filme"), primary_key=True),
    db.Column("pk_genero", db.ForeignKey("Genero.pk_genero"), primary_key=True),
)'''


class Filme(db.Model):
    __tablename__ = "Filme"

    pk_filme = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    diretor = db.Column(db.String(50), nullable=False)
    classificacao = db.Column(db.Integer, nullable=False)
    duracao = db.Column(db.Integer, nullable=False)
    ano_producao = db.Column(db.Integer, nullable=False)
    sinopse = db.Column(db.Text, nullable=False)
    nacionalidade = db.Column(db.String(11), nullable=False)
    produtora = db.Column(db.String(50), nullable=False)
    #ator = db.relashionship("Ator", secondary=filme_ator)
    #genero = db.relashionship("Genero", secondary=filme_genero)
    #sessao = db.relationship("Sessao")

    def __repr__(self):
        return '<Nome %r>' % self.nome

'''
class Ator(db.Model):
    __tablename__ = "Ator"
    pk_ator = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ator = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return '<Ator %r>' % self.ator


class Genero(db.Model):
    __tablename__ = "Genero"
    pk_genero = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genero = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return '<Genero %r >' % self.genero


class Sala(db.Model):
    __tablename__ = "Sala"

    pk_sala = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero = db.Column(db.Integer, nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)
    sessao = db.relationship("Sessao")

    def __repr__(self):
        return '<Sala %r>' % self.numero


class Hora(db.Model):
    __tablename__ = "hora"

    pk_horario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    horario = db.Column(db.DateTime, nullable=False)
    sessao = db.relationship("Sessao")

    def __repr__(self):
        return '<Hora %r>' % self.horario


class Sessao(db.Model):
    __tablename__ = "Sessao"

    pk_sessao = db.Column(db.Integer, primary_key=True, autoincrement=True)
    experiencia = db.Column(db.String(8), nullable=False)
    formato = db.Column(db.String(2), nullable=False)
    idioma = db.Column(db.String(9), nullable=False)
    fk_sala = db.Column(db.Integer, db.ForeignKey("Sala.pk_sala"))
    fk_filmes = db.Column(db.Integer, db.ForeignKey("Filme.pk_filme"))
    fk_hora = db.Column(db.Integer, db.ForeignKey("hora.pk_horario"))
    ingresso = db.relationship("Ingresso")

    def __repr__(self):
        return '<Sessao %r>' % self.pk_sessao


class Ingresso(db.Model):
    __tablename__ = "Ingresso"

    pk_ingresso = db.Column(db.Integer, primary_key=True, autoincrement=True)
    preco = db.Column(db.Float, nullable=False)
    fk_categoria = db.Column(db.Integer, db.ForeignKey("Categoria.pk_categoria"))
    fk_sessao = db.Column(db.Interger, db.ForeignKey("Sessoes.pk_sessao"))
    carrinho = db.relationship("Carrinho")
    #QUANTIDADE

    def __repr__(self):
        return '<Ingresso %r>' % self.id


class Cliente(db.Model):
    __tablename___ = "Cliente"

    pk_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.Integer, nullable=True) #Deveria ser String
    telefone = db.Column(db.Integer, nullable=True) #Deveria ser String
    fk_carrinho = db.Column(db.Interger, db.ForeignKey("Carrinho.pk_carrinho"))
    carrinho = db.relationship("Carrinho", back_populates="Cliente")

    def __repr__(self):
        return '<Cliente %r>' % self.nome


class Carrinho(db.model):
    __tablename__ = "Carrinho"

    pk_carrinho = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fk_ingresso = db.Column(db.Interger, db.ForeignKey("Ingresso.id"))
    fk_cliente = db.Column(db.Interger, db.ForeignKey("Cliente.id"))
    fk_produto = db.Column(db.Interger, db.ForeignKey("Produto.id"))
    tipo_pagamento = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.Bool, nullable=False)
    cliente = db.relationship("Cliente", back_populates="Cliente")

    def __repr__(self):
        return '<Carrinho %r>' % self.pk_carrinho


class Produto(db.Model):
    __tablename__ = "Produto"

    pk_produto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    fk_oferta = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Produto %r>' % self.nome


class Oferta(db.Model):
    __tablename__ = "Oferta"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    desconto = db.Column(db.Float, nullable=False)
    inicio = db.Column(db.Date, nullable=False)
    fim = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Oferta %r>' % self.nome


class Categoria(db.Model):
    __tablename__ = "Categoria"

    pk_categoria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    ingresso = db.relationship("Ingresso")

    def __repr__(self):
        return '<Categoria %r>' % self.nome
'''