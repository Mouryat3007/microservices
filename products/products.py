from flask import Flask, jsonify

app = Flask(__name__)

# Sample product data
products = [
    {'id': 1, 'name': 'Product 1', 'price': 19.99},
    {'id': 2, 'name': 'Product 2', 'price': 29.99},
    {'id': 3, 'name': 'Product 3', 'price': 39.99},
]

@app.route('/')
def get_products():
    return jsonify({
        'products': products,
        'status': 'success'
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
