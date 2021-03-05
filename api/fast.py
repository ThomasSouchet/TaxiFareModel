from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def index(response : Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return {"greeting": "Hello world"}

@app.get("/predict_fare")
def predict(pickup_datetime, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count):
    dict_ =  {
            "pickup_datetime": pickup_datetime,
            "pickup_longitude": pickup_longitude,
            "pickup_latitude": pickup_latitude,
            "dropoff_longitude": dropoff_longitude,
            "dropoff_latitude": dropoff_latitude,
            "passenger_count": passenger_count
            }
    return dict_

if __name__ == "__main__":
    dict_ =  {
            "pickup_datetime": "2013-07-06%2017:18:00%20UTC",
            "pickup_longitude": "-73.950655",
            "pickup_latitude": "40.783282",
            "dropoff_longitude": "-73.984365",
            "dropoff_latitude": "40.769802",
            "passenger_count": "1"
            }
    X_pred = pd.DataFrame(dict_, index=[0])
    print(X_pred)