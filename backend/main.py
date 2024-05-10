from typing import Union
from fastapi import FastAPI
from langchain.chat_models.openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
import os
from dotenv import load_dotenv
import uvicorn
from app.api.titanic.model.titanic_model import TitanicModel
from app.main_router import router
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

class Request(BaseModel):
    question: str

class Response(BaseModel):
    answer: str

llm = ChatOpenAI(openai_api_key="...")
app = FastAPI()

app.include_router(router)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Hello": "message"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str,  None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/chat")
def chatting(req:Request):
    print(req)

    chat= ChatOpenAI(
        openai_api_key=os.environ["api_key"],
        temperature=0.1,
        max_tokens=2048,
        model_name = 'gpt-3.5-turbo-0613'
    )
    # question = '대한민국의 수도는 뭐야?'질문Unexpected indentation

    # result = chat.predict(question)

    # print(f'[답변] : {result}')

    message= [
        SystemMessage(content="You are a traveler. I know the capitals of every country in the world",type="system"),
        HumanMessage(content="한국의 수도는 어디야 ?",type="human"),
        AIMessage(content="서울 입니다.", type="ai")
    ]

    print(f'[답변] : {chat.predict_messages(message)}')

    return  Response(answer=chat.predict(req.question))

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)