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
#from mistral_api import MistralChat, setup_logger



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "This is Letters Service!"}



#Прогноз по найму на день
@app.get("/day_forecast")
async def forecast():
    try:
        return {'forecast': "Its raining men, aliluya"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Что то наебнулос: {ex}")
    



#Суммаризация резюме
class Request_Summ_Reс(BaseModel):
    full_resume: str = "Текст полного резюме"


@app.post("/summarize_resume")
async def summ_rec(request: Request_Summ_Reс):
    try:
        return {'summary': 'Что то будет написано по резюме'}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Что то наебнулос: {ex}")
    


# Суммаризированный расклад Таро по персональной информации пользователя
class summarize_tarot_spread(BaseModel):
    full_tarot: str = "Полный расклад таро"


@app.post("/summarize_tarot_spread")
async def summ_tarot(request: summarize_tarot_spread):
    try:
        return {'summary': 'У тебя пиписька отвалится'}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Что то наебнулос: {ex}")
        


#Полный расклад Таро по персональной информации пользователя
class Request_Tarot_Spread(BaseModel):
    resume_summary: str = "Краткая инфа по резюме человека"


@app.post("/tarot_spread")
async def full_tarot_spread(request: Request_Tarot_Spread):
    try:
        return {'tarot_spread': 'ДА ПРИБУДЕТ С ТОБОЙ СИЛА И СОЛНЦЕ НАД ТОБОЙ'}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Что то наебнулос: {ex}")
    


#Расклад по заданному вопросу
class Request_Question_Tarot_Spread(BaseModel):
    user_question: str = "Любит - Не любит"


@app.post("/question_tarot_spread")
async def question_tarot_spread(request: Request_Question_Tarot_Spread):
    try:
        return {'tarot_spread': 'Иди траву потрогуй да одувангчик подари, а не фигнёй занимайся'}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Что то наебнулос: {ex}")
    




#Построение карты компетенций
class Request_Competency_Map(BaseModel):
    source: str = '"summarized_tarot" или "resume"',
    data: str = "Суммаризированный расклад или текст резюме"


@app.post("/competency_map")
async def competency_map(request: Request_Competency_Map):
    try:
        return {'map': 'что то в форме json'}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Что то наебнулос: {ex}")
    



#Характеристика с прошлых мест работы
class Request_Work_History(BaseModel):
    full_resume: str = "Текст полного резюме"


@app.post("/work_history_review")
async def work_history_review(request: Request_Work_History):
    try:
        return {'work_review': 'Он был прекрасен как Иисус'}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Что то наебнулос: {ex}")
    


#Рекомендательная система
class Request_Recommendations(BaseModel):
    context: str = "Что именно нужно рекомендовать",
    data: str =  "Дополнительные данные, например, резюме или расклад"


@app.post("/recommendations")
async def recommendations(request: Request_Recommendations):
    try:
        return {'recommendations': ["Рекомендация 1: потрогай траву", "Рекомендация 2: попой песенки"]}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Что то наебнулос: {ex}")
    






if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)