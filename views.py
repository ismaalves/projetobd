from app import app, db
from models2 import Filme, Sessao, Hora, Categoria_Ingresso
from flask import render_template
from sqlalchemy import func

@app.route("/")
def index():
     filmes = Filme.query.order_by(Filme.idFilme)
     return render_template('index.html', filmes=filmes)

@app.route("/sessoes/<int:idFilme>")
def sessoes(idFilme):
     sessao_filme = Sessao.query.filter_by(fkFilme=idFilme)
     filme = Filme.query.filter_by(idFilme=idFilme).first()

     query =f'SELECT "Sessao"."idSessao", "Sessao".experiencia, \
          "Sessao".formato, "Sessao".idioma, "Sessao"."fkSala",\
          "Sessao"."fkFilme", "Sessao".dia, "Sessao".valor,\
          "Sessao".disponibilidade, "Hora".horario \
          FROM "Sessao" JOIN "Hora" ON "Sessao"."fkHora" = "Hora"."idHorario"\
          WHERE "Sessao"."fkFilme" = {idFilme}'

     sessoes = db.session.execute(query)
     return render_template('sessoes.html', sessao_filme=sessoes, filme=filme, Hora=Hora)

@app.route("/compraringresso/<int:idSessao>%<int:idFilme>")
def comprarIngresso(idSessao,idFilme):
     sessao = Sessao.query.filter_by(idSessao=idSessao).first()
     filme = Filme.query.filter_by(idFilme=idFilme).first()
     tipo_ingresso = Categoria_Ingresso.query.order_by(Categoria_Ingresso.idCategoria)
     
     return render_template('ingresso.html', sessao=sessao, filme=filme, tipos=tipo_ingresso)