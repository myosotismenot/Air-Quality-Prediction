# Air-Quality-Prediction

Westwood Air Quality Prediction for STAT 418 Final Project. 

You can access the Shiny App hosted on Google Cloud Run [here](https://rfshiny-1099088179937.us-central1.run.app/).

You can also acess the Flask API hosted on a separate instance of Google Cloud Run [here](https://rf-aqi-1099088179937.us-central1.run.app/).
If you would like to test the Flask API model via input in terminal, you can do as so:

Test input for terminal:
```
curl -X POST https://rf-aqi-1099088179937.us-central1.run.app/predict \
  -H "Content-Type: application/json" \
  -d '{"temp": 25, "precip": 0, "humidity": 60, "cloud": 30}'
```
Expected output:
```
{
  "pm2_5_prediction": 19.0
}
```

For more info on the api/app itself, read more below as well as access the individual readme's in their respective directories.

## Background

The Westwood Air Quality Prediction App is a simple app that predicts the PM2.5 ppm based on four weather factors. These factors include the temperature (celsius), precipitation (mm), relative humidity (%), and cloud coverage(%). The model utilized is a random forest model. As this app was mainly designed for learning how to use shiny, docker, and other tools, I have not tried to fine-tune or achieve the best performing model, but aimed to simply build something that is clean and simple. The data utilized was obtained via Open-meteo's [free weather api](https://open-meteo.com/).

## Light EDA

correlation plot

interesting table

trends

## Methodology

## Deployment

## Results


