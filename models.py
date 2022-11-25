from app import db

filme_ator = db.Table(
    "filme_ator",
    db.Base.metadata,
    db.Column("id_filme", db.ForeignKey("Filmes.id"), primary_key=True),
    db.Column("id_ator", db.ForeignKey("Atores.id"), primary_key=True),
)


filme_genero = db.Table(
    "filme_genero",
    db.Base.metadata,
    db.Column("id_filme", db.ForeignKey("Filmes.id"), primary_key=True),
    db.Column("id_genero", db.ForeignKey("Generos.id"), primary_key=True),
)


class Filme(db.Model):
    __tablename__ = "Filmes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    diretor = db.Column(db.String(50), nullable=False)
    classificacao = db.Column(db.Interger, nullable=False)
    duracao = db.Column(db.Interger, nullable=False)
    ano_prod = db.Column(db.Interger, nullable=False)
    sinopse = db.Column(db.Text, nullable=False)
    nacionalidade = db.Column(db.String(11), nullable=False)
    produtora = db.Column(db.String(50), nullable=False)
    ator = db.relashionship("Ator", secondary=filme_ator)
    genero = db.relashionship("Genero", secondary=filme_genero)
    sessao = db.relationship("Sessao")

    def __repr__(self):
        return '<Nome %r>' % self.nome


class Ator(db.Model):
    __tablename__ = "Atores"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return '<Nome %r>' % self.nome


class Genero(db.Model):
    __tablename__ = "Generos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genero = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return '<Genero %r >' % self.genero


class Sala(db.Model):
    __tablename__ = "Sala"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    num_sala = db.Column(db.Integer, nullable=False)
    cap_sala = db.Column(db.Integer, nullable=False)
    sessao = db.relationship("Sessao")

    def __repr__(self):
        return '<Sala %r>' % self.num_sala


class Hora(db.Model):
    __tablename__ = "Hora"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hora = db.Column(db.DateTime, nullable=False)
    sessao = db.relationship("Sessao")

    def __repr__(self):
        return '<Hora %r>' % self.num_sala


class Sessao(db.Model):
    __tablename__ = "Sessoes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    experiencia = db.Column(db.String(8), nullable=False)
    formato = db.Column(db.String(2), nullable=False)
    idioma = db.Column(db.String(9), nullable=False)
    fk_filmes = db.Column(db.Integer, db.ForeignKey("Filmes.id"))
    fk_hora = db.Column(db.Integer, db.ForeignKey("Hora.id"))
    fk_sala = db.Column(db.Integer, db.ForeignKey("Sala.id"))

    def __repr__(self):
        return f"Sessão: {self.id}"


class Ingresso(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    preco = db.Column(db.Float, nullable=False)
    categoria = db.Column(db.Integer, nullable=False)
    sessao = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Ingresso %r>' % self.id


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.Integer, nullable=True) #Deveria ser String
    telefone = db.Column(db.Integer, nullable=True) #Deveria ser String
    carrinho = db.Column(db.Integer, unique=True)

    def __repr__(self):
        return '<Cliente %r>' % self.nome


class Carrinho(db.model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ingresso = db.Column(db.String(50), nullable=True)
    produto = db.Column(db.Integer, nullable=True) #Deveria ser String
    cliente = db.Column(db.Integer, nullable=False) #Deveria ser String
    tipo_pg = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.Bool, nullable=False)

    def __repr__(self):
        return '<Carrinho %r>' % self.id


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    categoria = db.Column(db.Integer, nullable=False)
    oferta = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Produto %r>' % self.nome


class Oferta(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.Float, nullable=False)
    inicio = db.Column(db.Date, nullable=False)
    fim = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Oferta %r>' % self.nome


class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Categoria %r>' % self.nome
