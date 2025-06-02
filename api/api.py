from flask import Flask, request, jsonify
import pickle

HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}

with open("rf_pm25_model.pkl", "rb") as f:
    model = pickle.load(f)

def flask_app():
    app = Flask(__name__)


    @app.route('/', methods=['GET'])
    def server_is_up():
        # print("success")
        return 'server is up - nice job! \n \n'

    @app.route('/predict', methods=['POST'])
    def predict():
        data = request.json
        temp = data.get("temp")
        precip = data.get("precip")
        humidity = data.get("humidity")
        cloud = data.get("cloud")
    
        # Simple input validation
        if None in [temp, precip, humidity, cloud]:
            return jsonify({"error": "Missing input data"}), 400
        
        X = [[temp, precip, humidity, cloud]]
        prediction = model.predict(X)[0]
        
        return jsonify({"pm2_5_prediction": round(prediction, 2)})
    return app
if __name__ == '__main__':
    app = flask_app()
    app.run(debug=True, host='0.0.0.0',port=5001)