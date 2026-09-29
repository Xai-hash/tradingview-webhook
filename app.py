from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BOT_TOKEN = "8803947694:AAGFEuY74Ernu4_3dNNIQNgEOJAd0WxKa9w"
CHANNEL_ID = "-1004477871320"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if not data:
        return jsonify({"status": "no data"}), 400

    ticker = data.get('ticker', 'N/A')
    action = data.get('action', 'SIGNAL')
    price = data.get('price', 'N/A')
    timeframe = data.get('timeframe', '')

    message = (
        f"🚨 **NEW TRADING SIGNAL** 🚨\n\n"
        f"📈 **Asset:** {ticker}\n"
        f"⚡ **Action:** {action.upper()}\n"
        f"💰 **Price:** {price}\n"
        f"⏱️ **Timeframe:** {timeframe}"
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    requests.post(url, json=payload)
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
