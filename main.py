from fastapi import FastAPI, HTTPException, APIRouter

app = FastAPI()

app.include_router(router)

