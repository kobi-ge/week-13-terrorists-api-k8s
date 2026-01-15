import pandas as pd
from fastapi import FastAPI, APIRouter, UploadFile, Query, Form
import shutil
import multipart
import models
from pymongo import MongoClient

class Connection:
    def __init__(self):
        self.coll =None

    def connect(self):
        try:    
            uri = "mongodb://localhost:27017/"
            client = MongoClient(uri)
            client.connect()


        except Exception as e:
            raise Exception(
        "The following error occurred: ", e)



# client.close()

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


def extract_top_5(df):
    top = df.sort_values(by=['danger_rate'], ascending= False)
    top_5 = top.head()
    data = top_5.to_dict(orient= "tight", index=False)
    return data['data']


def to_final_dict(data):
    external_dict = {"conut": 5, "top": []}
    internal_dict = {}
    for terrorist in data:
        internal_dict['name'] = terrorist[0]
        internal_dict['danger_rate'] = terrorist[1]
        internal_dict['location'] = terrorist[2]
        external_dict['top'].append(internal_dict)
    return external_dict


