from app import app, db
from models2 import Filme, Sessao
from flask import render_template

@app.route("/")
def index():
     lista = Filme.query.order_by(Filme.idFilme)
     return render_template('index.html', filmes=lista)

@app.route("/sessoes/<int:idFilme>")
def sessoes(idFilme):
     sessao_filme = Sessao.query.filter_by(fkFilme=idFilme)
     filme = Filme.query.filter_by(idFilme=idFilme).first()
     return render_template('sessoes.html', sessao_filme=sessao_filme, filme=filme)