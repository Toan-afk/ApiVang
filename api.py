from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/giavang")
def giavang():
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        res = requests.get("https://giavang.doji.vn", headers=headers, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        table = soup.find("table", class_="table-price")
        rows = table.find_all("tr")

        for row in rows:
            cols = row.find_all("td")
            if cols and "DOJI HN" in cols[0].text:
                mua = cols[1].text.strip()
                ban = cols[2].text.strip()
                return jsonify({"giavang": f"DOJI HN Mua: {mua} | Bán: {ban}"})
    except Exception as e:
        return jsonify({"giavang": "Không lấy được giá!"})
