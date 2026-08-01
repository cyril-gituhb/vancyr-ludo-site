    from flask import Flask, request, jsonify
    from flask_cors import CORS
    import random
    from datetime import datetime
    import os

    app = Flask(__name__)
    CORS(app)

    ACCESS_CODE = "CYRILKELVIN" 

    @app.route('/api/predict', methods=['POST'])
    def predict():
        data = request.get_json()
        
        if data.get('access_code') != ACCESS_CODE:
            return jsonify({"error": "Accès refusé"}), 403

        odds = data.get('odds', [])
        
        try:
            avg = sum([float(o) for o in odds]) / len(odds)
            predicted = round(avg + random.uniform(0.5, 3.0), 2)
            confidence = random.randint(78, 99)
        except:
            predicted = round(random.uniform(1.50, 15.00), 2)
            confidence = random.randint(60, 80)

        now = datetime.now()
        next_time = (now.replace(second=now.second + 20)).strftime("%H:%M:%S")

        return jsonify({
            "predicted_odds": predicted,
            "confidence": f"{confidence}%",
            "timestamp": next_time
        })

    if __name__ == '__main__':
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
