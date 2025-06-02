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

### Summary Statistics

To get a better idea of the data, here is a table of the summary statistics

| Statistic | temperature_2m | precipitation | relative_humidity_2m | cloud_cover | pm2_5 |
|-----------|----------------|---------------|-----------------------|-------------|--------|
| **Count** | 365.000        | 365.000       | 365.000               | 365.000     | 365.000 |
| **Mean**  | 16.579         | 0.602         | 66.773                | 37.325      | 21.580  |
| **Std**   | 4.275          | 2.976         | 18.872                | 28.627      | 13.476  |
| **Min**   | 8.068          | 0.000         | 7.620                 | 0.000       | 4.754   |
| **25%**   | 13.345         | 0.000         | 60.081                | 10.250      | 13.771  |
| **50%**   | 15.799         | 0.000         | 73.363                | 34.208      | 18.379  |
| **75%**   | 19.885         | 0.000         | 79.439                | 60.875      | 26.404  |
| **Max**   | 33.245         | 29.800        | 93.886                | 99.375      | 141.733 |

Our data ranges from 1 April 2024 to 31 March 2025, in which we have converted the data from hourly to daily based on averages. We see there are no missing values based on the count. Some of this information is expected For example, we typically don't see to much precipitation in California, which is why up to the 75th quartile, there is still 0 mm for precipitation. Likely, the pm2.5 content is skewed, as the average and the median differ heavily, which is also similar to what we see in precipitation.

### Correlation Plot

Inline-style: 
![alt text](https://github.com/myosotismenot/Air-Quality-Prediction/blob/main/Images-slides/Heatmap.png "Heatmap")

interesting table

trends

## Methodology

## Deployment

## Results


