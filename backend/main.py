from typing import Union
from fastapi import FastAPI
from langchain.chat_models.openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
import os
from dotenv import load_dotenv
from typing import Optional
from pydantic import BaseModel


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

llm = ChatOpenAI(openai_api_key="...")
app = FastAPI()



@app.get("/")
async def read_root():

    chat = ChatOpenAI(
        openai_api_key=os.environ["API_KEY"],
        temperature=0.1,
        max_tokens=2048,
        model_name="gpt-3.5-turbo-0613",
    )

    # question = 'korea?'
    # print(f'answer {chat.predict(question)}')
    
    # message = [
    #     SystemMessage(content="""
    #                   You are SQL Developer. My database is innodb mysql.
    #                   The database has a table named 'players' with the following columns: id, name, age.
    #                   The database has another table named 'teams' with the following columns: id, name, player_id.
    #                   """, type="system"),
    #     HumanMessage(content="What is the SQL query to get the names of all players?", type="human"),
    #     AIMessage(content="SELECT name FROM players", type="ai"),
    # ]

    message = [
        SystemMessage(content="""
                      You are a traveler.
                      I know the capitals of every country in the world.
                      """, type="system"),
        HumanMessage(content="where is korea capitals?", type="human"),
        AIMessage(content="seoul", type="ai"),
    ]
    
    print('answer2 : ',chat.predict_messages(message))
    return {"Hello": message}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str,  None] = None):
    return {"item_id": item_id, "q": q}

class Item(BaseModel):
    question :str

@app.post("/chat/")
def chatting(question: str):
    print("question ",question)
    return question