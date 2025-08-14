# Currency Converter Web App 💰

A modern **Currency Converter** project using **Flask API** and a **responsive HTML front-end** with Bootstrap 5.

---

## 📌 Features

- Convert any currency to another using **ExchangeRate API**.
- Fetches real-time conversion rates.
- Responsive and modern UI with Bootstrap.
- JSON API endpoint for programmatic access.
- CORS enabled for cross-origin requests.

---

## 🛠️ Project Structure

currency-converter/
├─ app.py # Flask API
├─ index.html # Front-end UI
├─ README.md


---

📷 Screenshots

![Home Screen](https://github.com/AhmetFarukTUNC/notepad/blob/main/images/kaydol.jpg)

## 🚀 How to Run

### 1. Clone the repository

```bash

git clone https://github.com/AhmetFarukTUNC/exchangeapi

cd exchangeapi

2. Install dependencies

pip install flask requests flask-cors


3. Run Flask API

python app.py

API will run on http://127.0.0.1:5000/convert

Query Example:

http://127.0.0.1:5000/convert?from=USD&to=TRY&amount=100

4. Open Front-end

Simply open index.html in your browser and use the currency converter.




💻 Example API Response

{
    "from": "USD",
    "to": "TRY",
    "amount": 100,
    "rate": 33.45,
    "converted_amount": 3345.0
}


⚡ Notes

Make sure to replace API_KEY in app.py with your own ExchangeRate API key.

CORS is enabled, so you can fetch from different domains.

