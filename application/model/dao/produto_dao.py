import json
from application.model.entity.produto import Produto

class ProdutoDAO:
  def __init__(self):
    self._lista_produtos = []
    self._product_list = []

  def getProducts(self):
    with open('application\\view\\static\\json\\products.json') as product_file:
      product_list = json.load(product_file)

    productList = []
    for product in product_list:
      productList.append(Produto(product['id'], product['name'], product['image'],product['oldPrice'],product['price'],product['description'],product['installments']['count'],product['installments']['value']))
    return productList

  def instanceProducts(self):
    self.getProducts()
    for product in self._product_list:
        self._lista_produtos.append(Produto(product['id'], product['name'], product['image'],product['oldPrice'],product['price'],product['description'],product['installments']['count'],product['installments']['value']))

  def listProduct(self):
    self.instanceProducts()
    return self._lista_produtos