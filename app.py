from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Example client status data
clients_data = [
    {"name": "Citibank", "status": 75},
    {"name": "Wilmington Trust", "status": 50},
    {"name": "WSFS", "status": 90}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/clients")
def api_clients():
    return jsonify(clients_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
