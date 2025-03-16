from fastapi import FastAPI, HTTPException
from database import engine, Base
import json

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/validate_despatch/")
async def validate_despatch(data: dict):
    """
    Validates despatch advice details and returns a response.
    """
    despatch_advice_type_code = data.get("key1")
    note = data.get("key2")
    item_name = data.get("key3")
    item_desc = data.get("key4")

    # Initialize response
    response = {}

    # Validate despatch advice type code
    if despatch_advice_type_code not in ["delivery", "partial"]:
        raise HTTPException(status_code=400, detail="DespatchAdviceTypeCode is not valid, please update")

    # Validate note length
    if len(note) > 20:
        raise HTTPException(status_code=400, detail="Note is too long, please update")

    # Validate item name length
    if len(item_name) > 10:
        raise HTTPException(status_code=400, detail="Item name is too long, please update")

    # Validate item description length
    if len(item_desc) > 100:
        raise HTTPException(status_code=400, detail="Item description is too long, please update")

    # Success response
    response_body = {
        "DespatchAdviceTypeCode": despatch_advice_type_code,
        "Note": note,
        "itemName": item_name,
        "itemDesc": item_desc
    }

    return {"statusCode": 200, "body": response_body}
