# Flask API

This Folder contains all the files related to the flask api. The flask api can be found [here](https://rf-aqi-1099088179937.us-central1.run.app).

To test whether this api is currently running, you can click the link. Alternatively you can test by utilizing the model.

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
## Contents
Here are the files contained within this folder:

- this README.md file
- `api.py` - python file containing the flask api to GET/POST
- `docker-compose.yml` - yaml file to compose docker via `docker compose up -d`
- `Dockerfile` - File to make docker locally
- `model.py` - python file that flask api calls to get model results
- `requirements.txt` - text file containing the necessary python modules
- `rf_pm25_model.pkl` - pickle file containing model

You can use the docker files to run this flask api locally and/or deploy it to google cloud run yourself. This will be necessary if you try to run this after i shut down access to my flask api after the quarter ends.
