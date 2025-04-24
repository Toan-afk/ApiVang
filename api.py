
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
        res = requests.get("https://www.24h.com.vn/gia-vang-hom-nay-c425.html", headers=headers, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")

        table = soup.find("table", class_="tblVang") or soup.find("table")  # Fallback nếu class đổi
        rows = table.find_all("tr")

        for row in rows:
            cols = row.find_all("td")
            if cols and "SJC TP.HCM" in cols[0].text:
                mua = cols[1].text.strip()
                ban = cols[2].text.strip()
                return jsonify({
                    "giavang": f"SJC TP.HCM Mua: {mua} | Bán: {ban}"
                })
    except Exception as e:
        return jsonify({
            "giavang": "Không thể lấy giá từ 24h.com.vn!"
        })

if __name__ == "__main__":
    app.run()
