from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json(force=True)
    return jsonify({"message": "Hello from analyze!", "received": data})

if __name__ == '__main__':
    app.run()
