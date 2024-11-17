from pathlib import Path
from datetime import datetime
import uuid
import shutil
import models
import requests
from pdf_adapter import pdf_reader, extract_first_image_from_pdf

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, File, UploadFile, Form
from fastapi.responses import FileResponse

from sqlalchemy.orm import Session, joinedload
from database import SessionLocal, engine

API_TARO = 'http://go.itatmisis.ru:8002'

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
UPLOAD_FILE_PHOTO = Path('photo/')
UPLOAD_FILE_PHOTO.mkdir(parents=True, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def start():
    return {"message": "I am working!"}

@app.get('/get_taro_card/')
async def get_photo(card):
   return FileResponse('./taro/' + card + '.png')

@app.get('/get_pdf_resume/')
async def get_photo(name):
   return FileResponse('./resumes/' + name)


@app.get('/get_profiles/')
async def get_profiles(offset: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    result = db.query(models.UserProfile).offset(offset).limit(limit).all()
    return {
        'offset' : offset,
        'limit' : limit,
        'result': result
    }

@app.get('/get_profile/{id}')
async def get_profile(id:int, db: Session = Depends(get_db)):
    result = db.query(models.UserProfile).filter(models.UserProfile.user_profile_id == id).first()
    return result

@app.get('/get_taros/')
async def get_taros(
    status: str,
    offset: int = 0, 
    limit: int = 10,
    db: Session = Depends(get_db)
    ):
    result = db.query(models.UserTaro).filter(models.UserTaro.status == status)\
        .options(joinedload(models.UserTaro.user_profile))\
        .offset(offset).limit(limit).all()
    return {
        'offset' : offset,
        'limit' : limit,
        'result': result
    }

@app.get('/get_taro/')
async def get_taro(
    id : int,
    status: str,
    offset: int = 0, 
    limit: int = 10,
    db: Session = Depends(get_db)
    ):
    result = db.query(models.UserTaro).filter(models.UserTaro.user_profile_id == id)\
        .filter(models.UserTaro.status == status)\
        .options(joinedload(models.UserTaro.user_profile))\
        .offset(offset).limit(limit).first()
    return {
        'offset' : offset,
        'limit' : limit,
        'result': result
    }


@app.post('/post_answer/')
async def post_answer(
    question: str = Form(...)
):
    payload = {
        'question': question
    }
    response = requests.post(f'{API_TARO}/question_tarot_spread', json=payload)
    data = response.json()
    return data


@app.post('/post_resume/')
async def post_resume(
    db : Session = Depends(get_db),
    file: UploadFile = File(None)
):
    if file is None:
        return {'message': 'Неверно введены данные.'}
    else:
        filename = file.filename.replace(' ', '')
        new_filename = f'{uuid.uuid4()}_{Path(filename)}'
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
    
    pdf_text = pdf_reader(file_location)
    #path_pdf_photo = extract_first_image_from_pdf(file_location, UPLOAD_FILE_PHOTO)
    payload = {
        'full_resume': pdf_text
    }
    response = requests.post(f'{API_TARO}/profile_extract', json=payload)
    data = response.json()

    payload_rec = {
        'resume_summary': data['summary_by_resume']
    }
    recommendation = requests.post(f'{API_TARO}/recommendations', json=payload_rec)
    rec = recommendation.json()
 
    db_profile = models.UserProfile(
        full_name = data['name'],
        phone_number = data['phone_number'],
        salary = data['salary'],
        email = data['email'],
        birthday = data['birthday'],
        prof = data['prof'],
        city = data['city'],
        education = data['education'],
        faculty = data['faculty'],
        experience = data['experience'],
        recomendation = rec['content'],
        summary_by_resume = data['summary_by_resume'],
        job_experience = data['job_experience'],
        about = data['about'],
        url_photo = '',
        resume_id = db_resume.resume_id
    )
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)

    return {'message': 'Сохранение резюме и создание профиля прошло успешно.'}

@app.post("/post_taro_spread/")
async def post_taro_spread(
    taro_status: str,
    id: int,
    db: Session = Depends(get_db)
):
    user_profile = db.query(models.UserProfile).filter(models.UserProfile.user_profile_id == id).first()
    payload = {
        'full_resume': user_profile.summary_by_resume
    }
    if taro_status == 'compatibility':
        response = requests.get(f'{API_TARO}/compatibility')
    else:
        response = requests.post(f'{API_TARO}/tarot_spread', json=payload)
    data = response.json()

    db_taro = models.UserTaro(
        user_profile_id = user_profile.user_profile_id,
        taro_info = data['content'],
        cards = ','.join(list(data['tarot'].keys())),
        status = taro_status
    )
    db.add(db_taro)
    db.commit()
    db.refresh(db_taro)

    return db_taro


@app.get('/get_competency/')
async def get(
    id: int,
    db: Session = Depends(get_db)
):
    info = db.query(models.Metrics).filter(models.Metrics.taro_id == id).first()
    return info


@app.post('/post_competency_map/')
async def post(
    id: int,
    db: Session = Depends(get_db)
):
    user_taro = db.query(models.UserTaro).filter(models.UserTaro.user_profile_id == id).first()

    payload = {
        'taro_spred': user_taro.taro_info
    }
    response = requests.post(f'{API_TARO}/competency_map', json=payload)
    data = response.json()

    db_metrics = models.Metrics(
        taro_id = user_taro.taro_id,
        stress_resistance = data['content']['Стрессоустойчивость'],
        flexibility = data['content']['Гибкость'],
        communication_skills = data['content']['Коммуникабельность'],
        creativity = data['content']['Креативность'],
        initiative = data['content']['Инициативность'],
        leadership_qualities = data['content']['Лидерские качества'],
        professional_competence = data['content']['Профессиональная компетентность'],
        ability_decisions = data['content']['Умение принимать решения'],
        hard_work = data['content']['Трудолюбивость'],
        organizational_skills = data['content']['Организаторские способности'],
        productivity = data['content']['Результативность труда'],
        teamwork = data['content']['Работа в команде']
    )
    db.add(db_metrics)
    db.commit()
    db.refresh(db_metrics)
    return db_metrics

@app.post('/tarot_one/')
async def post(
    id: int,
    db: Session = Depends(get_db)
):
    pass
