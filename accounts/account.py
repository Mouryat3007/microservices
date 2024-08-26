from flask import Flask, jsonify

app = Flask(__name__)

# Sample account data
account = {
    'username': 'johndoe',
    'email': 'johndoe@example.com',
    'name': 'John Doe'
}

@app.route('/account', methods=['GET'])
def get_account():
    return jsonify({
        'account': account,
        'status': 'success'
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
