
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Request(BaseModel):
    question :str

class Response(BaseModel):
    answer :str

@router.post("/titanic")
async def titanic(req:Request):
    print("titanic 진입완")
    print(req)
    return {"answer": "titanic"}
