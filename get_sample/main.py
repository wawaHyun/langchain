from fastapi import FastAPI
import uvicorn
from example.bmi import BMI
from example.leap_year import LeapYear
from get_sample.example.rps import RPS

app = FastAPI()


@app.get("/api/sample/bmi")
async def root():
    result = BMI.getBMI()
    return {"answer": "bmi : {result}"}

@app.get("/api/sample/leapyear")
async def root():
    result = LeapYear.is_leap_year()
    return {"answer": "leapyear : {result}"}

@app.get("/api/sample/rps")
async def root():
    result = RPS.play()
    return {"answer": "rps result : {result}"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)