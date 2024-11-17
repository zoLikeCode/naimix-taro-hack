import os
from datetime import datetime, timedelta

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from logging.handlers import RotatingFileHandler
from pydantic import BaseModel
import uvicorn
from api import Api

load_dotenv()
API = os.getenv("MODEL_API")
ID = os.getenv("FOLDER_ID")


app = FastAPI()
chat = Api(API_KEY = API, FOLDER_ID = ID)


class FullResume(BaseModel): #Запрос с использованием всего резюме
    full_resume: str = "Текст полного резюме"


class SummResume(BaseModel): #Запрос с использованием суммаризированного резюме
    resume_summary: str = "Краткая инфа по резюме человека"


class Question(BaseModel): #Запрос с использованием вопроса человека
    user_question: str = "Любит - Не любит"


class TarotSpread(BaseModel): # Запрос с использованием полного расклада таро
    taro_spred: str = "Полный расклад таро"

class FeedBack(BaseModel):
    candidate_name: str = "ФИО кандидата",
    feedback_type: int =  0



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
        raise HTTPException(status_code=500, detail=f"Произошла ошибка запроса: {ex}")
    


#Сработаются ли 2 работника
@app.get("/compatibility")
async def compatibility():
    try:
        rec = chat.compatibility()
        return rec
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Произошла ошибка запроса: {ex}")

#Суммаризация резюме +
@app.post("/summarize_resume")
async def summ_rec(request: FullResume):
    try:
        summary = chat.summ_rec(request.full_resume)
        return summary
    
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Произошла ошибка запроса: {ex}")
    


# Суммаризированный расклад Таро по персональной информации пользователя +
@app.post("/summarize_tarot_spread")
async def summ_tarot(request: TarotSpread):
    try:
        summary = chat.summ_tarot_full(request.taro_spred)
        return summary
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Произошла ошибка запроса: {ex}")
    


#Расклад таро по 1 карте для кандидата +
@app.post("/tarot_one")
async def one_tarot_spread(request: SummResume):
    try:
        tarot_spread = chat.tarot_one(request.resume_summary)
        return tarot_spread
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Произошла ошибка запроса: {ex}")
        


#Полный расклад Таро по персональной информации пользователя +
@app.post("/tarot_spread") #Добавить удаление доп символов
async def full_tarot_spread(request: SummResume):
    try:
        tarot_spread = chat.tarot_spread(request.resume_summary)
        return tarot_spread
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Произошла ошибка запроса: {ex}")
    


#Расклад по заданному вопросу +
@app.post("/question_tarot_spread")
async def question_tarot_spread(request: Question):
    try:
        print(request.user_question)
        rec = chat.question(request.user_question)
        return rec
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Произошла ошибка запроса: {ex}")
    


#создание карты компетенции
@app.post("/competency_map")
async def competency_map(request: TarotSpread):
    try:
        rec = chat.competency_map(request.taro_spred)
        return rec
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Произошла ошибка запроса: {ex}")
    

#Заполнение данных профиля +
@app.post("/profile_extract")
async def profile_extract(request: FullResume):
    try:
        print(1)
        rec = chat.profile_extract(full_resume = request.full_resume)
        return rec
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Произошла ошибка запроса: {ex}")
    

    



#Характеристика с прошлых мест работы +
@app.post("/work_history_review")
async def work_history_review(request: FullResume):
    try:
        rec = chat.work_history_review(request.full_resume)
        return rec
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Произошла ошибка запроса: {ex}")
    




#Запрос для генерации ответа пользователю +
@app.post("/feedback")
async def feedback_1(request: FeedBack):
    try:
        print(1)
        rec = chat.feedback(request.candidate_name, request.feedback_type)
        return rec
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Произошла ошибка запроса: {ex}")
    



#Рекомендательная система +
@app.post("/recommendations")
async def recommendations(request: SummResume):
    try:
        rec = chat.recommendations(request.resume_summary)
        return rec
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Произошла ошибка запроса: {ex}")








if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)