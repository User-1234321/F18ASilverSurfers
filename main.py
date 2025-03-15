from fastapi import FastAPI
from routes import despatch_advice

app = FastAPI()

app.include_router(despatch_advice.router)