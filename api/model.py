import pickle
import pandas as pd

with open("rf_pm25_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_pm25(temp, precip, humidity, cloud):
    df = pd.DataFrame([{
        "temperature_2m": temp,
        "precipitation": precip,
        "relative_humidity_2m": humidity,
        "cloud_cover": cloud,
    }])
    prediction = model.predict(df)[0]
    return round(prediction, 2)