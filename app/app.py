from shiny import App, ui, render, reactive
import requests

app_ui = ui.page_fluid(
    ui.h2("PM2.5 Prediction"),
    ui.input_slider("temp", "Temperature (°C)", min=-30, max=50, value=22.5, step=0.1),
    ui.input_slider("precip", "Precipitation (mm)", min=0, max=100, value=0.0, step=0.1),
    ui.input_slider("humidity", "Relative Humidity (%)", min=0, max=100, value=55, step=1),
    ui.input_slider("cloud", "Cloud Cover (%)", min=0, max=100, value=20, step=1),
    ui.input_action_button("predict", "Predict"),
    ui.output_text("result")
)

FLASK_API_URL = "https://rf-aqi-1099088179937.us-central1.run.app/predict"

def server(input, output, session):
    @reactive.event(input.predict)
    def get_prediction():
        try:
            response = requests.post(
                FLASK_API_URL,
                json={
                    "temp": input.temp(),
                    "precip": input.precip(),
                    "humidity": input.humidity(),
                    "cloud": input.cloud()
                },
                timeout=200
            )
            response.raise_for_status()
            return response.json().get("pm2_5_prediction", "No prediction returned")
        except Exception as e:
            return f"API Error: {e}"

    @output
    @render.text
    def result():
        return f"Predicted PM2.5: {get_prediction()}"

app = App(app_ui, server)