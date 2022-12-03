from app import db
from models2 import Categoria_Ingresso, Ingresso, Venda, Venda_Produto, Produto
from sqlalchemy.sql import select,insert



def cria_venda():
     venda = insert(Venda).values(estado='Aguardando').returning(Venda.idVenda)
     result = db.session.execute(venda)   
     id_venda = 0
     for i in result.first():
          id_venda = i
          print(type(i))
     db.session.commit()
     return id_venda


def verifica_ingressos(entrada):
     soma = 0
     for chave, valor in entrada.items():
          if type(valor) == type(1):
               soma = soma+valor

     if(soma > 0):
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
     preco_total = 0
     for c, v in new_dados.items():
          produto = Produto.query.filter_by(idProduto = c).first()
          preco_total = float(v)*float(produto.preco)
          insert_prod = insert(Venda_Produto).values(idVenda=id_venda, idproduto=c, quantidadevendida=v, valortotal=preco_total)
          db.session.execute(insert_prod)
     
     db.session.commit()
     return True
     