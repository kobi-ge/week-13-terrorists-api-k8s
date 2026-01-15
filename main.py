from fastapi import FastAPI, HTTPException, APIRouter, UploadFile, Query, Form
import uvicorn

import db

app = FastAPI()



router = APIRouter()

@router.post("/top-threats")
def post_terrorists(file: UploadFile):
    df = db.UploadFile(file)
    #top_5 = db.extract_top_5(df)
    return df





app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app="main:main", host="127.0.0.1", port=8000)