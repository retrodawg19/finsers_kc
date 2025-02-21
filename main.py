from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from typing import List

import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend is running!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
app = FastAPI()

# Define the request schema
class InputData(BaseModel):
    data: List[str]  # Mixed list of numbers & alphabets

# Define the response schema
class OutputData(BaseModel):
    is_success: bool
    user_id: str
    email: str
    roll_number: str
    numbers: List[str]
    alphabets: List[str]
    highest_alphabet: List[str]

# GET request - Returns operation_code
@app.get("/bfhl")
def get_operation_code():
    return JSONResponse(content={"operation_code": 1}, status_code=200)

# POST request - Process input data
@app.post("/bfhl", response_model=OutputData)
def process_data(request: InputData):
    try:
        # Predefined values for user ID, email, and roll number
        user_id = "KunalChopra_16102003"
        email = "choprakunal329@gmail.com"
        roll_number = "22BAi71267"

        # Separate numbers and alphabets
        numbers = [item for item in request.data if item.isdigit()]
        alphabets = [item for item in request.data if item.isalpha()]

        # Find the highest alphabet (case insensitive)
        highest_alphabet = [max(alphabets, key=lambda x: x.upper())] if alphabets else []

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }
        return JSONResponse(content=response, status_code=200)

    except HTTPException as e:
        raise e  # Return user-friendly error messages
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error: " + str(e))