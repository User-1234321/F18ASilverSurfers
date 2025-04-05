from fastapi import FastAPI
from f18asilversurfers.database import Base, SessionLocal, engine
from f18asilversurfers.routes import order, despatch_advice


app = FastAPI()

app.include_router(order.router)
app.include_router(despatch_advice.router)
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
