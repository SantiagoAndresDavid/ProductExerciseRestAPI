from crypt import methods
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
    if(len(product_found) >= 1):
       return jsonify({'product':product_found[0]})
    return jsonify("message", "product not found")

@app.route('/products',methods=['POST'])
def add_product():
    print(request.json)
    return 'received'


if __name__ == '__main__':
    app.run(debug=True, port =4000)