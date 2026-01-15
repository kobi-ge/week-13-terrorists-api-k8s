from fastapi import FastAPI, HTTPException, APIRouter, UploadFile, Query, Form
import uvicorn

import db

app = FastAPI()



router = APIRouter()

@router.post("/top-threats")
def post_terrorists(file: UploadFile):
    df = db.UploadFile(file)
    top_5 = db.extract_top_5(df)
    dict_format = db.to_final_dict(top_5)
    return dict_format





app.include_router(router)

