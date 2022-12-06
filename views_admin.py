from app import app, db
from models2 import Filme, Sessao, Filme_Genero
from flask import render_template, redirect, request, url_for
from helpers import cadastrofilmeForm, cadastrosessaoForm
from views import index
import datetime

from sqlalchemy import insert, delete


@app.route("/admin/cadastrofilmes")
def cadastroFilmes():
     
     form = cadastrofilmeForm()
     
     return render_template('cadastro_filmes.html', form=form)


@app.route("/admin/processacadastro", methods=['POST'])
def processaCadastro():

    form = cadastrofilmeForm(request.form)

    filme = insert(Filme).values(nome=form.nome.data, classificacao=form.classificacao.data, duracao=form.duracao.data, anoProducao=form.ano.data, sinopse=form.sinopse.data, 
    nacionalidade=form.nacionalidade.data, produtora=form.produtor.data, img=form.img.data, diretor=form.diretor.data, atores=form.atores.data).returning(Filme.idFilme)
    
    id_filme_tuple = db.session.execute(filme)
    db.session.commit()

    id_filme = 0
     
    for i in id_filme_tuple:
     id_filme = int(i[0])



    genero = (insert(Filme_Genero).values(idFilme=id_filme, idGenero=form.genero.data))

    db.session.execute(genero)
    db.session.commit()

    return redirect(url_for('index'))

@app.route("/admin/cadastrosessoes")
def cadastroSessoes():

     f = f'select * from verfilme'
     filmes = db.session.execute(f)

     s = f'select * from ver_sala order by numero'
     salas = db.session.execute(s)

     h = f'select * from ver_hora'
     horarios = db.session.execute(h)
     
     form = cadastrosessaoForm()

     form.salas.choices = [(c.idSala, c.numero) for c in salas]
     form.horarios.choices = [(c.idHorario, c.horario) for c in horarios]
     form.filmes.choices = [(c.idFilme, c.nome) for c in filmes]

     
     return render_template('cadastro_sessoes.html', form=form)

@app.route("/admin/processacadastrosessoes", methods=['POST'])
def processaCadastroSessoes():

     form = cadastrosessaoForm(request.form)

     sessao = insert(Sessao).values(
          experiencia=form.experiencia.data,
          formato=form.formato.data,
          idioma=form.idioma.data,
          fkSala=form.salas.data,
          fkFilme=form.filmes.data,
          fkHora=form.horarios.data,
          dia=form.dia.data,
          valor=form.valor.data,
          disponibilidade=form.disponibilidade.data)

     db.session.execute(sessao)
     db.session.commit()

     return redirect(url_for('index'))

@app.route("/admin/deletafilmes")
def deletaFilmes():
     
     f = f'select * from verfilme'
     filmes = db.session.execute(f)

     form=cadastrosessaoForm()

     form.filmes.choices = [(c.idFilme, c.nome) for c in filmes]

     return render_template('deleta_filmes.html', form=form)

@app.route("/admin/processadeletafilmes", methods=['POST'])
def processadeletaFilmes():
     
     form = cadastrosessaoForm(request.form)

     deleta = delete(Filme).where(Filme.idFilme == form.filmes.data)

     db.session.execute(deleta)
     db.session.commit()

     return redirect(url_for('index'))

