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

We can get some ideas of the relationship between the predictors as well as the response with a correlation heatmap.

![alt text](https://github.com/myosotismenot/Air-Quality-Prediction/blob/main/Images-slides/output.png "Heatmap")

Here is a correlation plot of the numerical predictors as well as the pm2.5 concentration. From here, we can see that none of the predictors have a particularly strong correlation with the response.

### trends

Let's look at the overall trend over the past year of some of the variables

![alt text](https://github.com/myosotismenot/Air-Quality-Prediction/blob/main/Images-slides/temp.png "Temperature")

Overall relatively cool other than an increase around September. Interesting that it did not get hotter around the time of the fires.

![alt text](https://github.com/myosotismenot/Air-Quality-Prediction/blob/main/Images-slides/humidity.png "Humidity")

The humidity seems to vary based on the time of year, but we can see the lowest point was around the time of the fires.

![alt text](https://github.com/myosotismenot/Air-Quality-Prediction/blob/main/Images-slides/cloudcover.png "Cloud Coverage")

The cloud coverage had the strongest correlation with humidity. Base on the plot, it can be difficult at points though.

![alt text](https://github.com/myosotismenot/Air-Quality-Prediction/blob/main/Images-slides/pm2.5.png "Response - Pm2.5 Concentration")

The overall pM2.5 concentration within the past year.

## Methodology

The data was retrieved via open-meteo's weather api. To see how to use it and the data, you can visit their [website](https://open-meteo.com/), as well as examine the Access-Api-and-EDA directory. To access the api, we utilizied a python notebook, and saved the data in chunks of 3 months (maximum) split for weather and data. The csv for the data can also be found in the folders as well.

We used a random forest model, as it was a simple model that can be utilized for this data. The building of this model can be found in `prediction.ipynb`, which outputs a `rf_pm25_model.pkl` file that is used by the flask api app. While this file is not included in the github due to size limitations, you can run the `prediction.ipynb` if you wish to see/run it yourself.

## Deployment

The information related to deployment of the flask api and the shiny app can be found in the [api](https://github.com/myosotismenot/Air-Quality-Prediction/tree/main/api) and [app](https://github.com/myosotismenot/Air-Quality-Prediction/tree/main/app) directories, respectively. They are both hosted on separate Google Cloud Run instances, but can also be run locally.

The flask api portion uses the random forest model created in the methodology portion. There is a `model.py` file that utilizes the pickle file created from the methodology portion that contains a predict function to make a prediction. The `api.py` file contains the Flask API that listens for a user to either test that the server is running or retrieve the input data in order to make a prediction via POST.

The shiny app portion contains the app portion of the project in `app.py`, which allows a user to drag via a slider the inputs for the prediction. The shiny app then calls the flask api to get the prediction, which the shiny app will then display.

## Results

You can see the model in action via visiting the shiny app or utilizing the flask api, whether locally, self deployed, or the links above while they are still active. As a user, you can drag the sliders for the four predictors and press predict to get a prediction of the pm2.5 concentration. To see an image of this, you can look at the final slide of this [presentation](https://github.com/myosotismenot/Air-Quality-Prediction/blob/main/Images-slides/Tu%20Timothy%20Final%20Presentation.pdf).


