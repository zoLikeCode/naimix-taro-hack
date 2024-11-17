import os
import time
import uuid
import logging
from functools import wraps
from typing import Any, Awaitable, Callable
from datetime import datetime, timedelta
import re

import asyncio
from fastapi import HTTPException
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
from langchain_mistralai.chat_models import ChatMistralAI
from logging.handlers import RotatingFileHandler
import contextvars
import json
from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser
from tarot import get_tarot, parse_txt_files, date_parsing, cleaner
#from langchain_community.chat_models import GigaChat



def handle_exceptions(func):
    """
    Декоратор для обработки всех ошибок в _chain_*
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        repetition  = kwargs.get('repetition') 
        try:
            return func(*args, **kwargs)
            
        except Exception as ex:
            
            if repetition  < 5:  
                wait_time = 1 + repetition  / 10
                time.sleep(wait_time) 
                repetition += 1
                kwargs['repetition'] = repetition
                return wrapper(*args, **kwargs)
            else:
                return ex
            
    return wrapper
                



class Api:
    def __init__(self, API_KEY):
        self.data = parse_txt_files('prompts/')
        self.model = ChatMistralAI(api_key = API_KEY, model_name = 'ministral-8b-latest')
        #self.model = GigaChat(credentials=API_KEY, verify_ssl_certs=False)
        a = self.model.invoke('Как у тебя дела?')
        print(a)

    
    #Суммаризация резюме
    @handle_exceptions
    def summ_rec(self, full_resume: str, repetition: int = 0) -> str:
        """
        Функция для суммаризации письма

        full_resume - резюме кандидата
        return -> суммаризированное резюме
        """
        text_prompt = self.data['summ_rec']

        prompt = PromptTemplate(
            template = text_prompt,
            input_variables=["resume_text"]
        ).format(resume_text=full_resume)

        rec = self.model.invoke(prompt).content
        return cleaner(rec)
    
    @handle_exceptions
    def tarot_spread(self, resume_summary: str, repetition: int = 0) -> dict:
        """"
        Полный расклад Таро по персональной информации пользователя

        resume_summary: str - суммаризация резюме
        return -> расклад таро
        """
        text_prompt = self.data['tarot_spread']
        cards = get_tarot(model = self.model, data = self.data, N = 3)


        prompt = PromptTemplate(
            template=text_prompt,
            input_variables=["sum_resume", "cards"]
        ).format(sum_resume=resume_summary, cards=cards)

        rec = self.model.invoke(prompt)
        rec.tarot = cards

        return {"content": cleaner(rec.content), "tarot": rec.tarot}
    

    @handle_exceptions
    def summ_tarot_full(self, resume_summary: str, repetition: int = 0) -> dict:
        """"
        Суммаризация таро для 3 карт

        resume_summary: str - суммаризация резюме
        return -> суммаризированный расклад таро
        """
        text_prompt = self.data['summ_tarot_full']
        full_taro_spread = self.tarot_spread(resume_summary)

        prompt = PromptTemplate(
            template=text_prompt,
            input_variables=["full_taro_spread"]
        ).format(full_taro_spread=full_taro_spread['content'])

        rec = self.model.invoke(prompt)


        return{
            "content": cleaner(rec.content),
            "tarot": full_taro_spread['tarot']
        }

    
    @handle_exceptions
    def tarot_one(self, resume_summary: str, repetition: int = 0) -> dict:
        """"
        Функция для ответа на вопрос с 1 картой

        resume_summary: str - суммаризация резюме
        return -> расклад на одной карте
        """
        text_prompt = self.data['tarot_one']
        cards = get_tarot(model = self.model, data = self.data, N = 1)
        prompt = PromptTemplate(
            template=text_prompt,
            input_variables=["sum_resume", "cards"]
        ).format(sum_resume=resume_summary, cards=cards)

        rec = self.model.invoke(prompt)
        rec.tarot = cards

        return {"content": cleaner(rec.content), "tarot": rec.tarot}
    

    @handle_exceptions
    def question(self, question: str, repetition: int = 0) -> dict:
        """"
        question: str - Вопрос пользователя
        return -> Ответ человеку на основе 3 карт
        """
        print('работает question')
        text_prompt = self.data['question']
        cards = get_tarot(model = self.model, data = self.data, N = 3)

        prompt = PromptTemplate(
            template=text_prompt,
            input_variables=["cards", "question"]
        ).format(cards=cards, question=question)

        rec = self.model.invoke(prompt)
        rec.tarot = cards

        return {"content": cleaner(rec.content), "tarot": rec.tarot}
    

    @handle_exceptions
    def forecast(self, repetition: int = 0) -> dict:
        """
        Выдаёт хороший ли сегодня день для найма отрудников на основании 3 карт
        """

        text_prompt = self.data['forecast']
        cards = get_tarot(model = self.model, data = self.data, N = 3)


        prompt = PromptTemplate(
            template=text_prompt,
            input_variables=["cards"]
        ).format(cards=cards)

        rec = self.model.invoke(prompt)
        rec.tarot = cards

        return {"content": cleaner(rec.content), "tarot": rec.tarot}
    

    @handle_exceptions
    def competency_map(self, taro_spred: str, repetition: int = 0) -> dict:
        """
        Создание компетенционной карты

        resume_summary -> суммаризированное резюме
        return -> словарь с качествами участника
        """
        print(2)
        text_prompt = self.data['competency_map']

        prompt = PromptTemplate (
            template=text_prompt,
            input_variables=["full_taro_spread"],
        ).format(full_taro_spread = taro_spred)

        rec = self.model.invoke(prompt)
        rec.content = date_parsing(rec.content)
        

        return {"content": rec.content}
    

    @handle_exceptions
    def work_history_review(self, full_resume: str, repetition: int = 0) -> dict:
        """
        Создание компетенционной карты

        full_resume -> полное резюме
        return -> словарь с историей работы
        """

        text_prompt = self.data['work_history_review']
        cards = get_tarot(model = self.model, data = self.data, N = 3)

        prompt = PromptTemplate(
            template=text_prompt,
            input_variables=["resume_text", "cards"]
        ).format(resume_text=full_resume, cards=cards)

        rec = self.model.invoke(prompt)
        rec.tarot = cards

        return {"content": cleaner(rec.content), "tarot": rec.tarot}
    

    @handle_exceptions
    def profile_extract(self, full_resume: str, repetition: int = 0) -> dict:
        """
        Используется для заполнения базы данных для нового кандидата

        full_resume -> полное резюме
        return -> словарь с всеми данными
        """
        text_prompt = self.data['profile_extract']
        full_resume = full_resume
        prompt = PromptTemplate (
            template=text_prompt,
            input_variables=["resume_text"]
        ).format(resume_text = full_resume)
        rec = self.model.invoke(prompt).content
        rec = date_parsing(rec)
        rec['summary_by_resume'] = self.summ_rec(full_resume)
        return rec
    

    @handle_exceptions
    def feedback(self, candidate_name: str, feedback_type: int, repetition: int = 0) -> str: 
        """
        Функция генерирует фидбек для кандидата, учитывая положительный или
        отрицаьельный результат найма

        candidate_name = ФИО кандидата
        feedback_type = 1/0, в зависимости от готовности взять на работа

        return -> готовый фидбек
        """
        text_prompt = self.data['feedback']

        prompt = PromptTemplate(
            template=text_prompt,
            input_variables=["candidate_name", "feedback_type"]
        ).format(candidate_name=candidate_name,
                feedback_type=feedback_type)

        rec = self.model.invoke(prompt).content
        return cleaner(rec)
        

    @handle_exceptions
    def recommendations(self, resume_summary: str, repetition: int = 0) -> dict:
        """
        Функция для получения рекомендаций Hr, как лучше всего общаться с пользователем

        resume_summary -> суммаризированное резюме

        return -> рекомендация на основе карт таро
        """

        text_prompt = self.data['recommendations']
        taro_spread = self.tarot_spread(resume_summary)
        cards = taro_spread['tarot']

        prompt = PromptTemplate(
            template=text_prompt,
            input_variables=["cards", "full_taro_spread"]
        ).format(cards = cards,
                full_taro_spread = taro_spread['content'])
        
        rec = self.model.invoke(prompt)
        rec.tarot = taro_spread['tarot']
        
        return {"content": cleaner(rec.content), "tarot": rec.tarot}
    
    @handle_exceptions
    def compatibility(self, repetition: int = 0) -> dict:
        """
        Функция для предсказания смогут ли сработаться 2 человека 

        return -> Сможет или нет, и почему
        """
        text_prompt = self.data['compatibility']
        cards = get_tarot(model = self.model, data = self.data, N = 3)

        prompt = PromptTemplate(
            template=text_prompt,
            input_variables=["cards"]
        ).format(cards=cards)

        rec = self.model.invoke(prompt)

        return {"content": cleaner(rec.content), "tarot": cards}


        
    




    
