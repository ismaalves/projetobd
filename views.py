from app import app, db
from models2 import Filme, Sessao, Hora, Categoria_Ingresso
from flask import render_template, redirect, request, url_for
from helpers import FormIngresso

@app.route("/")
def index():
     q = f'select * from verfilme'
     filmes = db.session.execute(q)

     return render_template('index.html', filmes=filmes)


@app.route("/sessoes/<int:idFilme>")
def sessoes(idFilme):
     filme = Filme.query.filter_by(idFilme=idFilme).first()

     q = f'select * from versessao \
          WHERE versessao."idFilme" = {idFilme}'

     sessoes = db.session.execute(q)
     return render_template('sessoes.html', sessao_filme=sessoes, filme=filme, Hora=Hora)


@app.route("/compraringresso/<int:idSessao>%<int:idFilme>")
def comprarIngresso(idSessao,idFilme):
     form = FormIngresso()
     
     sessao = Sessao.query.filter_by(idSessao=idSessao).first()
     filme = Filme.query.filter_by(idFilme=idFilme).first()
     tipo_ingresso = Categoria_Ingresso.query.order_by(Categoria_Ingresso.idCategoria)
     
     return render_template('ingresso.html', sessao=sessao, filme=filme, tipos=tipo_ingresso, form=form)


#ESTA É UMA URL INTERMEDIARIA
@app.route("/venda_ingresso", methods=['POST','GET'])
def venda_ingresso():
     form = FormIngresso(request.form)
     
     if not form.validate_on_submit():
          return redirect(url_for('index'))

     return "Sucess"