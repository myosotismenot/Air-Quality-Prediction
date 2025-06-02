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
The `start_date` and `end_date` can be changed to fit what period of data you want to retrieve.

`weather_aqi_eda.ipynb` contains some light EDA performed to get a brief look at data before the midterm presentation.

`pre-prediction.ipynb` contains some more EDA performed before the final presentation, also used to try and create a more concrete idea for the final app.
