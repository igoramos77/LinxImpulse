from application import app
from flask import render_template, request
import json
from application.model.entity.produto import Produto


@app.route("/")
@app.route("/index")
def index():
  
  with open('application\\view\\static\\json\\products.json') as product_file:
    product_list = json.load(product_file)
  productList = []
  for product in product_list:
    productList.append(Produto(product['id'], product['name'], product['image'],product['oldPrice'],product['price'],product['description'],product['installments']['count'],product['installments']['value']))
  return render_template("index.html", productList=productList)