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
from tarot import get_tarot, parse_txt_files, process_tarot_data







class Api:
    def __init__(self, API_KEY):
        self.data = parse_txt_files('prompts/')
        self.model = ChatMistralAI(api_key = API_KEY, model_name = 'ministral-8b-latest')

    
    #Суммаризация резюме
    def summ_rec(self, resume_text):
        text_prompt = self.data['summ_rec']

        prompt = PromptTemplate(
            template = text_prompt,
            input_variables=["resume_text"]
        ).format(resume_text=resume_text)

        rec = self.model.invoke(prompt)
        return rec
    
    #Полный расклад Таро по персональной информации пользователя
    def tarot_spread(self, resume_summary):
        """"
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

        return {"content": rec.content, "tarot": rec.tarot}
    
    #Суммаризация таро для 3 карт
    def summ_tarot_full(self, resume_summary):
        """"
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
            "content": rec.content,
            "tarot": full_taro_spread['tarot']
        }

    
    def tarot_one(self, resume_summary):
        """"
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

        return {"content": rec.content, "tarot": rec.tarot}
    

    def question(self, question):
        """"
        question: str - Вопрос пользователя
        return -> Ответ человеку на основе 3 карт
        """
        text_prompt = self.data['question']
        cards = get_tarot(model = self.model, data = self.data, N = 3)


        prompt = PromptTemplate(
            template=text_prompt,
            input_variables=["cards", "question"]
        ).format(cards=cards, question=question)

        rec = self.model.invoke(prompt)
        rec.tarot = cards

        return {"content": rec.content, "tarot": rec.tarot}
    

    def forecast(self):
        """
        Выдаёт хороший ли сегодня день для найма отрудников на основании 3 карт
        """
        print('Работает forecast')

        text_prompt = self.data['forecast']
        cards = get_tarot(model = self.model, data = self.data, N = 3)


        prompt = PromptTemplate(
            template=text_prompt,
            input_variables=["cards"]
        ).format(cards=cards)

        rec = self.model.invoke(prompt)
        rec.tarot = cards

        return {"content": rec.content, "tarot": rec.tarot}
    

    def competency_map(self, resume_summary):
        text_prompt = self.data['competency_map']
        full_taro_spread = self.tarot_spread(resume_summary)

        prompt = PromptTemplate (
            template=text_prompt,
            input_variables=["full_taro_spread"],
        ).format(full_taro_spread = full_taro_spread['content'])
        
        rec = self.model.invoke(prompt)
        rec.content = process_tarot_data(rec.content)
        rec.tarot = full_taro_spread['tarot']

        return {"content": rec.content, "tarot": rec.tarot}
    




    
