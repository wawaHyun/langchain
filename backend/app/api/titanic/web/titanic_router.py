
from fastapi import APIRouter
from pydantic import BaseModel
from app.api.titanic.service.titanic_service import TitanicService
import sys
sys.setrecursionlimit(10000)


router = APIRouter()
service = TitanicService()

class Request(BaseModel):
    question :str

class Response(BaseModel):
    answer :str

@router.post("/titanic")
async def titanic(req:Request):
    print("titanic 진입완1")
    
    hello = 'C:\\Users\\bitcamp\\TuringTeamPJT\\langchain\\backend\\app\\api\\titanic\\data\\hellow.txt'

    f = open(hello, "r", encoding="utf-8")
    data = f.read()
    print(data)
    f.close()

    result = service.process()
 
    print(req)
    return {"answer": result}
