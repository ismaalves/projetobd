from app import app, db
from models2 import Filme, Sessao, Hora, Categoria_Ingresso, Produto
from flask import render_template, redirect, request, url_for
from helpers import FormIngresso
from funcs import verifica_ingressos, insert_ingresso, verifica_produtos, insert_produtos
import requests

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


#ESTA e UMA URL INTERMEDIARIA
@app.route("/venda_ingresso/<int:idSessao>", methods=['POST','GET'])
def venda_ingresso(idSessao):

     form = FormIngresso(request.form)
     preco = Sessao.query.filter_by(idSessao=idSessao)
     preco_sessao = 0

     for i in preco:
          if(i.idSessao == idSessao):
               preco_sessao = float(i.valor)
     
     if not verifica_ingressos(form.data):
          return redirect(url_for('index'))
     else:
          id_venda = insert_ingresso(form.data, idSessao, preco_sessao)

     return redirect(url_for('comprar_produto', id_venda=id_venda))


@app.route("/comprar_produto/<int:id_venda>")
def comprar_produto(id_venda):
     produtos = Produto.query.order_by(Produto.idProduto)
     return render_template('produto.html', produtos=produtos, id_venda=id_venda)


@app.route("/venda_produto/<int:id_venda>", methods=['POST','GET'])
def venda_produto(id_venda):
     form = request.form

     if verifica_produtos(form):
          insert_produtos(form,id_venda)
     else:
          redirect(url_for('comprar_produto', id_venda=id_venda))

     return redirect(url_for('finalizar_venda', id_venda=id_venda))


@app.route("/finalizar_venda/<int:id_venda>")
def finalizar_venda(id_venda):
     return f"<h1>Cheguei ate aqui{id_venda}</h1>"