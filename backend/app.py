from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

items = []

@app.route('/add-item', methods=['POST'])
def add_item():
    data = request.json
    items.append(data['item'])
    return jsonify({"message": "Item added successfully!"})

@app.route('/get-items', methods=['GET'])
def get_items():
    return jsonify(items)

if __name__ == "__main__":
    app.run(debug=True)
