from app import db
from models2 import Categoria_Ingresso, Ingresso, Venda, Venda_Produto, Produto, Cliente
from sqlalchemy.sql import select, insert


def cria_venda():
     venda = insert(Venda).values(estado='Aguardando').returning(Venda.idVenda)
     result = db.session.execute(venda)   
     id_venda = 0
     for i in result.first():
          id_venda = i
          print(type(i))
     db.session.commit()
     return id_venda


def verifica_ingressos(entrada, idSessao):
     disp = update_sessao(idSessao)
     print(disp)
     soma = 0
     for chave, valor in entrada.items():
          if type(valor) == type(1):
               soma = soma + valor

     if(soma > 0 and soma <= disp):
          print(disp)
          return True
     else:
          return False


def insert_ingresso(dados, idSessao, preco):
     new_dados = { key: dados[key] for key in dados if key != 'csrf_token' and key != 'comprar' and dados[key] != 0}
     ids_ing = []
     qtd, preco_total = 0,0

     id_venda = cria_venda()
     
     for c, v in new_dados.items():
          qtd = qtd+v
          for j in range(0, v):
               categoria = Categoria_Ingresso.query.filter_by(nome = c).first()
               preco_total += float(preco)*float(categoria.desconto)
               ingresso = insert(Ingresso).values(preco=(float(preco)*float(categoria.desconto)), fkCategoria=categoria.idCategoria, fkSessao=idSessao).returning(Ingresso.idIngresso)
               print(ingresso)
               result = db.session.execute(ingresso)
               
               for i in result:
                    ids_ing.append(int(i[0]))

     for i in ids_ing:
          new_ing_venda=f'INSERT INTO "Venda_Ingresso" ("idVenda", "idIngresso") VALUES ({id_venda}, {i})'
          db.session.execute(new_ing_venda) 

     db.session.commit()

     return id_venda


def verifica_produtos(form):
     soma = 0 
     for i,j in form.items():
          soma = soma + int(j)
     if soma > 0:
          return True
     else:
          return False


def insert_produtos(form, id_venda):
     new_dados = { int(key): int(value) for key, value in form.items() if value != '0'}
     for c, v in new_dados.items():
          produto = Produto.query.filter_by(idProduto = c).first()
          insert_prod = insert(Venda_Produto).values(idVenda=id_venda, idproduto=c, quantidadevendida=v, valortotal=(float(v)*float(produto.preco)))
          db.session.execute(insert_prod)
     
     db.session.commit()
     return True


def update_sessao(idSessao):
     q1 = f'SELECT COUNT (i."fkSessao") FROM "Ingresso" i where i."fkSessao" = {idSessao} GROUP BY	i."fkSessao";'
     
     q2 = f'select s.capacidade from "Sala" s inner join "Sessao" s2 on s2."fkSala" = s."idSala" where s2."idSessao" = {idSessao}'

     result1 = db.session.execute(q1)
     result2 = db.session.execute(q2)
     t1,t2=0,0
     
     for i in result1:
          t1 = i[0]

     for i in result2:
          t2 = i[0]
     
     return int(t2) - int(t1)


def total_venda(id_venda):

     q1 = f'SELECT sum(iv.preco) FROM \
     (SELECT vi."idVenda", i.* FROM "Venda_Ingresso" vi INNER JOIN "Ingresso" i  ON vi."idIngresso"  = i."idIngresso" WHERE vi."idVenda" = {id_venda}) \
     AS iv INNER JOIN versessao v \
     ON iv."fkSessao" = v."idSessao"'

     q2 = f'SELECT sum(produto_venda.valortotal) FROM (SELECT * FROM "Venda_Produto" vp \
     INNER JOIN "Produto" p ON vp."idproduto"  = p."idProduto" WHERE vp."idVenda" = {id_venda}) as produto_venda'


     result1 = db.session.execute(q1)
     result2 = db.session.execute(q2)
     t1, t2, total = 0, 0, 0
     
     for i in result1:
          t1 = i[0]

     for i in result2:
          t2 = i[0]
     
     if(t1 and t2):
          total = float(t2) + float(t1)
     elif (t1):
          total = float(t1)

     return total


def clientes():
     q = f'select * from "Cliente" c order by c.nome '
     result = db.session.execute(q)
     r_clientes = [(c.idCliente, c.nome) for c in result]
     
     return r_clientes