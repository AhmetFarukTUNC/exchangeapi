from flask import Flask, request, jsonify
import requests
import json
from flask_cors import CORS  # <-- Bunu ekle

app = Flask(__name__)
CORS(app)  # <-- Tüm alanlardan gelen isteklere izin verir

API_KEY = "6cad53ea6437f497f2c8e9d2"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

@app.route("/convert", methods=["GET"])
def convert_currency():
    bozulan_doviz = request.args.get("from")  # Örn: USD
    alinan_doviz = request.args.get("to")     # Örn: TRY
    miktar = request.args.get("amount", type=float)

    if not bozulan_doviz or not alinan_doviz or miktar is None:
        return jsonify({"error": "Eksik parametre. from, to, amount gerekli"}), 400

    try:
        response = requests.get(BASE_URL + bozulan_doviz.upper())
        data = response.json()

        if "conversion_rates" not in data:
            return jsonify({"error": "API'den veri alınamadı", "details": data}), 500

        oran = data["conversion_rates"].get(alinan_doviz.upper())
        if oran is None:
            return jsonify({"error": f"{alinan_doviz} para birimi bulunamadı"}), 400

        sonuc = miktar * oran

        return jsonify({
            "from": bozulan_doviz.upper(),
            "to": alinan_doviz.upper(),
            "amount": miktar,
            "rate": oran,
            "converted_amount": sonuc
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
