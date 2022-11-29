from app import db


class filme_elenco(db.Model):
    __tablename__ = "filme_elenco"

    __table_args__ = (
        db.PrimaryKeyConstraint("idFilme", "idElenco"),
    )

    idFilme = db.Column(db.Integer, db.ForeignKey("Filme.idFilme"))
    idElenco = db.Column(db.Integer, db.ForeignKey("Elenco.idElenco"))

    def __repr__(self):
        return f"{filme_elenco.idFilme}-{filme_elenco.idElenco}"


class filme_genero(db.Model):
    __tablename__ = "filme_genero"

    __table_args__ = (
        db.PrimaryKeyConstraint('idFilme', 'idGenero'),
    )

    idFilme = db.Column(db.Integer, db.ForeignKey("Filme.idFilme"))
    idGenero = db.Column(db.Integer, db.ForeignKey("Genero.idGenero"))

    def __repr__(self):
        return f"{filme_genero.idFilme}-{filme_genero.idGenero}"


class Filme(db.Model):
    __tablename__ = "Filme"

    idFilme = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    classificacao = db.Column(db.Integer, nullable=False)
    duracao = db.Column(db.Integer, nullable=False)
    anoProducao = db.Column(db.Integer, nullable=False)
    sinopse = db.Column(db.Text, nullable=False)
    nacionalidade = db.Column(db.String(11), nullable=False)
    produtora = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"{Filme.id}-{Filme.nome}"

class Elenco(db.Model):
    __tablename__ = "Elenco"

    idElenco = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    fkCategoria = db.Column(db.Integer, db.ForeignKey("categoria_elenco.idCategoriaElenco"))
    
    def __repr__(self):
        return f"{Elenco.idElenco}-{Elenco.nome}-{Elenco.fkCategoria}"


class Genero(db.Model):
    __tablename__ = "Genero"

    idGenero = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genero = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return f"{Genero.idGenero}-{Genero.genero}"


class Sala(db.Model):
    __tablename__ = "Sala"

    idSala = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero = db.Column(db.Integer, nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"{Sala.idSala}-{Sala.numero}"


class Hora(db.Model):
    __tablename__ = "hora"

    idHorario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    horario = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"{Hora.idHorario}-{Hora.horario}"


class Sessao(db.Model):
    __tablename__ = "Sessao"

    idSessao = db.Column(db.Integer, primary_key=True, autoincrement=True)
    experiencia = db.Column(db.String(8), nullable=False)
    formato = db.Column(db.String(2), nullable=False)
    idioma = db.Column(db.String(9), nullable=False)
    fkSala = db.Column(db.Integer, db.ForeignKey("Sala.idSala"))
    fkFilme = db.Column(db.Integer, db.ForeignKey("Filme.idFilme"))
    fkHora = db.Column(db.Integer, db.ForeignKey("hora.idHorario"))
    dia = db.Column(db.Date, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    disponibilidade = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"{Sessao.idSessao}"


class Ingresso(db.Model):
    __tablename__ = "Ingresso"

    idIngresso = db.Column(db.Integer, primary_key=True, autoincrement=True)
    preco = db.Column(db.Float, nullable=False)
    fkCategoria = db.Column(db.Integer, db.ForeignKey("Categoria.idCategoria"))
    fkSessao = db.Column(db.Integer, db.ForeignKey("Sessao.idSessao"))

    def __repr__(self):
        return f"{Ingresso.idIngresso}-{Ingresso.preco}"


class Venda_Ingresso(db.Model):
    __tablename__ = "Venda_Ingresso"

    __table_args__ = (
        db.PrimaryKeyConstraint("idVenda", "idIngresso"),
    )

    idVenda = db.Column(db.Integer, db.ForeignKey("Venda.idVenda"))
    idIngresso = db.Column(db.Integer, db.ForeignKey("Ingresso.idIngresso"))
    quantidadecendida = db.Column(db.Integer, nullable=True)
    preco = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"{Venda_Ingresso.idVenda}-{Venda_Ingresso.idIngresso}"


class Venda(db.Model):
    __tablename__ = "Venda"

    idVenda = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fkCliente = db.Column(db.Integer, db.ForeignKey("Cliente.idCliente"))
    tipo_pagamento = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"{Venda.idVenda}-{Venda.fkCliente}"


class Venda_Produto(db.Model):
    __tablename__ = "Venda_Produto"
    
    __table_args__ = (
        db.PrimaryKeyConstraint("idVenda", "idproduto"),
    )

    idVenda = db.Column(db.Integer, db.ForeignKey("Venda.idVenda"))
    idproduto = db.Column(db.Integer, db.ForeignKey("Produto.idproduto"))
    quantidadecendida = db.Column(db.Integer, nullable=True)
    preco = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"{Venda_Produto.idVenda}-{Venda_Produto.idproduto}"


class Produto(db.Model):
    __tablename__ = "Produto"

    idProduto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    categoria = db.Column(db.String(15), nullable=False)
    fkOferta = db.Column(db.Integer, db.ForeignKey("Oferta.idOferta") ,nullable=True)
    quantidade = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{Produto.idProduto}-{Produto.nome}'


class Oferta(db.Model):
    __tablename__ = "Oferta"

    idOferta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    desconto = db.Column(db.Float, nullable=False)
    inicio = db.Column(db.Date, nullable=False)
    fim = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'{Oferta.idOferta}-{Oferta.nome}'


class Categoria_Ingresso(db.Model):
    __tablename__ = "Categoria_Ingresso"

    idCategoria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    desconto = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'{Categoria_Ingresso.idCategoria}-{Categoria_Ingresso.nome}'


class categoria_elenco(db.Model):
    __tablename__ = "categoria_elenco"

    idCategoriaElenco = db.Column(db.Integer, primary_key=True, autoincrement=True)
    categoria = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"{categoria_elenco.idCategoriaElenco}-{categoria_elenco.categoria}"


class Cliente(db.Model):
    __tablename___ = "Cliente"

    idCliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(20), nullable=True) #Deveria ser String
    telefone = db.Column(db.String(20), nullable=True) #Deveria ser String

    def __repr__(self):
        return f'{Cliente.idCliente}-{Cliente.nome}'