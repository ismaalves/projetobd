from app import app, db
from models import Filme, Ator, Sala, Sessao, Carrinho, Cliente, filme_ator, filme_genero, Genero, Hora, Ingresso, Produto, Oferta, Categoria
from flask import render_template

@app.route("/")
def index():
     lista = Filme.query.order_by(Filme.pk_filme)
     return render_template('index.html', filmes=lista)