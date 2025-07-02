from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to portscanning backend!"})

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json(silent=True) or {}
    # Your analyze logic here
    return jsonify({"message": "Hello from analyze!", "received": data})
