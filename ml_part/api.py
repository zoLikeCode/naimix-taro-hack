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


print(1)