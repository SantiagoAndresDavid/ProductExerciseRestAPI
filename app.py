from crypt import methods
from itertools import product
from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/ping')

def ping():
    return jsonify({"message": "pong"})
    
@app.route('/products')
def getProducts():
    # return jsonify(products)
    return jsonify({'products': products})


@app.route('/products/<string:product_name>')
def getProduct (product_name):
    product_found = [product for product in products if product['name'] == product_name.lower()]
    if(len(product_found) > 0):
       return jsonify({'product':product_found[0]})
    return jsonify("message", "product not found")

@app.route('/products',methods=['POST'])
def add_product():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message":"product added successfully", "products": products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'Product Updated',
            'product': productsFound[0]
        })
    return jsonify({'message': 'Product Not found'})

if __name__ == '__main__':
    app.run(debug=True, port =4000)