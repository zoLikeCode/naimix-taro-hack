from pathlib import Path
from datetime import datetime
import uuid
import shutil
import models

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

UPLOAD_FILE_RESUMES = Path('resumes/')
UPLOAD_FILE_RESUMES.mkdir(parents=True, exist_ok=True)
UPLOAD_FILE_TARO = Path('taro/')
UPLOAD_FILE_TARO.mkdir(parents=True, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def start():
    return {"message": "I am working!"}

@app.post("/post_resume/")
async def post_resume(
    db : Session = Depends(get_db),
    file: UploadFile = File(None)
):
    if file is None:
        return {'message': 'Неверно введены данные.'}
    else:
        new_filename = f'{uuid.uuid4()}_{Path(file.filename)}'
        file_location = UPLOAD_FILE_RESUMES / new_filename
        with file_location.open('wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
    
    db_resume = models.Resume(
        url_to_resume = new_filename,
        download_date = datetime.now()
    )
    db.add(db_resume)
    db.commit()
    db.refresh(db_resume)
    return db_resume

