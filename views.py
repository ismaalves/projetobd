from app import app, db
from models2 import Filme, Sessao, Hora
from flask import render_template
from sqlalchemy import func

@app.route("/")
def index():
     lista = Filme.query.order_by(Filme.idFilme)
     return render_template('index.html', filmes=lista)

@app.route("/sessoes/<int:idFilme>")
def sessoes(idFilme):
     sessao_filme = Sessao.query.filter_by(fkFilme=idFilme)
     filme = Filme.query.filter_by(idFilme=idFilme).first()

     query =f'SELECT "Sessao"."idSessao", "Sessao".experiencia, \
          "Sessao".formato, "Sessao".idioma, "Sessao"."fkSala",\
          "Sessao"."fkFilme", "Sessao".dia, "Sessao".valor,\
          "Sessao".disponibilidade, "hora".horario \
          FROM "Sessao" JOIN hora ON "Sessao"."fkHora" = hora."idHorario"\
          WHERE "Sessao"."fkFilme" = {idFilme}'

     sessoes = db.session.execute(query)
     return render_template('sessoes.html', sessao_filme=sessoes, filme=filme, Hora=Hora)

@app.route("/compraringresso/<int:idSessao>%<int:idFilme>")
def comprarIngresso(idSessao,idFilme):
     sessao = Sessao.query.filter_by(idSessao=idSessao).first()
     filme = Filme.query.filter_by(idFilme=idFilme).first()

     return render_template('ingresso.html', sessao=sessao, filme=filme)