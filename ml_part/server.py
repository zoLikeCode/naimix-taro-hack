import json
import logging
import os
import uuid
from datetime import datetime, timedelta
import contextvars

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from logging.handlers import RotatingFileHandler
from pydantic import BaseModel
import uvicorn
from api import Api
#from mistral_api import MistralChat, setup_logger

load_dotenv()
API = os.getenv("MODEL_API")


app = FastAPI()
chat = Api(API_KEY=API)

@app.get("/")
async def root():
    return {"message": "This is Letters Service!"}



#Прогноз по найму на день +
@app.get("/day_forecast")
async def forecast():
    try:
        rec = chat.forecast()
        return rec
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Что то: {ex}")
    



#Суммаризация резюме +
class Request_Summ_Reс(BaseModel):
    full_resume: str = "Текст полного резюме"


@app.post("/summarize_resume")
async def summ_rec(request: Request_Summ_Reс):
    try:
        summary = chat.summ_rec(request.full_resume)
        return summary
    
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Что то: {ex}")
    


# Суммаризированный расклад Таро по персональной информации пользователя +
class summarize_tarot_spread(BaseModel):
    summary: str = "Полный расклад таро"


@app.post("/summarize_tarot_spread")
async def summ_tarot(request: summarize_tarot_spread):
    try:
        summary = chat.summ_tarot_full(request.summary)
        return summary
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Что то: {ex}")
    


#Расклад таро по 1 карте для кандидата +
class Request_Tarot_One(BaseModel):
    resume_summary: str = "Краткая инфа по резюме человека"


@app.post("/tarot_one")
async def one_tarot_spread(request: Request_Tarot_One):
    try:
        tarot_spread = chat.tarot_one(request.resume_summary)
        return tarot_spread
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Что то: {ex}")
        


#Полный расклад Таро по персональной информации пользователя +
class Request_Tarot_Spread(BaseModel):
    resume_summary: str = "Краткая инфа по резюме человека"


@app.post("/tarot_spread")
async def full_tarot_spread(request: Request_Tarot_Spread):
    try:
        tarot_spread = chat.tarot_spread(request.resume_summary)
        return tarot_spread
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Что то: {ex}")
    


#Расклад по заданному вопросу +
class Request_Question_Tarot_Spread(BaseModel):
    user_question: str = "Любит - Не любит"


@app.post("/question_tarot_spread")
async def question_tarot_spread(request: Request_Question_Tarot_Spread):
    try:
        rec = chat.question(request.user_question)
        return rec
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Что то: {ex}")
    









#Построение карты компетенций
class Request_Competency_Map(BaseModel):
    full_resume: str = "Полное резюме"


@app.post("/competency_map")
async def competency_map(request: Request_Competency_Map):
    try:
        rec = chat.competency_map(request.full_resume)
        return {'map': 'что то в форме json'}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Что то: {ex}")
    









#Характеристика с прошлых мест работы
class Request_Work_History(BaseModel):
    full_resume: str = "Текст полного резюме"


@app.post("/work_history_review")
async def work_history_review(request: Request_Work_History):
    try:
        return {'work_review': 'Он был прекрасен как Иисус'}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Что то: {ex}")
    











#Рекомендательная система
class Request_Recommendations(BaseModel):
    context: str = "Что именно нужно рекомендовать",
    data: str =  "Дополнительные данные, например, резюме или расклад"


@app.post("/recommendations")
async def recommendations(request: Request_Recommendations):
    try:
        return {'recommendations': ["Рекомендация 1: потрогай траву", "Рекомендация 2: попой песенки"]}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Что то: {ex}")
    






if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)