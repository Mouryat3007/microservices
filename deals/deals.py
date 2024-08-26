from flask import Flask, jsonify

app = Flask(__name__)

# Sample deals data
deals = [
    {'id': 1, 'product_name': 'Product 1', 'discount': '10%'},
    {'id': 2, 'product_name': 'Product 2', 'discount': '15%'},
    {'id': 3, 'product_name': 'Product 3', 'discount': '20%'},
]

@app.route('/')
def get_deals():
    return jsonify({
        'deals': deals,
        'status': 'success'
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
