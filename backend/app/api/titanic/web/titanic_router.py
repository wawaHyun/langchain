
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
    
    # hello = open('C:\\Users\\bitcamp\\TuringTeamPJT\\langchain\\backend\\app\\api\\titanic\\data\\hellow.txt')
    # # f = open("D:/101. work/python/res/path_test/test.txt", "r", encoding="utf-8")
    # data = hello.read()
    # print(data)
    # hello.close()
 
    print(req)
    return {"answer": "titanic 생존자는 100명"}
