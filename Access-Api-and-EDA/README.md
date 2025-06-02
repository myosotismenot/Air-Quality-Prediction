Here is the code I used to obtain the data from the open-meteo api, as well as some EDA. The api works in a way where a set of data can be obtained in a period up to 3 months long.

For `retrieve_aqi_from_api.ipynb` and `retrieve_weather_from_api.ipynb`, the `params` section is listed as:
```
params = {
	"latitude": 34.0588, # geographical coordinates of Westwood
	"longitude": -118.4439,
	"hourly": ["pm10", "pm2_5", "carbon_monoxide"], # dependant on which file
	"start_date": "2025-01-01", # start date to edit
	"end_date": "2025-03-31" # end date to edit
}
```
The `start_date` and `end_date` can be changed to fit what period of data you want to retrieve. The maximum range the start and end date is a period of 3 months, so to get a larger range, you can either run the code multiple times with different ranges or copy/paste with a different range to run at once.

`weather_aqi_eda.ipynb` contains some light EDA performed to get a brief look at data before the midterm presentation.

We used a random forest model, as it was a simple model that can be utilized for this data. The building of this model can be found in `prediction.ipynb`, which outputs a `rf_pm25_model.pkl` file that is used by the flask api app. While this file is not included in the github due to size limitations, you can run the `prediction.ipynb` if you wish to see/run it yourself.

All of these files should be able to run with the Docker image contained within the dockerfile folder. To do so, make sure you have docker installed. Afterwards, go to the folder containing the docker files within terminal and run:

```docker compose up -d```

From there, you should be able to go to [localhost:8888](http://localhost:8888/lab) to view/edit the jupyter notebooks, as well as view the files from browser.
