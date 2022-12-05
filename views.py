from app import app, db
from models2 import Filme, Sessao, Hora, Categoria_Ingresso, Produto, Venda, Oferta
from flask import render_template, redirect, request, url_for, flash
from helpers import FormIngresso, FormVenda
from funcs import verifica_ingressos, insert_ingresso, verifica_produtos, insert_produtos, total_venda, clientes
import datetime
from sqlalchemy import update, select


@app.route("/")
def index():
     q = f'select * from verfilme'
     filmes = db.session.execute(q)

     return render_template('index.html', filmes=filmes)



@app.route("/infofilme/<int:idFilme>")
def infofilme(idFilme):
     filme = Filme.query.filter_by(idFilme=idFilme).first()
     return render_template('infofilme.html', filme=filme)



@app.route("/sessoes/<int:idFilme>")
def sessoes(idFilme):
     filme = Filme.query.filter_by(idFilme=idFilme).first()
     dia = f"'{datetime.date.today()}'"
     q = f'select * from versessao \
          WHERE versessao."idFilme" = {idFilme} and versessao."dia" >= {dia} and versessao."disponibilidade" > 0'

     sessoes = db.session.execute(q)
     return render_template('sessoes.html', sessao_filme=sessoes, filme=filme, Hora=Hora)



@app.route("/compraringresso/<int:idSessao>&<int:idFilme>")
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
     
     if not verifica_ingressos(form.data, idSessao):
          return redirect(url_for('index'))
     else:
          id_venda = insert_ingresso(form.data, idSessao, preco_sessao)

     return redirect(url_for('comprar_produto', id_venda=id_venda))



@app.route("/comprar_produto/<int:id_venda>")
def comprar_produto(id_venda):
     produtos = Produto.query.order_by(Produto.idProduto)
     q = f'select * from ver_produtos'
     produtos = db.session.execute(q)

     return render_template('produto.html', produtos=produtos, id_venda=id_venda)



@app.route("/venda_produto/<int:id_venda>", methods=['POST','GET'])
def venda_produto(id_venda):
     form = request.form

     if verifica_produtos(form):
          insert_produtos(form, id_venda)
     else:
          redirect(url_for('comprar_produto', id_venda=id_venda))

     return redirect(url_for('finalizar_venda', id_venda=id_venda))


@app.route("/finalizar_venda/<int:id_venda>")
def finalizar_venda(id_venda):

     q1 = f'SELECT iv."idVenda", iv."idIngresso", iv.preco, iv."fkCategoria", v.nome, v.numero_da_sala, v.experiencia, v.formato, v.idioma, v.dia, v.horario FROM (SELECT vi."idVenda", i.* FROM "Venda_Ingresso" vi \
          INNER JOIN "Ingresso" i  ON vi."idIngresso"  = i."idIngresso" WHERE vi."idVenda" = {id_venda}) \
          AS iv INNER JOIN versessao v \
          ON iv."fkSessao" = v."idSessao"'
     
     q2 = f'SELECT * FROM (SELECT * FROM "Venda_Produto" vp \
          INNER JOIN "Produto" p ON vp."idproduto"  = p."idProduto" WHERE vp."idVenda" = {id_venda}) as produto_venda'

     venda_ingressos = db.session.execute(q1)
     venda_produtos = db.session.execute(q2)
     valor_total = total_venda(id_venda)

     venda = Venda.query.filter_by(idVenda=id_venda).first()

     form = FormVenda()

     form.idVenda.data = venda.idVenda
     form.estado.data = venda.estado
     form.total.data = valor_total
     form.data_venda.data = datetime.date.today()

     todos_clientes = clientes()
     form.fkCliente.choices = todos_clientes

     return render_template('venda.html', venda_ingressos=venda_ingressos, venda_produtos=venda_produtos, id_venda=id_venda, valor_total=valor_total, form=form)



@app.route("/cancelar_venda/<int:id_venda>", methods=['POST','GET'])
def cancelar_venda(id_venda):
     delete = f'delete from "Ingresso" where "idIngresso" in (select vi."idIngresso" from "Venda_Ingresso" vi where "idVenda" = {id_venda}); \
                 delete from "Venda" where "idVenda" = {id_venda};'
     
     db.session.execute(delete)
     db.session.commit()

     return redirect(url_for("index"))



@app.route("/finalizar/<int:id_venda>", methods=['POST','GET'])
def finalizar(id_venda):
     form = FormVenda(request.form)
     
     if (form.tipoPagamento.data =='Credito'):
          form.total.data = float(form.total.data) * 1.10
     
     if(form.fkCliente.data != '0'):
          form.fkCliente.data = form.fkCliente.data
     else:
          form.fkCliente.data = None

     update_venda = (
          update(Venda).
          where(Venda.idVenda == id_venda).
          values(
               fkCliente=form.fkCliente.data,
               tipoPagamento=form.tipoPagamento.data,
               estado=form.estado.data,
               total=form.total.data,
               data_venda=form.data_venda.data
          )
     )
     db.session.execute(update_venda)
     db.session.commit()

     return redirect(url_for('pagamento', id_venda=id_venda))



@app.route("/vouchers/<int:id_venda>", methods=['POST','GET'])
def vouchers(id_venda):
     venda = Venda.query.filter_by(idVenda=id_venda).first()
     flash("Venda Concluida")
     if (venda.fkCliente != None):
          q = f'select * from  "Cliente" c where "idCliente" = {venda.fkCliente} limit 1'
          result = db.session.execute(q)
          for i in result:
               cliente = i
          return render_template('final_venda.html',venda=venda, cliente=cliente)
     else:
          return render_template('final_venda.html',venda=venda)



@app.route("/pagamento/<int:id_venda>", methods=['POST', 'GET'])
def pagamento(id_venda):
     venda = Venda.query.filter_by(idVenda=id_venda).first()
     return render_template('pagamento.html', venda=venda)


@app.route("/processapagamento/<int:id_venda>")
def processapagamento(id_venda):
     update_venda = (
          update(Venda).
          where(Venda.idVenda == id_venda).
          values(estado="Pago")
     )
     db.session.execute(update_venda)
     db.session.commit()

     return redirect(url_for('vouchers', id_venda=id_venda))