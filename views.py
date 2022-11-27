from app import app, db
from models2 import Filme, filme_elenco
from flask import render_template

@app.route("/")
def index():
     lista = Filme.query.order_by(Filme.idFilme)
     lista2 = filme_elenco.query.order_by(filme_elenco.idFilme)
     for i in lista2:
          print(i)

     return render_template('index.html', filmes=lista, elenco=lista2)