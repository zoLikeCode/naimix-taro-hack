from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, File, UploadFile, Form, HTTPException
from fastapi.responses import FileResponse

from sqlalchemy.orm import Session, joinedload
from database import SessionLocal, engine


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
    expose_headers=["*"],  
)

@app.get("/")
async def root():
    return {"message": "Hello World!"}
