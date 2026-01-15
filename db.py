import pandas as pd
from fastapi import FastAPI, APIRouter, UploadFile, Query, Form
import shutil
import multipart
import models


def upload_file(file: UploadFile):
        if not file.filename.lower().endswith(('.csv')):
            return 404,"Please upload csv file."

        if file.filename.lower().endswith(".csv"):
            extension = ".csv"

        filepath = "C:\\projects\\data-course\\tests\\week-13-terrorists-api-k8s\\terrorists_data"+ extension

        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        try:
            if filepath.endswith(".csv"):
                df = pd.read_csv(filepath)
                return df
        except:
            return 401, "File is not proper"


def extract_top_5():
    df = pd.read_csv('terrorists_data.csv')
    top = df.sort_values(by=['danger_rate'], ascending= False)
    top_5 = top.head()
    return top_5.to_dict()


# b = {"d": top_5}
# c = {"name": top_5['name'], "location": b['d']['location'], "danger_rate": b['d']['danger_rate']}
# print(c)
# d = {"name": top_5["name"]}
# #print(type(d))
#print(b['d']['name'])

def validating(top_5):
    external_dict = {"conut": 5, "top": []}
    for column in top_5:
        if column in ['name', 'location', 'danger_rate']:
            for name 




a = extract_top_5()
b = validating(a)

# print(extract_top_5())