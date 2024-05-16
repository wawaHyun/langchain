from fastapi import FastAPI
import uvicorn
from example.bmi import BMI

app = FastAPI()

bmi = BMI()


@app.get("/")
async def root():
    bmi.bmi_try()
    return {"message": "oh hoh"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)