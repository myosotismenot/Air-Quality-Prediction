# Docker Files for EDA/Model creation

This docker folder contains the files necessary to recreate the docker image for accessing the api as well as creating the model/pickle file necessary for the eda should you want to recreate locally.

## Instructions

To build first time, you can simply run this command within terminal as long as you are located in this directory.

```
docker compose up -d
```

Alternatively, if you change some files, make sure to run

```
docker compose up --build -d
```
