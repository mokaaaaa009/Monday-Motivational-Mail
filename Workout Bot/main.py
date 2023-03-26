import json
from datetime import datetime
import requests
import os

NUTRITIONIX_ID=os.environ.get("nutritionix_ID")
NUTRITIONIX_KEY =os.environ.get("nutritionix_Key")
ENDPOINT =os.environ.get("endpoint")
SHEETY_PASSWORD=os.environ.get("SHEETY_PASSWORD")
SHEETY_USERNAME=os.environ.get("SHEETY_USERNAME")
SHEETY_ENDPOINT=os.environ.get("SHEETY_ENDPOINT")
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


headers = {
    "x-app-id":NUTRITIONIX_ID,
    "x-app-key":NUTRITIONIX_KEY,
}
print("Welcome to workout tracker !!!")

query=input(f"Tell us about your workout today:")
params={
    "query":query,
    "gender":"male",
    "weight_kg":66,
    "height_cm":160,
    "age":25,
}

nutrition_response=requests.post(url=ENDPOINT,headers=headers,json=params)
nutrition_json=nutrition_response.json()
exercise=""
duration=0
calories=0

for workout in nutrition_json["exercises"]:
     exercise = workout["name"]+" "
     duration += workout["duration_min"]
     calories += workout["nf_calories"]
date= datetime.now().today().strftime("%d-%m-%Y")
time=datetime.now().strftime("%H:%M:%S")

sheet_params={
    "workout":{
    "date":date,
    "time":time,
    "exercise":exercise.title(),
    "duration":duration,
    "calories":calories,
    }
}
auth=(SHEETY_USERNAME,SHEETY_PASSWORD)


sheety_response=requests.post(SHEETY_ENDPOINT,json=sheet_params,auth=auth)
print(sheety_response.text)









