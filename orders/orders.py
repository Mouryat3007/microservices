from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample orders data
orders = [
    {'order_id': 1, 'product_name': 'Product 1', 'quantity': 2, 'status': 'shipped'},
    {'order_id': 2, 'product_name': 'Product 2', 'quantity': 1, 'status': 'processing'},
]

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify({
        'orders': orders,
        'status': 'success'
    }), 200

@app.route('/orders', methods=['POST'])
def create_order():
    new_order = request.get_json()
    orders.append(new_order)
    return jsonify({
        'message': 'Order created successfully',
        'order': new_order,
        'status': 'success'
    }), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
