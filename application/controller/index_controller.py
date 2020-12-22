from application import app
from flask import render_template, request
import json
from application.model.entity.produto import Produto
from application.model.dao.produto_dao import ProdutoDAO

@app.route("/")
@app.route("/index")
def index():
  
  produtoDao = ProdutoDAO()
  productList = produtoDao.getProducts()
  return render_template("index.html", productList=productList)