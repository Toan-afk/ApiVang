
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/giavang")
def giavang():
    return jsonify({
        "giavang": "SJC Mua: 116.200.000 | Bán: 117.500.000"
    })

if __name__ == "__main__":
    app.run()
