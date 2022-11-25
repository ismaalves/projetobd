from app import app, db
from models import Filme
from flask import render_template

@app.route("/")
def index():
     lista = Filme.query.order_by(Filme.pk_filme)
     return render_template('index.html', filmes=lista)