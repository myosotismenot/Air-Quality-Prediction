# Shiny App

This folder contains the files related to the shiny app itself. The shiny app is hosted on google cloud run, and uses the flask api in a separate google cloud run to get the prediction from the random forest model. While it is still running, it can be found [here](https://rfshiny-1099088179937.us-central1.run.app/).

## Contents

Here are the files that you can find in this directory.

- `README.md` - this file containing info.
- `app.py` - Python file containing the shiny app
- `docker-compose.yml` - YAML file for Docker composition
- `Dockerfile` - file to recreate Docker image
- `requirements.txt` - text file containing required python modules

## Running locally/elsewhere

Should the app be taken down (once the quarter ends), the shiny app can be reconstructed here. However, it is likely that the google cloud run instance of the flask api has also been taken down. In this case, please make sure to change this line located in `app.py`. Likely, you can change it to a local instance or your own hosted instance of the flask api from the api folder in this same repository.

```
FLASK_API_URL = "https://rf-aqi-1099088179937.us-central1.run.app/predict"
```
