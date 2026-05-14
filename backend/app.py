from flask import Flask, request, jsonify
from flask_cors import CORS

from ml_model import train_model, predict_return
from sip_calculator import calculate_sip
from advisor import get_advice

app = Flask(__name__)

CORS(app)

model = train_model()

@app.route("/calculate", methods=["POST"])

def calculate():

    try:

        data = request.get_json()

        amount = float(data["amount"])

        years = int(data["years"])

        rate = float(data["rate"])

        invested, returns, total = calculate_sip(
            amount,
            rate,
            years
        )

        prediction = predict_return(
            model,
            years
        )

        advice = get_advice(
            prediction
        )

        return jsonify({

            "Expected Amount": round(total, 2),

            "Amount Invested": round(invested, 2),

            "Wealth Gain": round(returns, 2),

            "Predicted Return": prediction,

            "AI Advice": advice
        })

    except Exception as e:

        return jsonify({

            "error": str(e)
        })

if __name__ == "__main__":

    app.run(debug=True)