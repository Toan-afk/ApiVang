
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
        res = requests.get("https://sjc.com.vn", headers=headers, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")
        table = soup.find("table", class_="table")  # lấy bảng đầu tiên
        rows = table.find_all("tr")
        cols = rows[1].find_all("td")
        mua = cols[1].text.strip()
        ban = cols[2].text.strip()
        return jsonify({
            "giavang": f"SJC Mua: {mua} | Bán: {ban}"
        })
    except Exception as e:
        return jsonify({
            "giavang": "Không thể lấy giá từ SJC!"
        })

if __name__ == "__main__":
    app.run()
